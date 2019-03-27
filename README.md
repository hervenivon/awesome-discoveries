---
description: A curated list of awesome discoveries based on my readings.
title: awesome-discoveries introduction
---

# Introduction

This document is a curated list of useful, inspiring, fascinating, and eclectic discoveries and thoughts I made and produced during my readings, experiments and job decisions making being a startup advisor and the CTO of a world leading drone company. Some topics are highly technical; some are not.

This document was written mainly as a guide for my future self, a tool to precisely remember what it means building something, helping people to grow, and growing myself. One can see it as my humble version of the [Encyclopedia of Absolute and Relative Knowledge](http://www.bernardwerber.com/livres/ESRA3.php).

This document exposes some of my ideas and views expressed are my own.

## Inspirational resources 💡

I have several inspirational resources I regularly dig to do technology watch — certain almost every day.

### Publications

I subscribed to several newsletters, and I have my favorite websites.

* [arXiv](https://arxiv.org/) - The million e-prints open access to scientific papers that democratized Machine Learning over the globe. 99% of, not to say all, papers we were using are coming from that place. Even for not professional activities, it is inspiring to look at that source.
* [github](https://www.github.com) - GitHub again, with [explore](https://github.com/explore) you will discover a lot of inspiring projects.
* [MIT Technology Review](https://www.technologyreview.com/) - An endless stream of popular science, in particular in machine learning. The only one to which I have been willing to pay a subscription so far.
* [Kaggle](https://www.kaggle.com) - "The place to do datascience", learn, share and access dataset, share and create algorithms, compete
* Newsletters:
  * [Data Elixir](https://dataelixir.com/) - My most productive and de facto favorite newsletter regarding Artificial Intelligence and Data science in general.
  * [Changelog](https://changelog.com/weekly) - Staying up to date with the developer community and finding fun stuff.
  * [Inside AI](https://inside.com/ai) - A lot of AI news, sometimes too many
  * [UX Collective](https://newsletter.uxdesign.cc/) - When you are building a product, and you want your customer to fall in love with your product, you need basic knowledge of User eXperience. This newsletter will give you an excellent idea of what's going on.

### Companies

The following are companies with new business models, innovative offerings or inspiring founders. These truly stimulate me.

* [namr](https://namr.com/) - Their mission is to create value from open data.
* [deepomatic](https://www.deepomatic.com/) - Their concept is to provide AI implementation acceleration service for fortune 500.
* [mobeye](https://www.mobeye-app.com/en/home) - How to crowdsource data annotation through a mobile application that lets people earn money.
* [fritz.ai](https://www.fritz.ai) - Focuses on mobile, provide a set of available models and allows for higher pricing some model customization.
* [algorithmia](https://algorithmia.com/) - AI models provisioned as APIs.
* [Comet.ml](https://comet.ml) - Provides a GitHub like experience dedicated to ML.

### Others

Some others I look less often, or I refer to time to time.

* [aiindex2018](http://cdn.aiindex.org/2018/AI%20Index%202018%20Annual%20Report.pdf) - The one place to go if you need insights into Artificial Intelligence in numbers: from the number of papers published by category to state of the art performances and human-level performance milestones going through VC funding landscape.
* [distill.pub](https://distill.pub/) - This is an attempt to modernize the main issues we face with the traditional printed scientific papers in computer science and machine learning which now more than ever involve an overabundant amount of data and are nearly impossible to understand on a sheet of paper. Distill.pub brings clarity, reproducibility, and interactivity. `PDF` files are from another age. `distill.pub` is an expression of our time.

## Must reads 📚

There are a couple of books mentioned in this document, and there are some books that inspired me so much. Here are my definite must-reads:

* [Edward Tufte's The Visual Display of Quantitative Information](https://amzn.to/2ROaWUl) - The first book to read when you are entering the world of data visualization.
* [Eric Rise's The lean startup](https://amzn.to/2RDDf3H) - This book led me to become CTO of a startup training me to the "lean approach." So much time saved from this lecture.
* [Toby Segaran's Programming Collective Intelligence](https://amzn.to/2HiJrgc) - This book built my interest for intelligent applications, it gives me a taste of how important are data in modern applications, and it was fun to read and to apply.
* [Yuval Noah Harari's Sapiens: A Brief History of Humankind](https://amzn.to/2WrN6fK) - This book and the followings "Homo Deus" and "21 lessons for the 21st century" were thrilling to discover. They give the key to understand Human relations, from where we are coming from and our possible futures.

## Feeback is welcome 📢

Even though I first wrote this document for myself as a way to track my knowledge and discoveries, any feedback or questions are more than welcome 😊.

## Table of content 🗂

Architecturing an information system and deploying its supporting infrastructure will set its backbone for a while. Doing it right is crucial.
{% page-ref page="docs/architecture-and-infrastructure/README.md" %}

Algorithms are a fascinating topic, this section will handle my favorite.
{% page-ref page="docs/algorithms/README.md" %}

{% page-ref page="docs/artificial-intelligence/README.md" %}

{% page-ref page="docs/blockchain/README.md" %}

{% page-ref page="docs/data-science/README.md" %}

{% page-ref page="docs/development/README.md" %}

{% page-ref page="docs/growing-a-company/README.md" %}

{% page-ref page="docs/growing-a-product/README.md" %}

{% page-ref page="docs/productivity/README.md" %}

{% page-ref page="docs/ux-ui/README.md" %}

{% page-ref page="docs/various/README.md" %}

## Technical details 🛠

This repository is automatically published on [gitbook](https://herve-nivon.gitbook.io/awesome-discoveries/). The next iteration is available with private access on [gitbook](https://herve-nivon.gitbook.io/awesome-discoveries-next/) too. That is, for instance, why a `SUMMARY` file exists.

In case you fork that repository, it is supported by `Python` scripts, here are some details that might be helpful.

### Pre-requisites

Conda must be [installed](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation).

Then create an environment dedicated to this project:

1. Create `conda` environment: `$> conda create --name ad python=3.7 ipython`
2. Activate `conda` environment: `$> conda activate ad`
3. Install other requirements: `$> pip install -r requirements.txt`

### url checker

In order to verify that referenced urls are valid please execute the following in the conda environment at the repository root directory:

```shell
./scripts/check-urls.py -v
```
