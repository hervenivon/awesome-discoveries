# Methodology

They are many different problem solving and optimization approaches or methodologies - most coming with certifications... - that when you start digging you might found yourself lost in the various terms and abbreviations: [design thinking](https://en.wikipedia.org/wiki/Design_thinking), [lean enterprise](https://en.wikipedia.org/wiki/Lean_enterprise), [lean startup](https://en.wikipedia.org/wiki/Lean_startup), [six sigma](https://en.wikipedia.org/wiki/Six_Sigma), [lean six sigma](https://en.wikipedia.org/wiki/Lean_Six_Sigma), DMAIC, DMADV, 5 whys, etc.

While some are coming from industrial production improvement with the idea of reducing waste, and others are synthesis from famous entrepreneurs, they are all directed toward better serving customers. In the end, they provide an incredible tool belt that you can leverage to enhance your process, better design your product and becoming a profitable company. I see here an abundant source of tools and techniques to solve issues and organize yourself and your company.

## The company loop

Redbird provided a data management platform using imagery acquired by drones to generate actionable insights and business decisions for various verticals. When I was the CTO of Redbird, on top of building the platform, we started partnership discussions with large companies in some of the industries we were serving: mines and quarries first. The idea was to develop a joint product: they will provide the data (tire, trucks, blast, sensor), we will aggregate and enhance them along with the data we were already producing from drone imagery.

These partnerships forced us to organize our startup as being the most efficient possible:

1. We needed to appear serious to our interlocutors,
1. We urge to keep our startup agility,
1. Our budget was short and our need for creativity colossal.

The most frugal and efficient methodology I knew was "lean startup." This methodology was our starting point. Coming from a consulting company in which I had to work with the fortune 500 for typical two years projects or in the innovation group to build new offering I was lucky enough to enrich our experience with a set of other techniques and methodologies: design thinking, UX Design, six sigma, scrum.

I was genuinely convinced that being transparent on the way we worked - one iteration after the other, with failure being part of the process, a continuous feedback loop to enrich the iterative development approach and to continuously improve, encourage criticism and learn from it - will turn these initiatives into a success.

Our partners trusted us. As a conclusion, we built several products we sold from machine efficiency geolocalized to blasting history and quality measurement becoming a digital twin of our customers' physical world.

The following illustration represents my ideal methodology to grow a company and a product in a fast innovative and competitive environment (Design Thinking + Lean Startup + Scrum + Experience): the company loop.

<img src="../resources/company-loop.png" alt="The company loop. Image Credit: Hervé Nivon"/>

While "Ideas" may be the starting point of the loop, I advise starting from insights which often are a pain point.

* **Comprehend**: the actions which lead to ***ideas*** from ***insights***
  * **Empathize**: What is the true problem? Do your homework and prepare yourself to be in your customers' shoes.
  * **Define**: How do my customers fill the issue? Use customers' interviews, feedback, and observation to define the customers' point of view.
  * **Ideate**: What are the craziest and most creative ideas you can come with? It is time to generate a flow of possibilities.
  * **Prototype**: How those ideas can operate? Put yourself at work and experiment. Rough sketches will do the job.
  * **Test**: What is the reaction against the prototype(s)? Does it work? Conduct workshop, test internally, play roles, act.
  * **Deliverables**:
    * Actionable ideas
    * Personas
    * Mood boards
    * User journeys
    * User flows
    * Wireframes
* **Build**: the actions that transform ***ideas*** into a ***product***
  * **Detail**: What do these ideas mean from a technical standpoint? Detail as much as possible. Use features, epics and user stories.
  * **Plan**: How do we organize the work? What are the priorities?
  * **Implement**: Time to make things real! Build, code, implement, iterate. Use open source, do not reinvent the wheel, leverage the cloud and its service. Focus on your core business and added value.
  * **Test**: Are your product working accordingly with your ideas? Unit tests, integration tests, usability tests.
  * **Review**: Time to learn from the development cycle to do a better iteration next.
  * **Deliverables**:
    * Continuous delivery of the product in an incremental fashion
* **Measure**: the actions that dissect ***product*** usage into ***insights***
  * **Define metrics**: What is relevant for your product? Churn, number of unique daily visit? Time spent on the platform? Tool duration usage? What are the relevant events?
  * **Collect data**: Continuously measure your defined metrics. Data will come from your product. Conduct
  * **Gather customers feedback**: Prepare the comprehension phase, gather your customers' feedback, listen to them, observe them. Provide different versions of the application and measure reaction differences.
  * **Visualize**: Put your data at work, spreadsheets are not enough. Assemble your measures in something meaningful to everyone. Leverage real-time analytics, alerting and monitoring.
  * **Evaluate**: What does these numbers and chart significate? Determine the quality of your data, judge the significance and how much it worths. Assess and select.
  * **Deliverables**:
    * Product heatmap
    * Cohort analysis
    * Funnel analysis
    * Dashboard
    * Geographic repartition
    * Technical environment
    * Pain points
    * Interviews

The overall idea is to minimize the whole cycle duration to achieve a better time to market for your product: build fast, fail fast. Each feature and your product must be thought and developed as a minimum viable product (MVP). Only build the strict minimum, avoid any waste, chase them, take as many shortcuts as possible, avoid reinventing the wheel. You will enrich it incrementally, one small step at a time with the validation of your customers every time.

A pivot is a shift in your business strategy in order to test and potentially validate a new approach regarding your initial product or business model. It typically happens from the comprehension of the product's insight and customer feedback.

Another virtue of this cycle: a strict implementation will lead to a better market fit.

When I think about the sentence "What the customer really wanted", here is the drawing which comes to my mind first. [How Projects Really Work?](http://www.projectcartoon.com/). It has been circulating for years with several variations and additions. My preferred version:

<img src="../resources/how-projects-really-work.png" alt="What the customer really wanted"/>

From here on, the paragraphs further list and detail methods or tools that have proven useful to me.

## 8 types of waste

Lean Six Sigma principles focus on eliminating eight varieties of waste (you will often read Muda). They form the acronym DOWNTIME. The following paragraph describes them applied to software development.

* Defects

Defects are errors that require additional time, resources (, and money) to fix. In a traditional manufacturing process, it can be a defective part that must be remade. In software development, it is certainly the easiest waste variety to understand in the list. Bugs and software development are going hand in hand since [1947](https://en.wikipedia.org/wiki/Software_bug). But, to my mind, defects in software development don't only appear in final the code they can occur all along the process from the software design to the poorly annotated data in machine learning.

* Overproduction

Overproduction is production ahead of demand. Ex: too many goods are produced and waiting to be sold at the warehouse. In software development, it means developing the wrong feature, either because it is badly designed or because it doesn't match any requirement and is therefore not used.

* Waiting

Waiting is the delay between steps in production. Ex: when the next person in line is overwhelmed, you must wait. In software development, it can happen in several places: when developers are waiting for a change request approval, when they are waiting for functional clarification, when they wait for builds in the CI.

* Not-Utilized Talent

In small businesses, the team is often the most critical asset; not and underutilized talents, skills, and knowledge can have a pernicious, negative and sometimes destructive effect on an organization. In small businesses and in startups in particular, people join you because they believe they can have a true impact which is way harder to achieve in big corporations. Recognizing their energy, nurturing them will provide great benefits. You must trust your team and leverage it as much as you can, and this is why you always must seek and be attentive to feedback. Wrong task assignment, lack of training, lack of teamwork, secrecy or poor communication are some evidence of not and underutilized talents.

* Transportation

Transportation waste is the movement of materials and goods that are not required to perform the processing. Ex: when you need to move a piece to another plant area because of a poorly design arrangement. It can be because of too many steps, miss designed workflows. In software development, we are speaking of information transportation which might seem seamless. Nevertheless, it can happen: when your customer feedback is going through too many steps before becoming actual lines of code, when you have to switch tasks continuously or when you have to duplicate data to perform machine learning training locally.

* Inventory

Inventory waste is all produced parts and material that have been purchased and are waiting to be used. It also includes work-in-process, everything that is not yet ready for shipment or sale. In software development, I mainly see it as non-deployed software which can be due to too long development cycles or finished software not validated and waiting for prime time

* Motion

Motion waste refers to any movement one has to do to accomplish his task for one employee, between employees, for a machine. In software development, we can see it as the necessary hand-offs between different jobs. Beyond the material conditions, such as the quality of the workspace highlighted in the industry, motion waste can be seen as the knowledge which is lost each time a deliverable is handed off between 2 employees to finish a task.

* Extra-Processing

Extra-processing waste is deduced from processes that require multiple versions of the same task, poorly defined processes or task with low value added. Examples: Excessive reports, data duplications, lack of standards. In software development, some working with agile methodologies argues that even estimating development time is a waste; this is the [#NoEstimates](https://twitter.com/search?q=%23noestimates) movement.

These eight varieties of waste are inspired by the [Toyota Production System](https://en.wikipedia.org/wiki/Toyota_Production_System). You can learn more about their definition and some other examples [here](https://www.processexcellencenetwork.com/business-transformation/articles/the-8-deadly-lean-wastes-downtime), [here](https://www.solutionsiq.com/resource/blog-post/waste-in-software-development/), and [here](https://www.solutionsiq.com/resource/blog-post/more-waste-in-software-development/).

## DMAIC & DMADV

DMAIC used for projects aiming at improving an existing business process and DMADV used for projects aiming at creating new product or process designs are two 5 steps methodologies coming from Six Sigma.

What is interesting is the actions these methodologies trigger.

### DMAIC

* Define the project goals from the voice of the customer and their requirements
* Measure key aspects of the current process, collect relevant data and calculate the 'as-is' process capability
* Analyze your measures to determine cause-and-effect relationships. Verify all factors have been considered. Get to the root cause of the problems you are looking at
* Improve the current process. Set up a pilot to establish process capability
* Control the new process to ensure that it can achieve the objective. If there is a deviation, repeat the process.

### DMADV

* Define the goals that are consistent with customer requirements and demands according to your strategy
* Measure criteria which are crucial to your new product or process
* Analyze your findings to identify alternatives
* Design an improve these alternatives
* Verify these alternatives, set up a pilot, implement the process or product.

## Value-stream mapping (VSM)

In short, value-stream mapping is a technique that helps to determine and distinguish valuable activities from wasted time and value in a production flow of material and information that is executed to bring products to customers.

VSM uses a set of predetermined symbols to map your process in an intelligible way.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/VSM1.JPG/1000px-VSM1.JPG" alt="VSM standard symbols from Wikipedia"/>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/ValueStreamMapParts.png/600px-ValueStreamMapParts.png" alt="A VSM example from Wikipedia"/>

VSM can be used to improve any process where there are repeatable steps, and handoffs. In software development, you can make an analogy with continuous delivery.

Learn more on [wikipedia](Value-stream mapping) or watching ["How to read a value stream map?"](https://vimeo.com/23684934) video.

## Interviews

* Use the [STAR](https://en.wikipedia.org/wiki/Situation,_task,_action,_result) technique to conduct your interviews: **S**ituation, **T**ask, **A**ction, **R**esult. This will help you gathering all relevant information and help interviewed people being complete.
* Set your objectives and review objectives of other with [SMART](https://en.wikipedia.org/wiki/SMART_criteria) Goals only: **S**pecific, **M**easurable, **A**chievable, **R**ealistic, **T**ime-related

## Virtues of constraint

[Peecho](https://www.peecho.com/) product owners had to do fifty push-ups as payment for each user story that they wanted to add to an ongoing sprint.
[myTommorows](https://mytomorrows.com/) Developer dance-offs are legendary: during the daily stand-ups, you are only allowed to speak while dancing
[Teletext](https://teletext.io) For example, all our logo design is done with technical diagramming tool Omnigraffle, so there is no way we could use hideous lens flares and such.

At redbird, budget constraints and technology constraints ended up fueling our creativity.
