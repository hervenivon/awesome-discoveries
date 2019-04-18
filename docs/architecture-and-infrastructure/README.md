---
description: 'Architecturing an information system and deploying its supporting infrastructure will set its backbone for a while. Doing it right is crucial.'
---

# Architecture & Infrastructure

> ‟Infrastructure describes the actual set of components that make up a system, while architecture describes the design of the components and their relationships. In a nutshell, a system is built on an infrastructure that has a particular architecture.” - [MooseBoys](https://stackoverflow.com/users/2726892/mooseboys)

Architecturing an information system and deploying its supporting infrastructure will set its backbone for a while. Doing it right is crucial.

Modern infrastructures, and in particular public cloud providers have paved the way to better-architectured information system. It is easier than ever to do it right.

Infrastructure as code has changed the development lifecycle changing forever project scale involving infrastructure deployment: from month or years to weeks.

* [CAP Theorem](https://www.itechart.com/blog/all-you-didnt-know-about-cap-theorem) - The CAP theorem extensive description - and its drawbacks. The CAP (Consistency, Availability, Partition-Tolerance) theorem helps selecting the best suited database solution for a particular problem. In this article, you will also discover its limits.
* AWS
  * [AWS Blog](https://aws.amazon.com/blogs/aws/) - If you want to be amazed by the innovation pace of AWS, be sure to subscribe to their blog, in addition to the day to day announcements you also get hands on blog post and a lot of inspiration.
* Cloud native
  * [Cloud Native Computing Foundation](https://www.cncf.io/) - The entry point to an open source journey in the cloud computing
* Tools for local development
  * [minio](https://min.io/product) - A distributed object storage server that mimic the "de facto standard API for object storage", named AWS S3.
  * [localstack](https://github.com/localstack/localstack) - The folks aren't really responsive, nor their enterprise offer seems to conclude in one way or another, but there is a lot of value and a lot to learn from that project.
* API design
  * [REST is the new SOAP](https://medium.freecodecamp.org/rest-is-the-new-soap-97ff6c09896d) - An article with a counter-current point of view that emphasizes every negative aspects of `REST`.
* Tools:
  * [Cloudcraft](https://cloudcraft.co/) - Isometric 3D drawing of your AWS infrastructure (to be or the actual one). Will help you document automatically your cloud infrastructure and to advertise it.
  * [Cloudockit](https://www.cloudockit.com/) - Same promise
* [Desired vs Deployed architecture](https://web.archive.org/web/20190327172748/https://twitter.com/changelog/status/839952960520138752)
* [BFF](https://blog.octo.com/les-indispensables-dun-projet-frontend-un-backend-for-frontend-une-api-sur-mesure/) - Backend For Frontend

<img src="https://pbs.twimg.com/media/C6gcqNJU8AAjOaK.jpg" alt="Desired vs Deployed architecture"/>

* Return of experience:
  * [Building Spotify’s New Web Player](https://labs.spotify.com/2019/03/25/building-spotifys-new-web-player/) - React + Redux migration.

## Serverless

Serverless is an infrastructure model in which the cloud provider handles every aspects of the infrastructure while the end user only provides the code to execute.

It doesn't mean that there is no server, it means than the server related activities virtualization, os and application activities are transparent for the end user. The provider dynamically manages the allocation of machines resources, the underlying infrastructure maintenance, and any OS patching. The code is typically run inside stateless containers that can be triggered by a variety of events (http requests, database events, queuing services, monitoring alerts, file uploads, schedulers, etc.)

Pricing is based on the actual amount of resources consumed by an application, rather than on pre-purchased units of capacity.

Serverless is sometimes referred to as “Functions as a Service” or “FaaS” because the end user only needs to send code functions, nothing else.

Serverless logic has been at the heart of my strategy at Redbird then Airware. With this model we have been able to focus all our resources on creating new value for our customers while our cloud provider was handling everything else.

There are different school to serverless, with a caricature we can split them into two categories, the cloud agnostic gurus and the opportunists.

I was part of the opportunists. As an early stage company I didn't want us to spend a cent in devops and infrastructure management. Why setting us a kubernetes cluster while we were able to use lambdas instead? Why setting our own database in a cluster while dynamo was here? Why setting us a custom HTTP gateway or building our own workflow engine? As a results, we ended with a fully scalable solution built out entirely on top of serverless services from AWS. All our man power directed into value added project that no one else were doing.

To start:

* [Serverless Stack](https://serverless-stack.com/) - A comprehensive guide to build your first serverless application
* [Serverless GraphQL](https://www.youtube.com/watch?reload=9&v=lnOIcKibKzc) - A 2016 speak by Jared Short that explains how to build a Serverless GraphQL on Lambda - before AWS released [AppSync](https://aws.amazon.com/appsync/). This is outdated but gives you a good taste of the serverless spirit

Testimonials:

* [The Serverless Start-Up - Down With Servers!](http://highscalability.com/blog/2015/12/7/the-serverless-start-up-down-with-servers.html) - A detailed return of experience on building a new adventure on top of API Gateway, Lambda, DynamoDB, S3 and Cloudfront ONLY: "The Virtues of Constraint". The no server startup!
* [Serverless Architecture and Box Platform](https://blog.box.com/blog/serverless-architecture-and-box-platform) - A testimonial from Box that illustrates a serverless authentication workflow.


### Controversy

The biggest concern that raises when you think about the serverless idea and you start implementing your application on top of cloud providers services is the vendor locking you are entering in. You are becoming wholly dependent on your cloud provider. This concern was the main argument for a potential full rewrite of Redbird application when Airware acquired it fall 2016 - (TLDR, we never did it.)

As a CTO, I carefully weighted and chose to empower the serverless paradigm over being cloud agnostic. I often had to justify that decision which happened to appear as a wrong choice for some of my interlocutors. But the equation is easy to solve: when you want to create as much value as you can, you must focus your energy and resource on building that value.  When the serverless paradigm supports that vision and accelerates the value creation, this is a no-brainer.

Embracing the serverless idea will save you time, resources and let you focus on what makes your business and application unique.

There are other controversies:

> While AWS continues its [Mr. Softy](https://en.wikipedia.org/wiki/Microsoft) strategy of [extend, embrace and extinguish](https://en.wikipedia.org/wiki/Embrace,_extend,_and_extinguish) with Lambda, Google is doubling down on its Kubernetes masterstroke with the upcoming “Knative.” - Abraham Ingersoll

Or the fact that Amazon Web Services [doesn't support the open source community](https://techcrunch.com/2019/01/09/aws-gives-open-source-the-middle-finger) while other [do](https://techcrunch.com/2019/04/09/google-gives-aws-the-open-source-middle-finger), but that is an entire other topic.

### Tools

* [Epsagon](https://epsagon.com/) - Observability is as of today the biggest challenge in serverless infrastructure - even with latest AWS enhancements on Cloudwatch, at least allowing textual search across your logs. Epsagon provides an observability SaaS board which creates - among other features - an execution map of all your connected services on a per API call basis. Tremendously useful.
* [Seed](https://seed.run/) - A solution that industrializes in a few clicks your serverless deployments. Frow manual command line deployment to production ready deployment board in minutes, literally.

### Various

* [Serverless on kubernetes](https://gravitational.com/blog/serverless-on-kubernetes/) - The concept seems strange to me in the sense it still forces you to handle the kubernetes cluster. To my mind, the real power of serverless resides in the infrastructure layer vanishment.
* [Serverless for data scientists](https://mike.place/talks/serverless/) - A [talk](https://www.youtube.com/watch?v=9PR2-ogB5qM) about what makes serverless paradigm, and function as service a good tool for data scientist. This talk comes with good examples, and neat logic.
* [Occupy the Cloud: Distributed Computing for the 99%](https://arxiv.org/abs/1702.04024) - A demonstration to achieve teraflops computing capability with AWS Lambda and [Pywren](http://pywren.io/).

## Data protection

Any SaaS business leads to customer data management. And, with customer data management comes responsibilities.

Like mentioned in the [Growing a company](./growing-a-company) section, Security should be a top priority for any SaaS company. It means protecting the data against intrusion, copy, and misappropriation, but is also means preserving the data.

A [reddit discussion](https://www.reddit.com/r/technology/comments/b2381s/myspace_lost_all_music_uploaded_from_2003_to_2015/) highlights the MySpace case: all music uploaded from 2003 to 2015 is lost due to a "server migration". Slightly confirmed on the Myspace [homepage](https://myspace.com).

> As a result of a server migration project, any photos, videos, and audio files you uploaded more than three years ago may no longer be available on or from Myspace. We apologize for the inconvenience. If you would like more information, please contact our Data Protection Officer at DPO@myspace.com.

<img src="./resources/myspace-case.png" width="300px" alt="Myspace homepage as of 27th of March 2019"/>

Handling data is hard, in particular when you deal yourselves with backups. Cloud providers are here to help, in particular for emerging business. They help you achieve a higher level of service quality at no cost. You don't have to deal with the overhead of such data management; you let them do and concentrate on your business. When you achieve success, you might go one step further and implement extra physical backups. What is stored on the Internet may disappear, and we never know, cloud providers might not remain forever. 😅
