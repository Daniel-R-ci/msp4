# The Barn User Stories

These are the fully detailed user stories for the project, also found and tracked on  [Github Projects](https://github.com/users/Daniel-R-ci/projects/8/)

(MVP) means the criteria/task should be completed before moving on to the next task (and ulitately project submission). When all MVP criteria/tasks are fullfilled, work can start on non mvp-tasks in order of priority.

## Owner: Publish courses and events
As a _business owner_, I would like to _publish information about upcoming courses and events_ to _let customers now about them and to eventually let them sign up for them_.

Priority: High

**Criteria**

- Publish information about upcoming courses and events (MVP)
- After customer signup, view a list of attending customers (MVP)

**Tasks**

- Implement necessary models and administer them via Django Admin (MVP)
- Publish the information (MVP)
- Integrate admin functions in frontend user interface to not rely on Admin interface

## Owner: Post articles / news

As a _business owner_, I would like to _publish news about new supplies, craft tips etc_, to _inspire future craft projects and bring more customers to the store_.

Priority: High

**Criteria**

- Publish various news relating to the business (MVP)

**Tasks**

- Implement necessary models and administer them via Django Admin (MVP)
- Publish the information (MVP)
- Integrate admin functions in frontend user interface to not rely on Admin interface

## Customer: User registration
As a _customer_, I would like to _register a user account_ in order to _take advantage of the online fuctions being offered_

Priority: High

**Criteria**

Implement user handling such as sign up, login/logout and password recovery (MVP)

**Tasks**

- Implement user handling as outlined above using Django AllAuth or equivilant (MVP)
- To make user registration easier, allow customers to use Google accounts to sign up

## Customer: Course and event registration

As a _customer_, I would like to be able to _register for upcoming courses and events_ in order to _secure a spot at those that interest me_

Priority: High

**Criteria**

- Let registered users sign up for courses and events (MVP)
- If not free of charge, offer participants a secure way to pay (MVP)

**Tasks**

- Implement course / event registration on a first-come, first-served basis, while still offer reasonable time to complete registration process. (MVP)
-Implement secure payments using STRIPE (MVP)

## Customer: Comment on articles
As a registered user, I would like to be able to _comment on articles and news_ posted on the website in order to _provide feedback to the store_.

Priority: Medium

**Criteria**

- A functioning comment system for registered users (MVP)

**Tasks**

- Implement comment system with full CRUD functionality for registered users (MVP)
- Through Admin interface, make sure superusers can delete/hide comments (MVP)
- Through Frontend user interface, give superusers a way to hide/delete comments

## Customer: Post information about own projects or ask questions

As a _registered user_, I would like a way to _show my projects or ask craft related questions_ in order to _receive feedback and interact more withthe creative community around The Barn._

Priority: Medium

**Criteria**

- Offer users a way to fullfill the above user story

**Tasks**

Task and scope to be defined later

## Owner: Inforamtion and contact

As a _business owner_, I need a way to _give general information about my store, as well as a way to let customers contact us_ in order to _provide expected customer service_.

Priority: Medium

**Criteria**

- Opening hours, adress and contact information easily found on the website (MVP)
- Contact form for general questions (MVP)

**Tasks**

- Opening hours and other relevant information easily found in headers/footers and/or contact page. (MVP)
- Contact form (MVP)

## Customer: Sign up for secret box subscription

As as _customer_, I would like to _register for The Barns secret craft boxes_ in order to _try new creative areas of the craft hobby that I would not otherwise have considered_.


Priority: Low

**Criteria**

- A subscription system for quarterly secret boxes within various fields such as painting, textile, wood, or child crafts.

**Tasks**

To be defined later


[Back to Main Readme](/README.md)

