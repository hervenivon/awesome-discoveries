# Artificial Intelligence

If you are new to Artificial Intelligence and machine learning, there is one place to go: the [machine learning glossary](https://developers.google.com/machine-learning/glossary) from the Google developers documentation.

For the complete bibliography, please look at the [bibliography](bibliography.tsv) file.

## Embedding

* [FaceNet: A Unified Embedding for Face Recognition and Clustering](https://arxiv.org/abs/1503.03832) - A solution which transforms an image into a compact Euclidean space allowing to enhance Face Recognition. [implementation](https://github.com/davidsandberg/facenet) _(`Embedding`, `image2vec`, `Tensorflow`)_
* [Grasp2Vec: Learning Object Representations from Self-Supervised Grasping](https://arxiv.org/abs/1811.06964) - Embedding used in reinforcement learning to represent reality through physical world robot grasping. [Google article](https://ai.googleblog.com/2018/12/grasp2vec-learning-object.html) _(`Embedding`, `image2vec`, `RL`)_

## Compression, enhancement

* [Learned Video Compression](https://arxiv.org/abs/1811.06981) - A traditional codec architecture where elements are replaced by Machine Learning ones. Results: the new codec outperforms all existing video codecs.

## Natural Language Processing and voice recognition

* Assisted writings
  * ["I want to live"](https://youtu.be/BhKw71AeOg4) - A 60 second clip entirely scripted from an AI studying 15 years of worth of award-winning ads.
  * [Bertie the Forbes' CMS](https://digiday.com/media/forbes-built-a-robot-to-pre-write-articles-for-its-contributors/) - Forbes [announced](https://www.forbes.com/sites/forbesproductgroup/2018/07/11/entering-the-next-century-with-a-new-forbes-experience/#5e9b28803bf4) its new AI powered CMS (Content Management System) where AI helps and support content creator from image selection to draft article writings.
* [Accurate Online Speaker Diarization with supervised learning](https://ai.googleblog.com/2018/11/accurate-online-speaker-diarization.html) - Detect interlaced speakers in a speech. But beware, code is not the original and you cannot access data. _(`PyTorch`, `Embedding`)_

## Semantic segmentation

Semantic segmentation is the practice of categorizing an image at the pixel level. i.e., semantic segmentation assigns a class to each pixel in an image. Semantic segmentation was at the heart of our core products at Redbird. There are a lot activities around that topic where state of the art is still not as accurate as human. I have written a [medium post](https://medium.com/@hervenivon/crafting-the-future-was-just-the-beginning-herve-nivon-3b7312a73184) where you will find further information regarding our projects.

Here are the most relevant findings we leverage for our project and some more recent ones that can enhance it:

* [Auto-DeepLab: Hierarchical Neural Architecture Search for Semantic Image Segmentation](https://arxiv.org/abs/1901.02985) - The next DeepLab generation which was already the state of the art in this field.
* [Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics](https://arxiv.org/abs/1705.07115) - Multi-task learning for segmentation and instance segmentation with a multi-task loss.
* [Panoptic Feature Pyramid Networks](https://arxiv.org/abs/1901.02446) - Unified architecture for multi task segmentation and instance segmentation.

## Data annotation

* [List of manual image annotation tools](https://en.wikipedia.org/wiki/List_of_manual_image_annotation_tools) - The list of annotation tools is long, unfortunately the Wikipedia rule enforce certain criteria I think are not smooth enough to enable tool discovery in fast pace changing environments. In that case, please take a look at the [talk](https://en.wikipedia.org/wiki/Talk:List_of_manual_image_annotation_tools) page of this article, there is pletoria of tools to discover here.
* Polygon-RNN:
  * [Efficient Interactive Annotation of Segmentation Datasets with Polygon-RNN++](https://www.youtube.com/watch?v=evGqMnL4P3E)
  * [Demo](http://www.cs.toronto.edu/polyrnn/)

Services:

* [supervise.ly](supervise.ly) - Is a an online service that enable automatic annotation of data. Fron the tens I tested it is my current favorite.
* [Alegion](https://alegion.com) - Annotation service that deals with computer vision, NLP, and data cleansing. The service alleges to combine machine learning and Human intelligence.

## Data Generation

* Face generation
  * [Inside the world of AI that forges beautiful art and terrifying deepfakes](https://www.technologyreview.com/s/612501/inside-the-world-of-ai-that-forges-beautiful-art-and-terrifying-deepfakes/) - A 2018 overview of GAN and latests progress in the field of generative networks.
  * [A Style-Based Generator Architecture for Generative Adversarial Networks](https://arxiv.org/abs/1812.04948) - Here we are, on December 2018 we discovered than a computer can generate images that we can definitely take for real ones. [summary](https://www.technologyreview.com/s/612612/these-incredibly-real-fake-faces-show-how-algorithms-can-now-mess-with-us/).
* Scenes generation
  * [AI software can dream up an entire digital world from a simple sketch](https://www.technologyreview.com/s/612503/ai-software-can-dream-up-an-entire-digital-world-from-a-simple-sketch/) - A photorealistic 3D engine renderer made out of GAN.
  * [GauGAN Turns Doodles into Stunning, Photorealistic Landscapes](https://blogs.nvidia.com/blog/2019/03/18/gaugan-photorealistic-landscapes-nvidia-research/) - This NVIDIA last sketch to photo GAN network based application - named GauGAN - results are unbelievable. [repository](https://github.com/NVlabs/SPADE), [paper](https://arxiv.org/abs/1903.07291)

<img src="./resources/gaugan.gif" alt="animation of GauGan in action">

* Object generation
  * [Visual Object Networks: Image Generation with Disentangled 3D Representation](http://papers.nips.cc/paper/7297-visual-object-networks-image-generation-with-disentangled-3d-representations.pdf) - How a set of specialized networks learn to generate 3D objects.
  * [This is the most complex generative design ever made](https://www.fastcompany.com/90269399/this-is-the-most-complex-generative-design-ever-made) - Purely inspirational, no implementation design, still further details are accessible [here](https://www.autodesk.com/solutions/generative-design).

## Understanding and interpreting the black box

Neural networks are known as black boxes, famously incomprehensible. Be careful whoever tells you he can surely explain how a deep learning model takes a decision. There are several tries to understand them, to explain how they are taking decisions, and even to debug them.

* [manifold](https://eng.uber.com/manifold/) - A platform from uber that promises ease of debugging, not publicly shared, not available for test, pretty, and a lot of ideas still.
* [comet.ml](https://comet.ml) - An online platform compatible with any Machine Learning framework that aggregate online stats and enable model comparison.
* [A New Approach to Understanding How Machines Think](https://www.quantamagazine.org/been-kim-is-building-a-translator-for-artificial-intelligence-20190110) - An interview of Been Kim from Google Brain for the introduction of “Testing with Concept Activation Vectors” [TCAV](https://arxiv.org/abs/1711.11279)
* [Machine Learning for Kids](https://machinelearningforkids.co.uk/) - If you want my mind, it is valuable not only for kids 😅
* [A neural network can learn to organize the world it sees into concepts—just like we do](https://www.technologyreview.com/s/612746/a-neural-network-can-learn-to-organize-the-world-it-sees-into-conceptsjust-like-we-do) - In this [paper](https://arxiv.org/abs/1811.10597), GAN are examined under a microscope, it is a major leap forward into comprehension of GANs.
* [The Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/) - A reproducible paper that combines different technics in order to better understand networks.
* [awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) - Another awesome list dedicated to machine learning interpretability, it wants itself to be an incomplete, imperfect blueprint for a more human-centered, lower-risk machine learning.
* [Four Experiments in Handwriting with a Neural Network](https://distill.pub/2016/handwriting/) - Interactive experiments to understand network based on your handwriting inputs
* [The Machine Learning Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf)

## Datasets

* [Adding Diversity to Images with Open Images Extended](https://ai.googleblog.com/2018/12/adding-diversity-to-images-with-open.html) _(`diversity`)_
* [Open Images Dataset V4](https://storage.googleapis.com/openimages/web/index.html)
* [Kaggle Datasets](https://www.kaggle.com/datasets)
* [BigQuery Datasets](https://cloud.google.com/bigquery/public-data/)
* [AWS OpenData](https://aws.amazon.com/opendata/)

## Performance and hardware

* [A full hardware guide to Deep Learning](http://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) - If you want to build your own local hardware for training, this is a must read.
* [Best Deals in Deep Learning Cloud Providers](https://towardsdatascience.com/maximize-your-gpu-dollars-a9133f4e546a) - Where does it more effective to train your models. AWS is the most expensive.

## Ethics

* [Research priorities for robust and beneficial Artificial Intelligence](https://futureoflife.org/ai-open-letter/) - The first round of people who expressed worries in the current research state of AI. It should be directed toward beneficial outcomes: "our AI systems must do what we want them to do".
* [China’s top AI scientist drives development of ethical guidelines](https://www.scmp.com/news/china/science/article/2181573/chinas-top-ai-scientist-drives-development-ethical-guidelines) - Yes it is time for the world to align itself on where it wants to go
* [Thinking inside the box: using and controlling an Oracle AI](https://link.springer.com/article/10.1007/s11023-012-9282-2) - Controlling AI has been a problem for a while even before the rise of deep learning. In this paper, you'll discover that a particular topic can raise a lot of questions, even if it seems simple at first: here controlling an Oracle AI that doesn't act in the world except by answering questions.
* [Google is trying to remove gender bias from its translation services](https://www.fastcompany.com/90278118/google-is-trying-to-remove-gender-bias-from-its-translation-services) - Gender bias is one of the problem in engineering, mostly only male all around. It is so easy to implement those bias and transmit them to the machine.
* [GPT-2 blog post announcement](https://openai.com/blog/better-language-models/) - OpenAI released a blog post along their paper [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) explaining why they won't share reproducibility parameters (regarding data and hyperparameters notably). The GPT-2 performances are unbelievable and in the absence of clear ethics in the artificial intelligence field I can't agree more at that time. Nevertheless, I'm utterly frustrated. We need to do something about the social implications of artificial intelligence. In the [OpenAI’s GPT-2: the model, the hype, and the controversy](https://towardsdatascience.com/openais-gpt-2-the-model-the-hype-and-the-controversy-1109f4bfd5e8) blog post, the idea of a ‘safety checklist’; similarly to the recent ‘[reproducibility checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf)’ arises. Why not?!
* [Counter strike against GPT-2](http://gltr.io/) - Perpetuating the long tradition of cat and mouse play, a new AI developed by researchers at MIT, IBM’s Watson A.I. Lab and Harvard University has been built to detect text generated by AI and therefore providing a tool to fight fake news! It comes with a nice [demo](http://gltr.io/dist/index.html)
* [AI Safety Needs Social Scientists](https://distill.pub/2019/safety-needs-social-scientists/) - An extensive explanation towards the Social Scientists requirement explanation.

## Sagemaker

[`sagemaker`](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is quickly becoming a state of the art for machine learning project. It assembles under this sole name a lot of capabilities that would accelerate and standardize any launching project involving machine learning of any sort. From [collaboration](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-notebooks-now-support-git-integration-for-increased-persistence-collaboration-and-reproducibility) to [continuous deployment of model](https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions), through [ground truth generation](https://aws.amazon.com/blogs/aws/amazon-sagemaker-ground-truth-build-highly-accurate-datasets-and-reduce-labeling-costs-by-up-to-70) `sagemaker` provides all necessary tools for most of the use cases.

The initial version of `sagemaker` has been released on [Nov 29, 2017](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-amazon-sagemaker/). As we were working on machine learning projects applied to production in early 2016, we needed to figured out by ourselves and our small team how to build, train and deploy our custom models. Spending a consequent amount of time in setting the instances, installing latest version - available at that time - of `cuda` and `tensorflow` and connecting the dots in the process.

If I would start something new today, `sagemaker` would be my primary target as a CTO, helping my future team to focus on the value added, not the infrastructure and process on which everyone - starting with AWS - is working on.

A `sagemaker` workflow for continuous deployment © [AWS](https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions):

<img src="./resources/sagemaker-continuous-deployment.gif" height="400" alt="Sagemaker Continuous deployment - © https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions/">

`sagemaker` use cases demonstration:

* [Analyzing live video](https://aws.amazon.com/blogs/machine-learning/analyze-live-video-at-scale-in-real-time-using-amazon-kinesis-video-streams-and-amazon-sagemaker/)
* [Classifying high-resolution chest x-ray medical images with Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/classifying-high-resolution-chest-x-ray-medical-images-with-amazon-sagemaker/)

other `sagemaker` key features:

* [Pipe mode](https://aws.amazon.com/blogs/machine-learning/accelerate-model-training-using-faster-pipe-mode-on-amazon-sagemaker/) - It allows to stream data directly from an `S3` bucket without the need to download the data on the machine. It leverages the [protobuf](https://developers.google.com/protocol-buffers/) to speedup streaming from S3 to the training instances.

## Setting an artificial intelligence project

Executing an enterprise grade machine learning project is complicated, a lot of steps are necessary in a highly uncertain context. As of today, you have a lot of choices to set your projects right. Depending on your team size, you might even willing to reinvent the wheel suffering from the ["Not Invented Here"](https://en.wikipedia.org/wiki/Not_invented_here) syndrome. The good news is there is a lot to learn from the already maturing industry. Here are some source to read before jumping straight ahead!

* [How to build a machine learning team when you are not google or facebook](https://www.wandb.com/blog/how-to-build-a-machine-learning-team-when-you-are-not-google-or-facebook) - Pragmatism has always been at the heart of our strategy regarding our machine learning projects. This article formalize best practice that a good manager will discover himself executing a machine learning project. One thing for sure, as of today, "it’s more efficient to teach a engineers machine learning than to teach machine learning practitioners how to be good engineers." And, with the right project and the rock solid computer scientist you can kick-start a machine learning in a small team.
* Productionizing an artificial intelligence project, tracking its progress or solely being able to reproduce an experiment is a challenge. A traditional system is seen as deterministic, for a particular version of your code, you have specific behavior. You can upgrade your software or dependencies to a particular version to benefit some improvements or you can roll-back to a previous version of it if you face some unexpected issues. Infrastructure as code paradigm enables the same features for the underlying elements supporting your project. For years now, continuous delivery is a well-known concept, often applied in production. When it comes to artificial intelligence projects it is steadily way more tricky: how do you manage that so-called black box? The good news is that the black box can also be versioned. You can version an artificial intelligence project on [different axes](https://emilygorcenski.com/post/data-versioning): code, model, data schema, data values, and data annotations. There is not only one approach, and it can become highly complex. It depends on your project ambition, data variation, number of people involved, go-live frequencies, etc. You must find the most appropriate way for each project. In my experience, versioning models, associated code and data annotations have proven to be the bare minimum - and even it wasn't always sufficient to reproduce a particular experiment. Some tools or services might assist you in this mission:
  * [comet](https://comet.ml)
  * [DVC](https://dvc.org/doc/dvc-philosophy/core-features)
  * [MLflow](https://mlflow.org/)
* [IBM Machine Learning Maturity Model](https://arxiv.org/abs/1811.04871) - Presents a set of best practices to implement when a company wants to deploy machine learning at scale and in a friendly fashion with enterprise landscape. Many of them might be complicated to achieve, anyhow, it will highlight any shortcomings in your projects or potential area of focus.

My synthesis: also look at The-Roadmap-to-Machine-Learning-Maturity-v1.pdf

Conclusions:

* Don't reinvent the wheel, just like all other computer science project!
* Don't be afraid to get your hands dirty, if you are working on cutting edge projects, your data won't be annotated. Obviously you can outsource annotation, but one need to understand what it means.
* Be humble, the research is going really blasting [fast](https://www.technologyreview.com/s/612582/data-that-illuminates-the-ai-boom/).
* Accept failure, and be patient. Only one thing is sure, in any machine learning project you'll met failure. Reaching success might be a long way...

## Further inspiration

* [Robust Website Fingerprinting Through the Cache Occupancy Channel](https://arxiv.org/abs/1811.07153) - What if you can leverage machine learning and a Javascript security hole to track anyone browsing history?
* [Track the number of coffees consumed using AWS DeepLens](https://aws.amazon.com/blogs/machine-learning/track-the-number-of-coffees-consumed-using-aws-deeplens/) - How to build a coffee tracker in the open space with AWS deeplens.
* [Deep Learning State of the Art (2019) - MIT](https://www.youtube.com/watch?v=53YvP6gdD7U) - A lecture from [@lexfridman](https://twitter.com/lexfridman) on recent developments in deep learning. That is a very good overview of 2018 state of the art in research and applied deep learning.
* Energy management:
  * [EnergyVault](https://energyvault.ch/#operating-parameters) - The cleverest idea ever regarding energy storage. Thinking out of the box is key when you are growing a startup. Here is the perfect example.
* Online AI experiments:
  * [Iconary](https://iconary.allenai.org/) - Iconary from researchers at the Allen Institute for #AI is an online drawing and guessing game based on Pictionary. Its engine #AllenAI will blow your mind.
  * [AI Experiments](https://experiments.withgoogle.com/collection/ai) - Curated list of AI experiments from Google. Doodle guessing, AI assisted drawing, Music, etc.

As we are loosing most of the [nonverbal communications](https://en.wikipedia.org/wiki/Nonverbal_communication) in a large portion of our day to day modern human to human interactions, I've always been curious on how we could extend it with expressive enhancements that would explain much more than lengthy descriptions. "A picture worths a thousand words." Some attempts:

* [Dango](https://getdango.com/) - Is an application and API to propose relevant emojis and GIFs based on your text input in messaging. This unfortunately doesn't provide the code.
* [live-mood](http://devpost.com/software/live-mood-2b5arl) - A former team member worked on a twitch extension to continuously transcribe watchers mood on a stream.

### Medicine

* [Brain2Speech](https://www.sciencemag.org/news/2019/01/artificial-intelligence-turns-brain-activity-speech) - Experiment using AI to get our voice out of our head automatically. The promise to an accessible world for disable people.
* [Learning to Design RNA](https://arxiv.org/abs/1812.11951) - Reinforcement Learning used to design RNA sequence to test _(`RL`)_
* [Face2Gene](https://www.nature.com/articles/d41586-019-00027-x#ref-CR1) - From Professional crowdsourcing to real life medicine aid use case, the face2gene application that spot genetic disorders is a promise for future medicine.
* [Artificial Intelligence Can Detect Alzheimer’s Disease in Brain Scans Six Years Before a Diagnosis](https://www.ucsf.edu/news/2018/12/412946/artificial-intelligence-can-detect-alzheimers-disease-brain-scans-six-years) - It is not a question of time any more, it is already here.
* [Detection of patient mobilization activities in the ICU](https://www.nature.com/articles/s41746-019-0087-z) - How a deep learning based computer vision can help to monitor patient mobilization and to mitigate risk for post-intensive care syndrome and long-term functional impairment  in intensive care unit (ICU).

### Games

* [Starcraft AI competition](http://www.cs.mun.ca/~dchurchill/starcraftaicomp/2018/aiide/) - The state of the Starcraft competition. Samsung 1st, Facebook 2nd.
* [Mortal Kombat](https://blog.mgechev.com/2018/10/20/transfer-learning-tensorflow-js-data-augmentation-mobile-net/) - A `Tensorflow.js` project that allows you to play Mortal Kombat with your webcam.
* [TensorKart](https://www.kevinhughes.ca/blog/tensor-kart) - Game played with an Xbox became training data for an off the shelf model to train an agent playing MarioKart 64. Data are all around us!

### Experiments & Art

* Music:
  * [Semi-Conductor](https://experiments.withgoogle.com/semi-conductor) - A Google AI experiment that allow one to conduct an orchestra from the browser
* Painting:
  * [amalGAN](http://areben.com/project/amalgan/) - [Alexander Reben](http://areben.com/cv/) used brain waves, GAN network and side supportive networks to generate a set of visually unusual paintings that are physically reproduced in a Chinese town: a human-machine global collaboration.
* Spotting AI-generated faces:
  * [nikola MIT experiment](https://web.archive.org/web/20181210150931/http://nikola.mit.edu/experiment) - People at MIT had set an online test that asks you to spot generated faces with [NVIDIA's Progressive GAN](https://research.nvidia.com/publication/2017-10_Progressive-Growing-of). I tried it myself and wasn't 100% correct 😅. Some
  * [How to recognize fake AI-generated images](https://medium.com/@kcimc/how-to-recognize-fake-ai-generated-images-4d1f6f9a2842) - An extensive look into AI-generated images that will train yourself to spot fake images.
* Future is brilliant
  * [Neural Ordinary Differential Equations](https://arxiv.org/abs/1806.07366) - Explorative new family of neural network that "parameterizes the derivative of the hidden state using a neural network".
  * [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261) - Advocacy for combinatory between "hand-engineering" and "end-to-end" learning in order to overcome current full deep learning approachs.
  * [AICAN HG Contemporary February exhibit](http://www.hgcontemporary.com/exhibitions/faceless-portraits-transcending-time?view=slider#5) - Faceless Portrait #5 is Terminator as an art piece. Someone will see a [disturbed AI](https://www.fastcompany.com/90307889/these-eerie-portraits-were-painted-by-a-very-disturbed-ai)
