# awesome-discoveries

This document is a curated list of inspiring and eclectic - mostly ordered - discoveries and thoughts I made and produce during my readings, experiments and job decisions making being a startup advisor and the CTO for a world leading drone company.

* [Inspirational resources and must reads](#inspirational-resources-and-must-reads)
* [Topics](#topics)
  * [Architecture and Infrastructure](#architecture-and-infrastructure)
  * [Algorithms](#algorithms)
  * [Artificial Intelligence](#artificial-intelligence)
    * [Embedding](#embedding)
    * [Compression, enhancement](#compression-enhancement)
    * [Natural Language Processing and voice recognition](#natural-language-processing-and-voice-recognition)
    * [Semantic segmentation](#semantic-segmentation)
    * [Medicine](#medicine)
    * [Data Generation](#data-generation)
    * [Understanding deep learning](#understanding-deep-learning)
    * [Games](#games)
    * [Experiments &amp; Art](#experiments--art)
    * [Data](#data)
    * [Performance and hardware](#performance-and-hardware)
    * [Ethics](#ethics)
    * [Sagemaker](#sagemaker)
    * [Various](#various)
    * [Setting a machine learning project](#setting-a-machine-learning-project)
  * [Blockchain](#blockchain)
  * [Data science](#data-science)
  * [Development](#development)
    * [Software design and principles](#software-design-and-principles)
    * [mono repo vs multi repo | microservices vs monolith](#mono-repo-vs-multi-repo--microservices-vs-monolith)
    * [vscode](#vscode)
    * [Languages and technologies](#languages-and-technologies)
      * [Javascript](#javascript)
      * [Python](#python)
      * [Ruby](#ruby)
      * [Bash](#bash)
      * [AWS](#aws)
  * [Growing a company](#growing-a-company)
  * [Productivity tools](#productivity-tools)
  * [UX/UI](#uxui)
  * [Various tools](#various-tools)
* [License](#license)

## Inspirational resources and must reads

My list of inspirational resources I go when I do technology watch.

* [arXiv](http://arxiv.org/) - The 1.5 Million e-prints open access to paper that democratized Machine Learning over the globe. 99% of papers we were using are coming from that place. It is even inspiring to look for information from that source.
* [aiindex2018](http://cdn.aiindex.org/2018/AI%20Index%202018%20Annual%20Report.pdf) - The one place to go if you need insights into Artificial Intelligence in numbers: from the number of papers published by category to state of the art performances and human-level performance milestones going through VC funding landscape.
* [distill.pub](https://distill.pub/) - This is an attempt to modernize the main issues with the traditional printed scientific papers in our area of computer science and machine learning over large amount of data: clarity, reproducibility, interactivity. `PDF` files are from another age. `distill.pub` is an expression of our age.
* [github](https://www.github.com) - GitHub again, with [explore](https://github.com/explore) you will discover a lot of inspiring projects.
* [MIT Technology Review](https://www.technologyreview.com/) - An endless stream of popular science, in particular in machine learning. The only one to which I have been willing to pay a subscription so far.
* [stateoftheart.ai](https://www.stateoftheart.ai) - Not entirely up to date on a few topic I'm aware of, but it deserves a look for everyone interested to get up to speed in a particular area they want to get in. A well ordered index for state of the art results in machine learning.
* News letters:
  * [Data Elixir](https://dataelixir.com/) - My most productive and de facto favorite newsletter regarding Artificial Intelligence and Data science in general.
  * [Changelog](https://changelog.com/weekly) - Staying up to date with the developer community and finding fun stuffs.
* Companies:
  * Providing data science and AI "as a service":
    * [namr](https://namr.com/) - Their mission is to create value from open data.
    * [deepomatic](https://www.deepomatic.com/) - Concept is providing AI implementation acceleration service for fortune 500.
    * [mobeye](https://www.mobeye-app.com/en/home) - How to crowdsource data annotation through a mobile application that let's people earn money
  * Providing github like services dedicated to ML:
    * [Comet.ml](https://comet.ml)

There are a couple of books mentioned in this document, here is my top five must read in alphabetical order:

* [Edward Tufte’s The Visual Display of Quantitative Information](https://amzn.to/2ROaWUl) - The first book to read when you are entering the world of data visualization.
* [Eric Rise's The lean startup](https://amzn.to/2RDDf3H) - This book that made become the CTO of a startup. It taught me the lean approach and made me save so much time

## Topics

### Architecture and Infrastructure

* [CAP Theorem](https://www.itechart.com/blog/all-you-didnt-know-about-cap-theorem/) - The CAP theorem extensive description - and its drawbacks. The CAP (Consistency, Availability, Partition-Tolerance) theorem helps selecting the best suited database solution for a particular problem. In this article, you will also discover its limits.
* Serverless paradigm
  * [Epsagon](https://epsagon.com/) - Observability is as of today the biggest challenge in serverless infrastructure - even with latest AWS enhancements on Cloudwatch, at least allowing textual search across your logs. Epsagon provides an observability SaaS board which creates - among other features - an execution map of all your connected services on a per API call basis. Tremendously useful.
  * [Seed](https://seed.run/) - A solution that industrializes in a few clicks your serverless deployments. Frow manual command line deployment to production ready deployment board in minutes, literally.
  * [The serverless stack](https://serverless-stack.com/) - The guys behind [Seed](https://seed.run/) wrote an amazing book which push you straight to your first true serverless deployment proving how fast a team can soon focus on building value instead of spending time to set an infrastructure.
* AWS
  * [AWS Blog](https://aws.amazon.com/blogs/aws/) - If you want to be amazed by the innovation pace of AWS, be sure to subscribe to their blog, in addition to the day to day announcements you also get hands on blog post and a lot of inspiration.
* Cloud native
  * [Cloud Native Computing Foundation](https://www.cncf.io/) - The entry point to an open source journey in the cloud computing
* Tools for local development
  * [minio.io](https://www.minio.io/features.html) - A distributed object storage server that mimic the "de facto standard API for object storage", named AWS S3.
  * [localstack](https://github.com/localstack/localstack) - The folks aren't really responsive, nor their enterprise offer seems to conclude in one way or another, but there is a lot of value and a lot to learn from that project.
* API design
  * [REST is the new SOAP](https://medium.freecodecamp.org/rest-is-the-new-soap-97ff6c09896d) - An article with a counter-current point of view that emphasizes every negative aspects of `REST`.

### Algorithms

* [Fountain Codes](https://divan.github.io/posts/fountaincodes/) - Transfer information over noisy channels. Example given with [txqr](https://github.com/divan/txqr) a project that uses Animated GQ to transfer data over mobiles.
* Any [Bret Victor](http://worrydream.com/) essays, demo, experiments. This inspired me so much and make myself questioning my day to day life as an engineer. He made me rethink the way we explain and learn things and share them with others. I'm so frustrated not seeing his demo becoming real life products.
  * [Algojammer](https://github.com/ChrisKnott/Algojammer) - A project that stole the idea of "Learning programming" is an attempt to turn Bret's work into reality.

### Artificial Intelligence

If you are new to Artificial Intelligence and machine learning, there is one place to go: the [machine learning glossary](https://developers.google.com/machine-learning/glossary) from the Google developers documentation.

For the complete bibliography, please look at the [bibliography](bibliography.tsv) file.

#### Embedding

* [FaceNet: A Unified Embedding for Face Recognition and Clustering](https://arxiv.org/abs/1503.03832) - A solution which transforms an image into a compact Euclidean space allowing to enhance Face Recognition. [implementation](https://github.com/davidsandberg/facenet) _(`Embedding`, `image2vec`, `Tensorflow`)_
* [Grasp2Vec: Learning Object Representations from Self-Supervised Grasping](https://arxiv.org/abs/1811.06964) - Embedding used in reinforcement learning to represent reality through physical world robot grasping. [Google article](https://ai.googleblog.com/2018/12/grasp2vec-learning-object.html) _(`Embedding`, `image2vec`, `RL`)_

#### Compression, enhancement

* [Learned Video Compression](https://arxiv.org/pdf/1811.06981.pdf) - A traditional codec architecture where elements are replaced by Machine Learning ones. Results: the new codec outperforms all existing video codecs.

#### Natural Language Processing and voice recognition

* Assisted writings
  * ["I want to live"](https://youtu.be/BhKw71AeOg4) - A 60 second clip entirely scripted from an AI studying 15 years of worth of award-winning ads.
  * [Bertie the Forbes' CMS](https://digiday.com/media/forbes-built-a-robot-to-pre-write-articles-for-its-contributors/) - Forbes [announced](https://www.forbes.com/sites/forbesproductgroup/2018/07/11/entering-the-next-century-with-a-new-forbes-experience/#5e9b28803bf4) its new AI powered CMS (Content Management System) where AI helps and support content creator from image selection to draft article writings.
* [Accurate Online Speaker Diarization with supervised learning](https://ai.googleblog.com/2018/11/accurate-online-speaker-diarization.html) - Detect interlaced speakers in a speech. But beware, code is not the original and you cannot access data. _(`PyTorch`, `Embedding`)_

#### Semantic segmentation

Semantic segmentation which is the practice of categorizing an image at the pixel level. i.e., semantic segmentation assigns a class to each pixel in an image was at the art of our core product at Redbird. There are a lot activities around that topic where state of the art is still not as accurate as human. I have written a [medium post](https://medium.com/@hervenivon/crafting-the-future-was-just-the-beginning-herve-nivon-3b7312a73184) where you will find further information regarding our project.

Here are the most relevant findings we leverage for our project and some more recent ones that can enhance it:

* [Auto-DeepLab: Hierarchical Neural Architecture Search for Semantic Image Segmentation](https://arxiv.org/pdf/1901.02985.pdf) - The next DeepLab generation which was already the state of the art in this field.
* [Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics](https://arxiv.org/pdf/1705.07115.pdf) - Multi-task learning for segmentation and instance segmentation with a multi-task loss.
* [Panoptic Feature Pyramid Networks](https://arxiv.org/pdf/1901.02446.pdf) - Unified architecture for multi task segmentation and instance segmentation.

#### Medicine

* [Brain2Speech](https://www.sciencemag.org/news/2019/01/artificial-intelligence-turns-brain-activity-speech) - Experiment using AI to get our voice out of our head automatically. The promise to an accessible world for disable people.
* [Learning to Design RNA](https://arxiv.org/pdf/1812.11951.pdf) - Reinforcement Learning used to design RNA sequence to test _(`RL`)_
* [Face2Gene](https://www.nature.com/articles/d41586-019-00027-x#ref-CR1) - From Professional crowdsourcing to real life medicine aid use case, the face2gene application that spot genetic disorders is a promise for future medicine.
* [Artificial Intelligence Can Detect Alzheimer’s Disease in Brain Scans Six Years Before a Diagnosis](https://www.ucsf.edu/news/2018/12/412946/artificial-intelligence-can-detect-alzheimers-disease-brain-scans-six-years) - It is not a question of time any more, it is already here.

#### Data Generation

* Face Generation
  * [Inside the world of AI that forges beautiful art and terrifying deepfakes](https://www.technologyreview.com/s/612501/inside-the-world-of-ai-that-forges-beautiful-art-and-terrifying-deepfakes/) - A 2018 overview of GAN and latests progress in the field of generative networks. _(`GAN`)_
  * [AI software can dream up an entire digital world from a simple sketch](https://www.technologyreview.com/s/612503/ai-software-can-dream-up-an-entire-digital-world-from-a-simple-sketch/) - A photorealistic 3D engine renderer made out of GAN. _(`GAN`)_
  * [A Style-Based Generator Architecture for Generative Adversarial Networks](https://arxiv.org/pdf/1812.04948.pdf) - Here we are, on December 2018 we discovered than a computer can generate images that we can definitely take for real ones. [summary](https://www.technologyreview.com/s/612612/these-incredibly-real-fake-faces-show-how-algorithms-can-now-mess-with-us/).
* Object generation
  * [Visual Object Networks: Image Generation with Disentangled 3D Representation](http://papers.nips.cc/paper/7297-visual-object-networks-image-generation-with-disentangled-3d-representations.pdf) - How a set of specialized networks learn to generate 3D objects. _(`GAN`, `3D`)_
  * [This is the most complex generative design ever made](https://www.fastcompany.com/90269399/this-is-the-most-complex-generative-design-ever-made) - Purely inspirational, no implementation design, still further details are accessible [here](https://www.autodesk.com/solutions/generative-design).

#### Understanding deep learning

Neural networks are known as black boxes, famously incomprehensible. Be careful whoever tells you he can surely explain how a deep learning model takes a decision. There are several tries to understand them, to explain how they are taking decisions, and even to debug them.

* [manifold](https://eng.uber.com/manifold/) - A platform from uber that promises ease of debugging, not publicly shared, not available for test, pretty, and a lot of ideas still.
* [comet.ml](https://comet.ml) - An online platform compatible with any Machine Learning framework that aggregate online stats and enable model comparison.
* [A New Approach to Understanding How Machines Think](https://www.quantamagazine.org/been-kim-is-building-a-translator-for-artificial-intelligence-20190110) - An interview of Been Kim from Google Brain for the introduction of “Testing with Concept Activation Vectors” ([TCAV](https://arxiv.org/pdf/1711.11279.pdf))
* [Machine Learning for Kids](https://machinelearningforkids.co.uk/) - If you want my mind, valuable not only for kids 😅
* [A neural network can learn to organize the world it sees into concepts—just like we do](https://www.technologyreview.com/s/612746/a-neural-network-can-learn-to-organize-the-world-it-sees-into-conceptsjust-like-we-do) - In this [paper](https://arxiv.org/pdf/1811.10597.pdf), GAN are examined under a microscope, it is a major leap forward into comprehension of GANs.
* [The Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/) - A reproducible paper that combines different technics in order to better understand networks.
* [Four Experiments in Handwriting with a Neural Network](https://distill.pub/2016/handwriting/) - Interactive experiments to understand network based on your handwriting inputs

#### Games

* [Starcraft AI competition](http://www.cs.mun.ca/~dchurchill/starcraftaicomp/2018/aiide/) - The state of the Starcraft competition. Samsung 1st, Facebook 2nd.
* [Mortal Kombat](https://blog.mgechev.com/2018/10/20/transfer-learning-tensorflow-js-data-augmentation-mobile-net/) - A `Tensorflow.js` project that allows you to play Mortal Kombat with your webcam.

#### Experiments & Art

* Music:
  * [Semi-Conductor](https://experiments.withgoogle.com/semi-conductor) - A Google AI experiment that allow one to conduct an orchestra from the browser
* Painting:
  * [amalGAN](http://areben.com/project/amalgan/) - [Alexander Reben](http://areben.com/cv/) used brain waves, GAN network and side supportive networks to generate a set of visually unusual paintings that are physically reproduced in a Chinese town: a human-machine global collaboration.
* Spotting AI-generated faces.
  * [nikola MIT experiment](http://nikola.mit.edu/experiment) - An online test that asks you to spot Generated faces with [NVIDIA's Progressive GAN](https://research.nvidia.com/publication/2017-10_Progressive-Growing-of). I wasn't 100% correct. 😅
  * [How to recognize fake AI-generated images](https://medium.com/@kcimc/how-to-recognize-fake-ai-generated-images-4d1f6f9a2842) - An extensive look into AI-generated images that will train yourself to spot fake images.
* Future is brilliant
  * [Neural Ordinary Differential Equations](https://arxiv.org/abs/1806.07366) - Explorative new family of neural network that "parameterizes the derivative of the hidden state using a neural network".
  * [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261) - Advocacy for combinatory between "hand-engineering" and "end-to-end" learning in order to overcome current full deep learning approachs.

#### Data

* [Adding Diversity to Images with Open Images Extended](https://ai.googleblog.com/2018/12/adding-diversity-to-images-with-open.html) _(`diversity`)_
* [Open Images Dataset V4](https://storage.googleapis.com/openimages/web/index.html)
* [Kaggle Datasets](https://www.kaggle.com/datasets)
* [BigQuery Datasets](https://cloud.google.com/bigquery/public-data/)
* [AWS OpenData](https://aws.amazon.com/opendata/)

#### Performance and hardware

* [A full hardware guide to Deep Learning](http://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) - If you want to build your own local hardware for training, this is a must read.
* [Best Deals in Deep Learning Cloud Providers](https://towardsdatascience.com/maximize-your-gpu-dollars-a9133f4e546a) - Where does it more effective to train your models. AWS is the most expensive.

#### Ethics

* [Research priorities for robust and beneficial Artificial Intelligence](https://futureoflife.org/ai-open-letter/) - The first round of people who expressed worries in the current research state of AI. It should be directed toward beneficial outcomes: "our AI systems must do what we want them to do".
* [China’s top AI scientist drives development of ethical guidelines](https://www.scmp.com/news/china/science/article/2181573/chinas-top-ai-scientist-drives-development-ethical-guidelines) - Yes it is time for the world to align itself on where it wants to go
* [Thinking inside the box: using and controlling an Oracle AI](https://link.springer.com/article/10.1007/s11023-012-9282-2) - Controlling AI has been a problem for a while even before the rise of deep learning. In this paper, you'll discover that a particular topic can raise a lot of questions, even if it seems simple at first: here controlling an Oracle AI that doesn't act in the world except by answering questions.
* [Google is trying to remove gender bias from its translation services](https://www.fastcompany.com/90278118/google-is-trying-to-remove-gender-bias-from-its-translation-services) - Gender bias is one of the problem in engineering, mostly only male all around. It is so easy to implement those bias and transmit them to the machine.

#### Sagemaker

[`sagemaker`](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is quickly becoming a state of the art for machine learning project. It assembles under this sole name a lot of capabilities that would accelerate and standardize any launching project involving machine learning of any sort. From [collaboration](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-notebooks-now-support-git-integration-for-increased-persistence-collaboration-and-reproducibility/) to [continuous deployment of model](https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions/), through [ground truth generation](https://aws.amazon.com/blogs/aws/amazon-sagemaker-ground-truth-build-highly-accurate-datasets-and-reduce-labeling-costs-by-up-to-70/) `sagemaker` provides all necessary tools for most of the use cases.

The initial version of `sagemaker` has been released on [Nov 29, 2017](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-amazon-sagemaker/). As we were working on machine learning projects applied to production in early 2016, we needed to figured out by ourselves and our small team how to build, train and deploy our custom models. Spending a consequent amount of time in setting the instances, installing latest version - available at that time - of `cuda` and `tensorflow` and connecting the dots in the process.

If I would start something new today, `sagemaker` would be my primary target as a CTO, helping my future team to focus on the value added, not the infrastructure and process on which everyone - starting with AWS - is working on.

A `sagemaker` workflow for continuous deployment (© [AWS](https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions/)):

<img src="./resources/machine-learning/sagemaker/sagemaker-continuous-deployment.gif" height="400" alt="Sagemaker Continuous deployment - © https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions/">

{::ignore rule="MD033" relative_line="-2"}

`sagemaker` use cases demonstration:

* [Analyzing live video](https://aws.amazon.com/blogs/machine-learning/analyze-live-video-at-scale-in-real-time-using-amazon-kinesis-video-streams-and-amazon-sagemaker/)
* [Classifying high-resolution chest x-ray medical images with Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/classifying-high-resolution-chest-x-ray-medical-images-with-amazon-sagemaker/)

other `sagemaker` key features:

* [Pipe mode](https://aws.amazon.com/blogs/machine-learning/accelerate-model-training-using-faster-pipe-mode-on-amazon-sagemaker/) - It allows to stream data directly from an `S3` bucket without the need to download the data on the machine. It leverages the [protobuf](https://developers.google.com/protocol-buffers/) to speedup streaming from S3 to the training instances.

#### Various

Going all directions:

* [Robust Website Fingerprinting Through the Cache Occupancy Channel](https://arxiv.org/pdf/1811.07153.pdf) - What if you can leverage machine learning and a Javascript security hole to track anyone browsing history?
* [Track the number of coffees consumed using AWS DeepLens](https://aws.amazon.com/blogs/machine-learning/track-the-number-of-coffees-consumed-using-aws-deeplens/) - How to build a coffee tracker in the open space with AWS deeplens.
* Energy management:
  * [EnergyVault](https://energyvault.ch/#operating-parameters) - The cleverest idea ever regarding energy storage. Thinking out of the box is key when you are growing a startup. Here is the perfect example.

#### Setting a machine learning project

Creating an enterprise grade machine learning project is complicated, a lot of steps are necessary. As of today, you have a lot of choices to set your projects right. Depending on your team size, you might even willing to reinvent the wheel suffering from the ["Not Invented Here"](https://en.wikipedia.org/wiki/Not_invented_here) syndrome. The good news is there is a lot to learn from the already maturing industry. Here are some source to read before jumping straight ahead!

* [How to build a machine learning team when you are not google or facebook](https://www.wandb.com/blog/how-to-build-a-machine-learning-team-when-you-are-not-google-or-facebook) - Pragmatism has always been at the heart of our strategy regarding our machine learning projects. This article formalize best practice that a good manager will discover himself executing a machine learning project. One thing for sure, as of today, "it’s more efficient to teach a engineers machine learning than to teach machine learning practitioners how to be good engineers." And, with the right project and the rock solid computer scientist you can kick-start a machine learning in a small team.
* [IBM Machine Learning Maturity Model](https://arxiv.org/pdf/1811.04871.pdf) - Presents a set of best practices to implement when a company wants to deploy machine learning at scale and in a friendly fashion with enterprise landscape. Many of them might be complicated to achieve, anyhow, it will highlight any shortcomings in your projects or potential area of focus.
* Services that might help you:
  * [comet](https://comet.ml)
  * [DVC](https://dvc.org/doc/dvc-philosophy/core-features)

My synthesis: also look at The-Roadmap-to-Machine-Learning-Maturity-v1.pdf

Conclusions:

* Don't reinvent the wheel, just like all other computer science project!
* Don't be afraid to get your hands dirty, if you are working on cutting edge projects, your data won't be annotated. Obviously you can outsource annotation, but one need to understand what it means.
* Be humble, the research is going really blasting [fast](https://www.technologyreview.com/s/612582/data-that-illuminates-the-ai-boom/).
* Accept failure, and be patient. Only one thing is sure, in any machine learning project you'll met failure. Reaching success might be a long way...

### Blockchain

Yes, during the last years I spent some time documenting myself on blockchain and its ecosystem. It is an emerging yet powerful new technology that deserves any tech friendly people deserve some attention or involvement into it.

### Data science

* Dataviz:
  * [Edward Tufte’s The Visual Display of Quantitative Information](https://amzn.to/2ROaWUl) - The first book to read when you are entering the world of data visualization.
  * [3rd Wave Data Visualization](https://towardsdatascience.com/3rd-wave-data-visualization-824c5dc84967) - Elijah Meeks author of [semiotic](https://github.com/emeeks/semiotic) - A react + d3.js library, a famous combo I experienced with success and pleasure - points to problems into the current landscape of data visualization.
  * Beware of the answers you'll find and always skeptic first. That a service you owe yourself:
    * [Curve Fitting](https://xkcd.com/2048/) - A drawing worths a thousand words.
    * [Importance of Skepticism in Data Science](https://jhu-advdatasci.github.io/2018/lectures/12-being-skeptical.html) - This long code detailed lecture aims at illustrating the bias that you might follow when you are interpreting data you have manipulated. _(`R`)_
* Data management:
  * [DVC](https://dvc.org/doc/dvc-philosophy/core-features) - A neat structured approach to the data science workflow management aiming to become a standard as git has become in the development workflow.

### Development

* Programming paradigms
  * [Goodbye, Object Oriented Programming](https://medium.com/@cscalfani/goodbye-object-oriented-programming-a59cda4c0e53) - That lecture helps to jolt away preconceived ideas that have been learned over the years OR simply point usual mistakes. Take a look. _(`OO`)_
* Code quality
  * [Code climate](https://codeclimate.com/quality/) - A lot of tools in the industry, give a try to this one.
* Tutorials
  * [GraphQL API with AWS and Use with React](https://scotch.io/tutorials/graphql-api-with-aws-and-use-with-react) - Setting a `graphql` API along with a react application on AWS and AWS Amplify.

#### Software design and principles

#### mono-repo vs multi-repo | microservices vs monolith

We have experienced both mono repo and multi repo along with microservices and monolith for years now. My conclusion regarding our context:

* It is hard to set a mono repository right,
* It is harder to manage hundreds of repository for several service right,
* You have to build or use tools dedicated to mono repository management, and in particular for continuous integration,
* A monorepo still is way more efficient regarding deployment, coherence, bug tracking, cleaning and "community management",
* Microservices are way more efficient in term of flexibility, possible innovation and creativity, overall velocity,
* The microservices set in a monorepo combination was perfect for our team, size and project.
* Continuous delivery setup is a journey. Keep the focus and priority: often it is delivering reliably new features to your customers.

Several sources, so you can have a better idea of the debate:

* [Segment's transition back to a monorepo](https://changelog.com/podcast/312) and its original [blog post](https://segment.com/blog/goodbye-microservices/)
* [Confessions of Continuous Delivery Experts: From microservices back to monolith](https://www.gocd.org/2017/12/06/confessions-continuous-delivery-experts-snapci-microservices-monolith/) - Lesson learnt moving from microservice to monolith.

For the same context that were ours, what I might consent is to split application tiers into different repositories (example: front-end in one repository, back-end in another), that's all!

#### `vscode`

[`vscode`](https://code.visualstudio.com/) replaces the long 1st in my heart [`Sublime`](https://www.sublimetext.com/): it has proven to turn myself into a better "prototyper", data extractor and developer in the past year. It is reliable, able to handle large files, has a small memory footprint and perfectly extendable.

My mandatory extensions:

* [Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) - You might spend a bunch of time configuring `vscode` (extensions, settings and keybindings). When you are changing your computer, you are happy being able to grasp all that configuration automatically. One extension to rule them all!.

Further awesomeness:

* [awesome-vscode](https://github.com/viatsko/awesome-vscode) - a extensive list of interesting resources for `vscode`.

#### Languages and technologies

##### `Javascript`

* Command line
  * [ervy](https://github.com/chunqiuyiyu/ervy) - Bringing charts to the terminal, because every project needs a command line and dataviz is fun!

##### `Python`

* Performances
  * [From Python to Numpy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/) - An online book that teaches how to migrate from standard `Python` to `Numpy` through vectorization.
  * [7 Strategies for Optimizing Numerical Code](https://speakerdeck.com/jakevdp/seven-strategies-for-optimizing-numerical-code) - An overview of 7 technics to enhance `Python` performances.
  * [Python Data Visualization landscape](https://www.anaconda.com/blog/developer-blog/python-data-visualization-2018-why-so-many-libraries) - An heavy loaded landscape of data visualization tools in python ready for convergence.
  * [plot.ly](https://towardsdatascience.com/the-next-level-of-data-visualization-in-python-dd6e99039d5e) - Extensive zoom and discovery of `plotly` for `Python`.

##### `Ruby`

* Command line:

##### `Bash`

* Command line:
  * [bash-boilerplate](https://github.com/alphabetum/bash-boilerplate) - Name speaks for itself. Even today, bash might be the best answer to a simple clear problem that needs a repetitive way to being reproduced. This repository kick-starts it even further.
  * [bash-oo-framework](https://github.com/niieani/bash-oo-framework) - If `bash-boilerplate` is not enough you should find everything you need here.

##### AWS

* Lambda Optimization:
  * [Lambda optimization tip – enable HTTP keep-alive](https://theburningmonk.com/2019/02/lambda-optimization-tip-enable-http-keep-alive/) - Drastically reduce average execution time of each lambda function working with a DB

### Growing a company

* [Can you bootstrap a startup on the side?](https://justinjackson.ca/bootstrap-side-project) - Build you own path based on your experience, will and target
* [This is hard](https://justinjackson.ca/hard) - Never forget that stopping your project is the main reason for failure
* Management
  * Working remotely
    * [All-remote workforce](https://www.businessinsider.fr/us/gitlab-zapier-remote-emsisoft-invision-workforce-2019-1) - A series of pros and cons from all-remote companies like Zapier and GitLab. Some ideas to gather, some lessons to learn or confirm you're not alone. Some are applicable to global companies. World is changing, cost of living is increasing in a lot of places, talents are all around the world. One thing for sure, you will see more and more all-remote rather than the contrary.
  * [Most leaders don't even know the game they are in](https://www.youtube.com/watch?v=RyTQ5-SQYTo)
  * [Simon Sinek on Millennials in the Workplace](https://www.youtube.com/watch?v=hER0Qp6QJNU) - A shorter version focusing on Millennials.

### Productivity tools

The following are my day to day productivity tools:

* [Grammarly](https://app.grammarly.com) - An awesome english spell checker that I use everyday. They also have a keyboard for iOS. But, they are missing an API to create 3rd parties app, like a vscode spell checker for `markdown` 😑
* [Todoist](https://todoist.com) - Simplest yet all features included todo manager
* [Evernote](https://evernote.com) - Powerful note taker that has neat web clipping, organization and sharing. I miss a bunch of features, like auto tagging of existing notes, archiving, smart lists, etc. But I wasn't able to find a really better alternative yet. I use it for all important article I want to preserve and for my projects
* [Apple notes](https://www.icloud.com/) - For rapid personal note taking for meetings, interviews, etc.
* [github](https://www.github.com) - Useful for your personal [CV](https://github.com/HerveNivon/CV) generation or important [note sharing](./) ☺️.

### UX/UI

### Various tools

* Command line enhancements
  * [graphcurl](https://github.com/hasura/graphqurl) - Turn your command line into a `curl` like tool for GraphQL, keeping the exploration taste of [graphiql](https://github.com/graphql/graphiql)
  * [`jq`](https://stedolan.github.io/jq/) - Must have tool for any modern devOps or serious people working with a `Terminal` 😄 _(`json`)_
  * [`rb`](https://github.com/thisredone/rb) - Extends your command line workflow with a fully loaded inline ruby interpreter. Just in case you are alergic to `awk` and `sed` _(`Ruby`)_
  * [`terminalizer`](https://github.com/faressoft/terminalizer) - A way to record your `Terminal` and create gif images.
  * [`tldr`](https://github.com/tldr-pages/tldr) - Ever wanted to get just what you need instead of verbose man pages?
  * [`q`](https://github.com/harelba/q) - Run SQL queries directly on CSV files.
  * [`up`](https://github.com/akavel/up) - Write pipe processing with instant live preview of command results.
* Docker
  * [`dive`](https://github.com/wagoodman/dive) - Have you ever wanted to look into your `Dockerimage` result layers. Here you are!
* Markdown
  * [`gh-md-toc`](https://github.com/ekalinin/github-markdown-toc.go) - Generate table of content from a `.md` file.
* Security
  * [gitleaks](https://github.com/zricethezav/gitleaks) - Waiting for github next move in the security landscape, here is a way for you to scan code source for unencrypted secrets. 👮‍♂️
* Static web sites (Wordpress certainly not is the best answer)
  * [Publii](https://opencollective.com/Publii) - Is an open source static site CMS management tool
  * [Gatsby.js](https://www.gatsbyjs.org) - Is a library that enables static site generation from react

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)