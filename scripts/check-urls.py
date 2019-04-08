#!/usr/bin/env python3

import argparse
import certifi
import os
import queue
import re
import threading
import urlextract
import urllib3
from multiprocessing import Pool
from tqdm import tqdm


'''
High level algorithm

List all files with a certain pattern, excluding some files
Extracts all urls and associated file path. Aggregates results urls in a queue
Compute unique urls
Checks urls all urls, computes progress, print out issues

'''
NBMAXPROCESS = 15

ROOT_PATH = '.'
INCLUDED_EXTENSIONS = ['md', 'tsv', 'csv']
FILE_EXCLUDED = ['SUMMARY.md', 'TODO.md']

# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) ' \
              'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
              'Version/11.1.1 Safari/605.1.15'
httpPool = urllib3.PoolManager(
  cert_reqs='CERT_REQUIRED',
  ca_certs=certifi.where(),
  headers={'user-agent': user_agent},
  retries=urllib3.Retry(5, redirect=5),
  timeout=10.0)


# listing of files
def list_files(root_path='.',
               included_extensions=['md', 'tsv', 'csv'],
               file_excluded=['SUMMARY.md', 'TODO.md']):
    files = [os.path.join(root, file)
             for root, dirs, files in os.walk(root_path)
             for file in files
             if any(file.endswith(ext) for ext in included_extensions)
             if all(file != excluded for excluded in file_excluded)]

    return files


# url extraction
def parallel_file_extraction_worker(file):
    extractor = urlextract.URLExtract()
    with open(file) as f:
        return list(map(lambda x: (file, x),
                        extractor.find_urls(f.read())))


def parallel_file_extraction(file_list, verbose=True):
    # Use many threads (NBMAXPROCESS max, or one for each file)
    num_worker_threads = min(NBMAXPROCESS, len(file_list))
    pool = Pool(processes=num_worker_threads)

    results = []
    with tqdm(total=len(file_list), disable=not(verbose)) as t:
        for res in pool.imap_unordered(parallel_file_extraction_worker,
                                       file_list):
            results.extend(res)
            t.update(1)

    # for file in file_list:
    #     results.extend(parallel_file_extraction_worker(file))

    return results


def get_unique_urls(urls):
    unique_urls = {}
    for url in urls:
        unique_urls.setdefault(url[1], []).append(url[0])
    unique_urls = [(key, values) for key, values in unique_urls.items()]

    return unique_urls


def validate_url(http=None, url='', refs=[]):
    try:
        response = http.request('GET', url)
        if (response.status == 200):
            return (True, url, refs, {})
        else:
            return (False, url, refs, response.status)
    except (urllib3.exceptions.NewConnectionError,
            urllib3.exceptions.MaxRetryError,
            ConnectionRefusedError,
            UnicodeEncodeError) as e:
        return (False, url, refs, e)


def parallel_url_validation_worker(args):
    return validate_url(httpPool, args[0], args[1])


def parallel_url_validation(unique_urls=[], verbose=True):
    # Use many threads (NBMAXPROCESS max, or one for each url)
    num_worker_threads = min(NBMAXPROCESS, len(unique_urls))
    pool = Pool(processes=num_worker_threads)

    results = []
    with tqdm(total=len(unique_urls), disable=not(verbose)) as t:
        for res in pool.imap_unordered(parallel_url_validation_worker,
                                       unique_urls):
            results.append(res)
            t.update(1)

    return results


def get_stats(url_results):
    success_per_file = {}
    errors_per_file = {}
    for res in url_results:
        # res[0]: status
        # res[1]: url
        # res[2]: files
        # res[3]: res[0] == False ? reason : {}
        if (not(res[0])):
            for file in res[2]:
                errors_per_file.setdefault(file, []).append((res[1], res[3]))
        else:
            for file in res[2]:
                success_per_file.setdefault(file, 0)
                success_per_file[file] = success_per_file[file] + 1
    errors_per_file = [(key, values)
                       for key, values in errors_per_file.items()]
    success_per_file = [(key, values)
                        for key, values in success_per_file.items()]

    return (errors_per_file, success_per_file)


def generate_argparse():
    parser = argparse.ArgumentParser(
        description='Verify that urls included in files are valid.',
        prog='check-urls.py',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'path', nargs='?',
        default=ROOT_PATH,
        help='Check all files starting for the specified path.\n'
             'Default: %s' % ROOT_PATH)
    parser.add_argument(
        '-e', '--extensions', nargs='*',
        default=INCLUDED_EXTENSIONS,
        help='Only the provided file extensions are parsed.\n'
             'Defaults: %s' % ', '.join(INCLUDED_EXTENSIONS))
    parser.add_argument(
        '-x', '--exclusions', nargs='*',
        default=FILE_EXCLUDED,
        help='Provided files are excluded from the analysis.\n'
             'Defaults: %s' % ', '.join(FILE_EXCLUDED))
    parser.add_argument('-s', '--silent', action='store_true')

    return parser


def main():
    parser = generate_argparse()
    args = parser.parse_args()

    if not args.silent:
        print('Listing files...')
    file_list = list_files(root_path=args.path,
                           included_extensions=args.extensions,
                           file_excluded=args.exclusions)

    if not args.silent:
        print('Extracting urls from %d files...' % len(file_list))
    urls = parallel_file_extraction(file_list, verbose=(not args.silent))
    unique_urls = get_unique_urls(urls)
    if not args.silent:
        print('%d unique urls to verify over %d total' %
              (len(unique_urls), len(urls)))
        print('Checking urls...')

    url_results = parallel_url_validation(unique_urls,
                                          verbose=(not args.silent))
    (errors_per_file, success_per_file) = get_stats(url_results)

    if not args.silent:
        for success in success_per_file:
            print('✓ %d urls successfully verified in "%s":' %
                  (success[1], success[0]))

        for file, failures in errors_per_file:
            print('✗ %d verifications failed in file "%s":' %
                  (len(failures), file))
            for failure in failures:
                print('  url: "%s", reason: %s' % (failure[0], failure[1]))

    if len(errors_per_file) > 0:
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()
