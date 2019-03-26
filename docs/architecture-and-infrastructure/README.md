---
description: 'Architecturing an information system and deploying its supporting infrastructure will set its backbone for a while. Doing it right is crucial'
---

# Architecture & Infrastructure

> ‟Infrastructure describes the actual set of components that make up a system, while architecture describes the design of the components and their relationships. In a nutshell, a system is built on an infrastructure that has a particular architecture.” - [MooseBoys](https://stackoverflow.com/users/2726892/mooseboys)

Architecturing an information system and deploying its supporting infrastructure will set its backbone for a while. Doing it right is crucial.

Modern infrastructures, and in particular public cloud providers have paved the way to better-architectured information system. It is easier than ever to do it right.

Infrastructure as code has changed the development lifecycle changing forever project scale involving infrastructure deployment: from month or years to weeks.

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
  * [minio](https://min.io/product) - A distributed object storage server that mimic the "de facto standard API for object storage", named AWS S3.
  * [localstack](https://github.com/localstack/localstack) - The folks aren't really responsive, nor their enterprise offer seems to conclude in one way or another, but there is a lot of value and a lot to learn from that project.
* API design
  * [REST is the new SOAP](https://medium.freecodecamp.org/rest-is-the-new-soap-97ff6c09896d) - An article with a counter-current point of view that emphasizes every negative aspects of `REST`.
* Tools:
  * [Cloudcraft](https://cloudcraft.co/) - Isometric 3D drawing of your AWS infrastructure (to be or the actual one). Will help you document automatically your cloud infrastructure and to advertise it.
  * [Cloudockit](https://www.cloudockit.com/) - Same promise
* [Desired vs Deployed architecture](https://twitter.com/changelog/status/839952960520138752)
* [BFF](https://blog.octo.com/les-indispensables-dun-projet-frontend-un-backend-for-frontend-une-api-sur-mesure/) - Backend For Frontend

## Serverless

Serverless is an infrastructure model in which the cloud provider handles every aspects of the infrastructure while the end user only provides the code to execute.

It doesn't mean that there is no server, it means than the server related activities virtualization, os and application activities are transparent for the end user. The provider dynamically manages the allocation of machines resources, the underlying infrastructure maintenance, and any OS patching. The code is typically run inside stateless containers that can be triggered by a variety of events (http requests, database events, queuing services, monitoring alerts, file uploads, schedulers, etc.)

Pricing is based on the actual amount of resources consumed by an application, rather than on pre-purchased units of capacity.

Serverless is sometimes referred to as “Functions as a Service” or “FaaS” because the end user only needs to send code functions, nothing else.

Serverless logic has been at the heart of my strategy at Redbird then Airware. With this model we have been able to focus all our resources on creating new value for our customers while our cloud provider was handling everything else.

There are different school to serverless, with a caricature we can split them into two categories, the cloud agnostic gurus and the opportunistics.

I was part of the opportunistics. As an early stage company I didn't want us to spend a cent in devops and infrastructure management. Why setting us a kubernetes cluster while we were able to use lambdas instead? Why setting our own database in a cluster while dynamo was here? Why setting us a custom HTTP gateway or building our own workflow engine? As a results, we ended with a fully scallable solution built out entirely on top of serverless services from AWS. All our man power directed into value added project that no one else were doing.

* [https://serverless-stack.com/](Serverless Stack) - A comprehensive guide to build your first serverless application

> While AWS continues its [Mr. Softy](https://en.wikipedia.org/wiki/Microsoft) strategy of [extend, embrace and extinguish](https://en.wikipedia.org/wiki/Embrace,_extend,_and_extinguish) with Lambda, Google is doubling down on its Kubernetes masterstroke with the upcoming “Knative.” - Abraham Ingersoll

* [Serverless on kubernetes](https://gravitational.com/blog/serverless-on-kubernetes/)
