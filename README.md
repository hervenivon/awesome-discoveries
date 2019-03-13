---
description: Welcome to awesome-discoveries
title: awesome-discoveries introduction
---

# Introduction

This document is a curated list of useful, inspiring, fascinating, and eclectic discoveries and thoughts I made and produced during my readings, experiments and job decisions making being a startup advisor and the CTO for a world leading drone company. Some topics are highly technical, some are not.

This document was written mainly as a guide for my future self, a tool to precisely remember what it means building something, helping people to grow, and helping never to reinvent the weel.

This document exposes some of my ideas and views expressed are my own.

## Inspirational resources

My list of inspirational resources I digg to do technology watch.

* [arXiv](https://arxiv.org/) - The million e-prints open access to scientific papers that democratized Machine Learning over the globe. 99% of, not to say all, papers we were using are coming from that place. Even for not professional activities, it is inspiring to look that source.
* [github](https://www.github.com) - GitHub again, with [explore](https://github.com/explore) you will discover a lot of inspiring projects.
* [MIT Technology Review](https://www.technologyreview.com/) - An endless stream of popular science, in particular in machine learning. The only one to which I have been willing to pay a subscription so far.
* News letters:
  * [Data Elixir](https://dataelixir.com/) - My most productive and de facto favorite newsletter regarding Artificial Intelligence and Data science in general.
  * [Changelog](https://changelog.com/weekly) - Staying up to date with the developer community and finding fun stuffs.
  * [Inside AI](https://inside.com/ai) - A lot of AI news, sometimes too many
  * [UX Collective](https://newsletter.uxdesign.cc/) - When you are building a product and you want your customer to fall in love with your product, you need basic knowledge of User eXperience. This newsletter will give you a very good idea of what's going on.
* Companies:
  * Providing data science and AI "as a service":
    * [namr](https://namr.com/) - Their mission is to create value from open data.
    * [deepomatic](https://www.deepomatic.com/) - Concept is providing AI implementation acceleration service for fortune 500.
    * [mobeye](https://www.mobeye-app.com/en/home) - How to crowdsource data annotation through a mobile application that let's people earn money
    * [fritz.ai](https://www.fritz.ai) - Focus on mobile, provide a set of available models and allows for an higher pricing some model customization
    * [algorithmia](https://algorithmia.com/) - Model provisioned as an API
  * Providing github like services dedicated to ML:
    * [Comet.ml](https://comet.ml)
* Various:
  * [aiindex2018](http://cdn.aiindex.org/2018/AI%20Index%202018%20Annual%20Report.pdf) - The one place to go if you need insights into Artificial Intelligence in numbers: from the number of papers published by category to state of the art performances and human-level performance milestones going through VC funding landscape.
  * [distill.pub](https://distill.pub/) - This is an attempt to modernize the main issues with the traditional printed scientific papers in our area of computer science and machine learning over large amount of data: clarity, reproducibility, interactivity. `PDF` files are from another age. `distill.pub` is an expression of our age.

## Must reads

There are a couple of books mentioned in this document, here is my must reads:

* [Edward Tufte's The Visual Display of Quantitative Information](https://amzn.to/2ROaWUl) - The first book to read when you are entering the world of data visualization.
* [Eric Rise's The lean startup](https://amzn.to/2RDDf3H) - This book that made become the CTO of a startup. It taught me the lean approach and made me save so much time
* [Toby Segaran's Programming Collective Intelligence](https://amzn.to/2HiJrgc) - This book built my interest for intelligent applications, it gives me a taste of how important are data in modern applications, and it was fun to read and to apply.

## Feeback is welcome

Even tough this document was first built for myself as a way to track my knowledge ans discoveries, any feedback or questions are more than welcome 😊.

## Table of content

{% page-ref page="docs/architecture-and-infrastructure/README.md" %}
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

## Technical details

In case you fork that repository, it is supported by `Python` scripts, here are some details that might be helpful.

### Pre-requisites

Conda must be [installed](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation).

Then create an environment dedicated to this project:

1. Create `conda` environment: `$> conda create --name ad python=3.7 ipython`
2. Activate `conda` environment: `$> conda activate ad`
3. Install other requirements: `$> pip install -r requirements.txt`
