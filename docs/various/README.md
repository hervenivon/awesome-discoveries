# Various

## Charting API

[quickchart](https://quickchart.io/) - Open source API that replace the deprecated [Google Chart API](https://developers.google.com/chart/image/).

Examples:

<img src="https://quickchart.io/chart?bkg=white&c=%7B%0A%20%20bkg%3A%20%22transparent%22%2C%0A%20%20type%3A%20%22doughnut%22%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%0A%20%20%20%20%20%20%22Cooking%22%2C%0A%20%20%20%20%20%20%22Sleeping%20%26%20Dreaming%20about%20solutions%22%2C%0A%20%20%20%20%20%20%22Brainstorming%20with%20my%20team%2C%20value%20their%20work%22%2C%0A%20%20%20%20%20%20%22Design%2C%20Architecture%22%2C%0A%20%20%20%20%20%20%22Prototyping%2C%20Development%22%2C%0A%20%20%20%20%20%20%22Family%20time%2C%20playing%20with%20my%20son%22%2C%0A%20%20%20%20%20%20%22Reading%20news%22%2C%0A%20%20%20%20%5D%2C%0A%20%20%20%20datasets%3A%20%5B%7B%0A%20%20%20%20%20%20data%3A%20%5B3%2C%2024%2C%2031%2C%2015%2C%2010%2C%2010%2C%208%5D%2C%0A%20%20%20%20%20%20backgroundColor%3A%20%5B%0A%20%20%20%20%20%20%20%20%22%23fef0d9%22%2C%0A%20%20%20%20%20%20%20%20%22%23fdd49e%22%2C%0A%20%20%20%20%20%20%20%20%22%23fdbb84%22%2C%0A%20%20%20%20%20%20%20%20%22%23fc8d59%22%2C%0A%20%20%20%20%20%20%20%20%22%23ef6548%22%2C%0A%20%20%20%20%20%20%20%20%22%23d7301f%22%2C%0A%20%20%20%20%20%20%20%20%22%23990000%22%2C%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%7D%5D%0A%20%20%7D%2C%0A%20%20options%3A%20%7B%0A%20%20%20%20title%3A%20%7B%0A%20%20%20%20%20%20display%3A%20true%2C%0A%20%20%20%20%20%20text%3A%20%22My%20worklife%20balance%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20legend%3A%20%7B%0A%20%20%20%20%20%20display%3A%20true%2C%0A%20%20%20%20%20%20position%3A%20%22bottom%22%2C%0A%20%20%20%20%7D%2C%0A%20%20%7D%0A%7D" alt="My work life Balance" />

The above chart is an extract from my CV available [here](https://github.com/hervenivon/CV/releases).

The following will generate you a QR code:

```html
<img scr="https://quickchart.io/qr?text=https%3A%2F%2Fgithub.com%2Fhervenivon%2FCV%2Freleases" alt="My CV link" />
```

[quickchart](https://quickchart.io/) has a playground to get the url already encoded. It transform that code:

```json
{
  bkg: "transparent",
  type: "doughnut",
  data: {
    labels: [
      "Cooking",
      "Sleeping & Dreaming about solutions",
      "Brainstorming with my team, value their work",
      "Design, Architecture",
      "Prototyping, Development",
      "Family time, playing with my son",
      "Reading news",
    ],
    datasets: [{
      data: [3, 24, 31, 15, 10, 10, 8],
      backgroundColor: [
        "#fef0d9",
        "#fdd49e",
        "#fdbb84",
        "#fc8d59",
        "#ef6548",
        "#d7301f",
        "#990000",
      ],
    }]
  },
  options: {
    title: {
      display: true,
      text: "My worklife balance"
    },
    legend: {
      display: true,
      position: "bottom",
    },
  }
}
```

into

```text
https://quickchart.io/chart?bkg=white&c=%7B%0A%20%20bkg%3A%20%22transparent%22%2C%0A%20%20type%3A%20%22doughnut%22%2C%0A%20%20data%3A%20%7B%0A%20%20%20%20labels%3A%20%5B%0A%20%20%20%20%20%20%22Cooking%22%2C%0A%20%20%20%20%20%20%22Sleeping%20%26%20Dreaming%20about%20solutions%22%2C%0A%20%20%20%20%20%20%22Brainstorming%20with%20my%20team%2C%20value%20their%20work%22%2C%0A%20%20%20%20%20%20%22Design%2C%20Architecture%22%2C%0A%20%20%20%20%20%20%22Prototyping%2C%20Development%22%2C%0A%20%20%20%20%20%20%22Family%20time%2C%20playing%20with%20my%20son%22%2C%0A%20%20%20%20%20%20%22Reading%20news%22%2C%0A%20%20%20%20%5D%2C%0A%20%20%20%20datasets%3A%20%5B%7B%0A%20%20%20%20%20%20data%3A%20%5B3%2C%2024%2C%2031%2C%2015%2C%2010%2C%2010%2C%208%5D%2C%0A%20%20%20%20%20%20backgroundColor%3A%20%5B%0A%20%20%20%20%20%20%20%20%22%23fef0d9%22%2C%0A%20%20%20%20%20%20%20%20%22%23fdd49e%22%2C%0A%20%20%20%20%20%20%20%20%22%23fdbb84%22%2C%0A%20%20%20%20%20%20%20%20%22%23fc8d59%22%2C%0A%20%20%20%20%20%20%20%20%22%23ef6548%22%2C%0A%20%20%20%20%20%20%20%20%22%23d7301f%22%2C%0A%20%20%20%20%20%20%20%20%22%23990000%22%2C%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%7D%5D%0A%20%20%7D%2C%0A%20%20options%3A%20%7B%0A%20%20%20%20title%3A%20%7B%0A%20%20%20%20%20%20display%3A%20true%2C%0A%20%20%20%20%20%20text%3A%20%22My%20worklife%20balance%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20legend%3A%20%7B%0A%20%20%20%20%20%20display%3A%20true%2C%0A%20%20%20%20%20%20position%3A%20%22bottom%22%2C%0A%20%20%20%20%7D%2C%0A%20%20%7D%0A%7D
```

The charts are extensively customizable, documentation is available [here](https://www.chartjs.org/docs/latest/).

## Bio inspiration

* [Navigation without a GPS](https://www.soonsoonsoon.com/remplacer-son-gps-par-un-cerveau-de-fourmi) - Inspired from a Sahara desert ant, this ant robot can orient itself without a GPS. After a random exploration behavior, it can go straight back to its departure origin.

## Color picking

[Colorbrewer](http://colorbrewer2.org) is an online tool, and a [npm package](https://www.npmjs.com/package/colorbrewer) that provides a set of color schemes suitable for certain conditions: diverging, colorblind safe, number of classes. While it was meant for maps at first, I use it extensively when it comes to choose colors for any purpose. I just find them elegant 😊. I discovered them through the [d3js](https://github.com/d3/d3) library. [Further reading](http://www.personal.psu.edu/cab38/ColorBrewer/ColorBrewer_updates.html)

## Markdown

* [`gh-md-toc`](https://github.com/ekalinin/github-markdown-toc.go) - Generate table of content from a `.md` file.

## Static web sites

Static web site in some occasions advantageouly replace self hosting services sush as Wordpress. They can be hosted on storage services such as [AWS S3](https://aws.amazon.com/s3/).

* [Publii](https://opencollective.com/Publii) - Is an open source static site CMS management tool
* [Gatsby.js](https://www.gatsbyjs.org) - Is a library that enables static site generation from react
  * [Migrating from Medium to Gatsby](https://www.no.lol/2019-03-16-medium-to-gatsby/) - Medium is really popular, but its T&C changes and pricing policies lead to some “migration escape" like [Hackernoon](http://web.archive.org/web/20190312050147/https://twitter.com/hackernoon/status/1105290961100259328), and now we see such blog posts.
* [hugo](https://gohugo.io/) - Another library to build static sites. A [comparison with gatsby](https://medium.freecodecamp.org/gatsby-vs-hugo-a-detailed-comparison-e78d94f640fc) if you need more insights
* [jekyll](https://github.com/jekyll/jekyll) - The static site generator behing [GiHub Pages](https://pages.github.com/). PlanetJekyll features a jekyll [showcase](http://planetjekyll.github.io/showcase/) of several live website and the associate sources.
