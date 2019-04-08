# Data science

To start this section, I would like to emphasize how wrong some of us are approching any data science related topics, I'm pleading for generalists team in opposition to specialists, in particular in early stages of a project. From the talks and meetups I assisted to my own experience, I confirm that [you learn on the go, not before you go](https://hbr.org/2019/03/why-data-science-teams-need-generalists-not-specialists) and, that a strong computer scientist is better than two PhD.

Some drawbacks of specialists teams:

1. It narrows team's point of view - Specialization rewards people augmenting their knowledge in a particular area focus and digging their expertise domain. A way more rewarding path is serendipity and curiosity that a generalist is more willing to trigger
1. It increases coordination cost - The number of relationships $$(r)$$ [grows as a function of members](https://amzn.to/2HGwixJ) $$(n)$$ according to this equation: $$r = (n^2-n) / 2$$. And, each relationship involves some coordination cost. And, with growing team, more meetings are usually involved. As you need as many specialists as the number of possible topics involved onto your project, that increase your coordination cost.
1. It augments your time to market - Not mentionning the coordination cost increase, if you build teams of PhD, it is likely that they won't be able to produce production ready programs. You will need to go through an industrialisation phase and sometimes to reimplement everything.

I'm not ready yet to remove PhD from the equation, my experience proved that their skills were necessary to trigger our deep learning projects; others are:

> "For more than 95% of use cases where data science or machine learning is involved, you should hire rock solid computer scientists instead of PhDs" - Werner Vogels, VP and CTO of Amazon, Fireside chat @ Station F on Tue 19 Jun. 2018

That still kind of makes sense. If you account for all the services and frameworks that are accessible today, all the pre-trained models or available algorithms, it is likelly that your project is going to fit in one of the boxes using on the shelves ready to serve tools. You'll need PhDs if you are on the fringe of existing solutions or if you tried everything that exists and it doesn't work. In our case - more details in the [artificial intelligence](/docs/artificial-intelligence) section, we were mainly dealing with aerial imagery taken from drones. And, almost nothing existed in that space at the time.

## Collaboration and reproductibility

As with artificial intelligence, data science is subject to reproducibility issues. We cannot just account for granted provided datavizualisation or explanation. As is enforcing [Bret Victor](http://worrydream.com/) in all his talks, being able to interact and to reproduce paves the way to a better understanding of the analyzed topic.

They are several initiative directed toward collaboration and reproductibilty enhancement of data manipulation programs. Some of them.

* [Colaboratory](https://colab.research.google.com/) - It is a research tool for machine learning education and research, a Jupyter notebook environment that requires no setup to use. And it comes with free GPUs
* [Iodide](https://alpha.iodide.io/) - Mozilla joining the game of reproducible data-science
* [Observable](https://observablehq.com/) - The famous author of [d3.js](https://d3js.org/) javascript library - I named [Mike Bostock](https://twitter.com/mbostock) - announced in April 2017 ["A Better Way to Code"](https://medium.com/@mbostock/a-better-way-to-code-2b1d2876a3a0).
* [Kaggle](https://www.kaggle.com) - "The place to do datascience", learn, share and access dataset, share and create algorithms, compete

## Data management

* [DVC](https://dvc.org/doc/dvc-philosophy/core-features) - A neat structured approach to the data science workflow management aiming to become a standard as git has become in the development workflow.

## Dataviz

* [Edward Tufte’s The Visual Display of Quantitative Information](https://amzn.to/2ROaWUl) - The first book to read when you are entering the world of data visualization.
* [3rd Wave Data Visualization](https://towardsdatascience.com/3rd-wave-data-visualization-824c5dc84967) - Elijah Meeks author of [semiotic](https://github.com/emeeks/semiotic) - A react + d3.js library, a famous combo I experienced with success and pleasure - points to problems into the current landscape of data visualization.
* [PCA, t-SNE, and UMAP: Modern Approaches to Dimension Reduction](https://www.reddit.com/r/datascience/comments/8rfrqg/pca_tsne_and_umap_modern_approaches_to_dimension/) - You always have too many dimension to play with, and a picture still worth a thousand words. Here enters dimension reduction algorithms
* [Dataviz Collection](https://www.pinterest.fr/acatonrails/data-viz/) - I'm collecting things a lot, here is my personnal collection of inspiring Datavizualisation.
* Beware of the answers you'll find and always be skeptic first. That a service you owe yourself:
  * [Curve Fitting](https://xkcd.com/2048/) - A drawing worths a thousand words.
  * [Importance of Skepticism in Data Science](https://jhu-advdatasci.github.io/2018/lectures/12-being-skeptical.html) - This long code detailed lecture aims at illustrating the bias that you might follow when you are interpreting data you have manipulated. _(`R`)_
