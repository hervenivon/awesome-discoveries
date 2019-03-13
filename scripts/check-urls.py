#!/usr/bin/env python3

import os, re
import certifi
import urllib3
import urlextract
import queue
import threading

'''
High level algorithm

List all files with a certain pattern, excluding some files
Extracts all urls and associated file path. Aggregates results urls in a queue
Compute unique urls
Checks urls all urls, computes progress, print out issues

'''

included_extensions = ['md', 'tsv', 'csv']
file_excluded = ['SUMMARY.md', 'TODO.md']
root_path = '.'


# listing of files
files = [os.path.join(root, file) for root, dirs, files in os.walk(root_path)
         for file in files
         if any(file.endswith(ext) for ext in included_extensions)
         if all(file != excluded for excluded in file_excluded)]

# url extraction
extractor = urlextract.URLExtract()
urls = []
for file in files:
  with open(file) as f:
    urls.extend(list(map(lambda x: (file, x), extractor.find_urls(f.read()))))

unique_urls = {}
for url in urls :
  unique_urls.setdefault(url[1], []).append(url[0])
unique_urls = [(key, values) for key, values in unique_urls.items()]
print('%d unique urls to verify over %d total' % (len(unique_urls), len(urls)))



# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings()

def validate_url(http=None, url='', refs=[]):
  try:
    response = http.request('GET', url)
    if (response.status == 200):
      return (True, url, refs, {})
    else:
      return (False, url, refs, response.status)
  except (urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError, ConnectionRefusedError, UnicodeEncodeError) as e:
    return (False, url, refs, e)

from multiprocessing import Pool
from tqdm import tqdm

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15'
http = urllib3.PoolManager(
  cert_reqs='CERT_REQUIRED',
  ca_certs=certifi.where(),
  headers={'user-agent': user_agent},
  retries=urllib3.Retry(5, redirect=5),
  timeout=10.0)

def parallel_url_validation_worker(args):
  return validate_url(http, args[0], args[1])

def parallel_url_validation():
  # Use many threads (15 max, or one for each url)
  num_worker_threads = min(15, len(unique_urls))
  pool = Pool(processes=num_worker_threads)

  results = []
  with tqdm(total=len(unique_urls)) as t:
    for res in pool.imap_unordered(parallel_url_validation_worker, unique_urls):
      results.append(res)
      t.update(1)

  success_per_file = {}
  errors_per_file = {}
  for res in results :
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
  errors_per_file = [(key, values) for key, values in errors_per_file.items()]
  success_per_file = [(key, values) for key, values in success_per_file.items()]

  for success in success_per_file:
    print('✓ %d urls successfully verified in "%s":' % (success[1], success[0]))

  for file, failures in errors_per_file:
    print('✗ %d verifications failed in file "%s":' % (len(failures), file))
    for failure in failures:
      print('  url: "%s", reason: %s' % (failure[0], failure[1]))

parallel_url_validation()
