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

The Home Page consists of a short description of the application and its purpose which upon clicking on a "Learn more" button will reveal more details about its functionality and rules. Furtherdown the page, the users will find a data insights showing the top 5 votes and top 5 viewed issues and features. The list of each is presented in a panel showing the number of votes or issues and related titles. Each of the elements inside these panels will redirect user to selected issue or feature. There are as well 2 pie charts showing the overall number of raised issues and features brokedown by categories of development progress, so whether the item is new, in progress, done, etc. At the bottom of the page, there are 2 bar charts showing daily, weekly and monthly development progress for raised issues and features. Both type of charts are color coded for easier readability, with red and its shades for issues and green with its shades for features.  

### Dashboard Page

The Dashboard Page was created with user in mind as it contains all of user application history and profile data. The page consists of a dummy user image which can be replaced with any image user wishes to upload and a 5 tabs panel. The tabs contains details of the following user interaction with the site:

- Votes tab, showing voted issues and features with number of given votes for each.
- Issues tab, showing issues created by the user.
- Features tab showing issues created by the user.
- Comments tab, showing comments added by the user to the blog, issues and features.
- Profile tab, showing user profile details that can be updated or deleted. The user has an option to upload an profile image here as mentioned earlier.

All of the issues, features and comments displayed in the tabs can be accessed for details from here.

### Issues and Features Page

Both, the Issues and Features pages have the same structure and layout. The top part of the page contains a short description and a "Add new issue"/"Add new feature" buttons. The remaining part of the page contains a list of 4 items per page. Each item, whether an issue or feature is displayed in a panel with title and a short fragment of a description. Furthermore, at the bottom of each panel, there is a paragraph showing the author, published and updated date, number of views and number of comments. Next to the title of the issue and feature, users can find two labels, one showing the status of the item, the other showing the number of votes. The status panel is color coded for each of the category type. Users can access details of each item by selecting the desired panel. The users have an option as well, to filter the page view by category by selecting the "Tags" dropdown menu. This menu, which contain as well the total number of issues or features can be found just below the page description at the top of the page.

### Navigation bar

The navigation bar sits at the top of the page and consists of links to all of the pages, including dashboard, issues, features, blog, contact and login/logout. There is as well a "create" dropdown list, which allows users to create an issue or feature instatnly without a need to go through the dedicated pages for each. This can be accessed from everywhere on the page making it qucik and easy to create a new issue or feature.

### Other Features

The other features of the CCTracker are as follows:

- Responsive layout that allows users to preview website on all devices.
- Simple and clean design with intuitive navigation and simplified data.
- Custom button styles which adds meaning and visual indication.
- Hover effect on clickable content to help users navigate and interact with the application.
- Notifications and personalised messages for visitors and logged users that either greets them, notify about user valid changes or display errors if needed, making the connection user friendly.

## Database Schema

The database schema consists of 8 tables build mainly around the default Django User table with many-to-one relationship model. During the development stage of the project the primary database used was the "sqlite3" which was later on migrated into the "Heroku Postgres".

Te details of the schema can be found below:

- <a href="db_schema/db_schema.png" target="_blank">database schema</a>

## Technologies Used

- [Django](https://www.djangoproject.com/) - open source Python Web framework.
- [Python](https://www.python.org/) - Used for application logic.
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript) - Used to make the application interactive.
- [HTML5](https://www.w3.org/TR/html52/) - Core structure of the website.
- [CSS](https://www.w3.org/Style/CSS/) - Main style of the website.
- [3D.js](https://d3js.org/) - Used to produce bar and pie charts data visualizations inside the application.
- [Dc.js](https://dc-js.github.io/dc.js/) - A javascript charting library with native crossfilter support.
- [SQLite](https://www.sqlite.org/index.html) - SQL database engine.
- [Postgres](https://www.postgresql.org/) - Open source object-relational database.
- [Balsamiq Mockups](https://balsamiq.com/) - Used to sketch quick wireframes for website's UX design.
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/) - Chrome browser tool used to iterate and debug the website.
- [PEP8](http://pep8online.com/) - Online PEP8 checker.
- [Parallels](https://www.parallels.com/) - Software providing hardware virtualization used to test application on other platforms like Windows or Linux.  
- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) - Online Chrome tool used to audit the website's performance and accessibility.
- [Caniuse](https://caniuse.com/) - Online browser support tables for modern web technologies.
- [Github](https://github.com/) - Project's repository.
- [Visual Studio Code](https://code.visualstudio.com/) - Text editor used to write down all the code.
- [Google Fonts](https://fonts.google.com/) - Typefaces used to style the website.
- [Dbdiagram](https://dbdiagram.io/home) - A Relational Database Diagram Design Tool.

## Testing

During the website development stage I have conducted two types of testing, manual and automated. The manual testing was ongoing throughout the whole development stage while the automated test was conducted using unittest module built in to the Python standard library when the project was at its finish.

### Manual Testing

- Chrome DevTools

Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. This tools allows me to instantly preview and edit my website but I was mainly using it to diagnose problems and fix them on the go.

- Operating Systems:
    - MacOS
    - Microsoft Windows
    - Linux
    - Android
    - iOS

The Operating Systems test played an important part of the manual testing. Majority of the test was done using the Parallels software on MacOS which allows me to test my application on Linux and Windows virtual machines. The test consisted of running the application on the most popular browsers within these Operating Systems and validating the expected behaviour of the site.

- Web browsers:
    - Chrome
    - Firefox
    - Safari
    - Opera
    - Internet Explorer

I made sure to check if browser prefixes where necessary and validate some of the code with "caniuse" website but to make sure that there are no errors with the website I was doing a cross browser testing from time to time. It basically consisted of running the site on these browsers, changing the size of the browser window and where possible using the native developer tools to check site responsiveness and functionality. These tests were run on desktop, tablet and smartphone devices.

- Devices:
    - desktop
    - tablet
    - smartphone

I run a manual testing on few types of devices whenever I had a chance but mainly I was testing the website using desktop, tablet and smartphone, so I could cover the most popular screen sizes.

- User Stories Testing

The following user stories from the UX section were tested to make sure everything works as intended:

