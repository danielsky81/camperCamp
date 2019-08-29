[![Build Status](https://travis-ci.org/danielsky81/camperCamp.svg?branch=master)](https://travis-ci.org/danielsky81/camperCamp)

# CamperCamp Tracker

The [CCTracker](https://camper-camp.herokuapp.com/) is a Full Stack Django Framework Milestone Project build for [Code Institute's](https://www.codeinstitute.net/) Full Stack Web Developer Course.

The CamperCamp Tracker is a tool for a fictional CamperCamp application that allows users to submit issues encountered with the app or create new features that would benefit them. The users have the option to comment and vote on the issues and features they believe are important. Each user can vote for a specific issue only once but have unlimited votes on the features. The votes are free when voting on issues but there is a charge of €5 for every vote used on features.

## The Brief

The project brief required to build a full-stack web application using technologies learned throughout the entire Full Stack Web Developer Course with emphesis on the Full Stack Frameworks with Django module. The core technologies for this particular project include Python and Django framework being the logic and Html, Css, Javascript and D3.js library as a structure and visualization. The CRUD operations were carried out using SQL Postgres and Sqlite3 databases.

## UX

The UX process played a major role in the design of the CC Tracker application with all of its components playing equally important role.

### Strategy

The CCTracker website is created for CamperCamp application users to allow them to submit issues encoutered with the app or create new features to make the app better. The main purpose of the CCTracker is to create an environment where users can raise and comment on issues encountered while using the app and to submit new features they believe would benefit other users while using the app. The site owners on the other hand promise to spend half of development time fixing the issues with the highest number of votes and the other half on building the most popular features.

Based on the above description and the research process the following user stories were identified:

- As a user A, I want to be able to create either issue or feature and give it a title and short description.
- As a user B, I want to be able to vote on the issue I encountered or feature I believe is important.
- As a user C, I want to be able to comment on issue or feature of my interest.
- As a user D, I want to be able to edit an issue or feature I created.
- As a user E, I want to be able to have my unique profile created so I can track all of my activities, including creation of issues or features, votes and comments.
- As a user F, I want to be able to edit or delete any comments I have made.
- As a user G, I want to be able to track status of the issue or feature I created, whether it is just raised, in progress or done.
- As a user H, I want to be able to see the author of the issue or feature and the date and time it was added or updated.
- As a user I, I want to be able to see how many votes and comments each of the issues or features have.
- As a user J, I want to be able to send my feadback or ask questions to the app owners using the contact form.
- As a user K, I want to be able edit my profile in case my details change.
- As a user L, I want to be able to upload an image to personalize my profile.
- As a user M, I want to be able to see the top voted and viewed issues and features.
- As a user N, I want to be able to see the number of raised, being looked after and developed features or fixed issues.
- As a user O, I want to be able to see how many of the issues and features are looked at on daily, weekly and monthly basis.
- As a user P, I want to be able to effortlessly pay for the services that require card payments.
- As a user Q, I want to be able get some communication from the app owners regarding the fixed issues or implemented features in a form of a blog posts. 

### Scope

The CCTracker app should focus on users by allowing them to intuitivelly and effortlessly engage with the website. Users should be able to create the account and amend their details if necessary. However, the main focus should be placed on the creation and engagement with issues and features which is the primarly purpose of the application. The users should be able to create new issue or feature, edit its contents if needed and to vote and comment on other users issues and features. In order to keep the voting system fair for all users, the owners of the issue or feature shouldn't be allowed to vote on their own tickets. The users however, should be allowed to comment on all issues and features, edit their comments and delelte them if they wish to do so.

### Structure

Based on the strategy and scope, the website structure should have clearly organized content and should allow an intuitive interaction for the users. The website should lack any clutter and be informative as much as possible at the same time. There shouldn't be any distractions to the users and the focus should be placed on providing a simple forms for creating issues and features as well as voting and commenting on them.

### Skeleton

The following wireframes were created to determine the visual form and arrangement of the application elements:

- <a href="mockups/small_screen.png" target="_blank">Small screen devices.</a>
- <a href="mockups/medium_to_large_screen.png" target="_blank">Medium to Large screen devices.</a>

### Surface

Once the wireframes were in place, the following visuals were introduced:

- The base colors for the site are orange for the navigation and text headings and white as the main background color. The orange color is assosiated with succsess, encouragement and change while the white color gives the feeling of safety, purity and cleanliness.
- Typography is limited to two typefaces, the "Roboto Condensed" and "Righteous". The "Roboto Condensed" is a clean and modern sans serif typeface making the site readable on both small and large devices. The "Righteous" typeface is used to style the app logotype making it more stylish and memorable thanks to its inspiration taken from the capital letterforms from the deco posters.

## Characteristics

The main idea behind the CCTracker website is to give users a place fpr raising issues they encoutered with the CamperCamp application or a place to create a new feature that could enhance the use of it. The users should be able to engage with all of the ticket raised by commenting and voting on each of the issues or features. The following characteristic play a major role in that process:

- Home page.
- Dashboard page.
- Issues and Features page.
- Navigation bar.

### Home Page

The Home Page consists of a short description of the application and its purpose which upon clicking on a "Learn more" button will reveal more details about its functionality and rules. Furtherdown the page, the users will find a data insights showing the top 5 votes and top 5 viewed issues and features. The list of each is presented in a panel showing the number of votes or issues and related titles. Each of the elements inside these panels will redirect user to selected issue or feature.   

### Dashboard Page



### Issues and Features Page



### Navigation bar