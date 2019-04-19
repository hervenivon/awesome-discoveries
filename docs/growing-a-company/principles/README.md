# Principles

The following paragraphs cover in details what I think are the most important principles to follow building your own company in our modern context:

1. [Widespread core values](#widespread-core-values)
1. [Be a leader](#be-a-leader)
1. [English first](#english-first)
1. [Document everything](#document-everything)
1. [Embrace change](#embrace-change)
1. [Default to Transparency](#default-to-transparency)
1. [Data driven](#data-driven)
1. [Security first](#security-first)
1. [Cloud only](#cloud-only)
1. [An API for everything](#an-api-for-everything)
1. [Failure is waiting for you](#failure-is-waiting-for-you)
1. [Automation is key](#automation-is-key)
1. [Be proud](#be-proud)

## Widespread core values

You should have clear and widespread core values. It is not enough to keep them for you, these core values should be known from everyone and should be part of all your interviews and you must ask each interviewed people how do they feel about them.

## Be a leader

There is a litany of management styles in the literature (Autocratic, Persuasive, Laissez-faire, Consultative, etc.). The past 15 years of management proved to myself that a good manager doesn't fit in one and only box. Furthermore your management style is really personal and may vary overtime or depending of the people you interact with. It is all about Human relations.

I think that I adapt myself to my interlocutor and the situation. I might be persuasive, consultative, or laissez-faire, but in all cases I invest a lot of my time in the relationships I'm building.

To my mind, there is only one rule of thumb, your collaborators will prefer working with a leader than with a boss!

<img src="./resources/boss-vs-leader.png" width="250" alt="Boss VS Leader">

## English first

Everything must be written in English. And for us, French people, it is unfortunate, but bad English is still better than French. You should at least write all of your documentation in English. This is the bare minimum.

Some key reasons gathered from the [FAQ](https://www.grammarly.com/faq) page of [Grammarly](https://www.grammarly.com/) a tool I use every day to enhance my English skills and quality:

> * One quarter of the world’s population speaks at least some English.
> * More than one billion people are studying English worldwide.
> * 80 percent of computer data is processed and stored in English.
> * Most satellite transmissions are carried in English.
> * More than half of the world’s newspapers are published in English.

## Document everything

Every piece of your work, from idea to real life architecture, should be documented.

## Embrace change

What you have in mind will never be in place, the secret is to adapt yourself, your strategy, your vision, your plan and everything in order to keep your project healthy. You must be agile and [don't just pretend to be](https://www.flickr.com/photos/lucaminudel/6059269914/).

<img src="./resources/lucaminudel_dilbert_bermuda_triangle_of_agile.png" alt="You can be agile inside this triangle! Image Credit: Luca Minudel"/>

## Default to Transparency

When Buffer introduced [Open Salaries](https://open.buffer.com/introducing-open-salaries-at-buffer-including-our-transparent-formula-and-all-individual-salaries/) they shared their second core value: "Default to Transparency". Back in 2013, I was working in one of the 5 biggest consulting company in the world, it inspired me a lot. At Redbird, then Airware and Delair, in hindsight, I can say that as a company we haven't always been transparent. In my next startup I will do as much as I can to embrace that principle, as strong as possible from internal email with open CC to personal shared self-improvement through open progress report. And, even if it is hard for my French culture 🐔🇫🇷🥖, up to Open Salaries!

Open your meetings, let interested people to come in as flies on the wall. Ask for candide feedback at the end of it.

What do you need to take a good decision? Personally, I require as much information as possible, I need a full context and I need to understand the whole situation which is often the case being a CTO or a VP of engineering. But, if you expect your team to take the smartest decision possible, they will need the same level of information than you.

> "lots of traditional, widely accepted, and perfectly legal business practices just can’t be trusted by customers, and will soon become extinct, driven to dust by rising levels of transparency, increasing consumer demand for fair treatment, and competitive pressure" - Don Peppers and Martha Rogers in [Extreme Trust: Honesty as a Competitive Advantage](https://amzn.to/2Cg0BYz)

Transparency will help more than it will harm. Transparency builds and strengthens trust in your team and with your customers.

[Why we made our product roadmap public (and how to build your own)](https://frontapp.com/blog/2015/04/02/why-we-made-our-roadmap-public-and-how-to-build-your-own/) - Front application explain why they made their roadmap public. It still is the case. Personally, I truly believe, that secrecy doesn't help any company to expand, its capability to execute better, and faster is. In short: users like that you share tour vision, product gets better even faster because of direct feedback, team accountability. Some public roadmaps:

* [Trello](https://trello.com/b/nC8QJJoZ/trello-development-roadmap)
* [Front](https://trello.com/b/kZsVVrc8/front-product-roadmap)
* [KanbanMail](https://www.notion.so/Public-Roadmap-7adabe84ea7a47588f4b5e8fa9e5dde8)
* [notion](https://www.notion.so/What-s-New-157765353f2c4705bd45474e5ba8b46c)

## Data driven

Think of your product in terms of data, gather every piece of data you can, measure, track and manage it, put it in your contracts and terms of services:

* It will be easier to determine the next iterations of your product (what features are used, how long did it take to load the page, what is the require accuracy)
* You will better serve your customers
* Data enables Machine Learning, the only mean actually.

## Security first

Security should be at the root of every technical, product or strategy choice. Your customers are your value. You will have to gain your customers’ trust, and you should do everything you can to keep it.

For any service, you should avoid to build your own authentication system and you must enable [SSO](https://en.wikipedia.org/wiki/Single_sign-on) as soon as possible. One password to rule them all is key to most B2B deals.

There are always ways to enhance your security. Beware, the system’s security your building should never slow down your people otherwise they will find a workaround. Everyone in the company should embrace it and support it. (Another question for your future recruitment).

[GDPR](https://eugdpr.org) is here to help anyway 🚨.

Open source in the recent years helps accelerate development of new projects, in the mean time, it has been a way to spread vulnerabilities in the most efficient way ever. To understand how open source can arm any project read ["I'm harvesting credit card numbers and passwords from your site. Here's how."](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5).

GitHub is providing more and more services ([token scanning](https://github.blog/2018-10-17-behind-the-scenes-of-github-token-scanning/), [security alerts](https://github.blog/2018-10-09-applying-machine-intelligence-to-security-alerts/), [bug bounty program](https://bounty.github.com/index.html#open-bounties)) to secure your repositories. That is great, but depending on your project you'll need further security, you might be asked to track your open source dependencies. Sooner than later, it will happen. There are a lot of tool in the wild. Here is where to start:

* [Fossa](https://fossa.io/)
* [Dependency Track](https://dependencytrack.org/)

You must be careful at any stage. I often share a story with my new hires about an intern that had to pay more than $8000 because of pushing AWS secret keys on one of his public repository. [`gitleaks`](https://github.com/zricethezav/gitleaks) will help you to ensure that in a CI/CD pipeline.

When you are dealing with large enterprises you are asked to prove the security level of your company. The security of devices used by your employees is part of the equation. Tools such as [Jamf](https://www.jamf.com/products/jamf-pro/) will help you manage and protect all Apple devices from anywhere.

## Cloud only

Everything must be in the cloud, nothing should ever take a way into your IT office, not a single server should ever exist into that cabinet. The only thing you should ever need is a VERY good internet connection. Every tool you’re about to use should be a service otherwise drawbacks are licensing nightmares and or on-site server maintenance. The other advantage of hosting everything in the cloud is to accelerate really strong, really quick.

If it ever happens to install a server, you will always need someone to maintain it, and it will be really hard to get rid of it.

Priority is your business, and all the time you spend should go into customer value creation. As a startup, you cannot afford reinventing the wheel or spending money to build things than others do better than you.

## An API for everything

Every development you make should be served through an API. This is a necessary mean to enable growth and make it sustainable for your project and your teams.

> "All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions. Anyone who doesn’t do this will be fired.  Thank you; have a nice day!" - Jeff Bezos CEO of Amazon

## Failure is waiting for you

Design with failure in mind. Failure is the first event you'll met in any project. What you will have at the end is likely to be more complex than what you desire. You have to embrace that fact, it is going to happen.

> "Everything fails, all the time" - Werner Vogels, CTO of Amazon

Some companies are even playing with their production environment. Netflix's [Chaosmonkey](https://github.com/Netflix/chaosmonkey) randomly terminates computing unites that run inside of a production environment exposing engineers to failures by design. It inherently incentivizes them to build resilient services.

## Automation is key

Automation is the key to successful development teams. And, it should come in the early stages on your internal tooling or your production workloads. Automation will save you time and money all along your journey

Tooling your developers is mandatory, and it you should let them be free (help them to have a good development environment. Enable your developers and keep the evolution process of the tooling easy. Let them propose, enhance it and share their creation with the rest of your team.

## Be proud

Overall, assume your choices, justify them, and proudly defend them. This is not because you are not using the last trendy single page application framework that your code base is crap or a spaghetti mess. Your startup will always have a history, you must be proud of it and all the lessons learned along the way.
