# **Capstone Project**

## Name: ironenclave.com

## Description:

Iron Enclave is resource for the strength athlete and enthusiast community. It is a tool for setting personal goals and tracking progress, a resource for quality information on all things strength sports, and a forum where people can connect with other members of the strength community.

### Libraries and Frameworks:

- Django
- Bootstrap
- dc.js
- <span style="color:cadetblue"> what about data visualizations? if you're going to use pandas i assume you'll need to display data to the user as well</span>
- <span style="color:green"> I will use dc.js instead of pandas to handle the user graph visualization. </span>

## **Functionality**

### User perspective:

1. Landing Page-- Two buttons hovering over a background image. One will read: "Visit the Enclave" and link to the home page. The other button will read: "Join the Enclave" and link to a sign-up page.

2. Home Page-- The home page will feature a side navigation bar with links to: a resources page, forum page, and profile page.
   - The resource page will be accessible to visitors and members.
   - The forum page will be visible to visitors, but only members may contribute to the discussion board.
   - The profile page will only be accessible by members.

3) Sign-up Page-- The sign-up page will include a form for creating a new profile. Required information will be: username, password, and email.

   - New user data will be stored in a user model.
   - Upon submittion of sign-up form the new user will be directed to their profile page where they can customize their profile.

4) Resource Page-- The resource page will feature links to tutorials, equipment, articles, books, coaching sites, and podcasts.

5) The Forum Page-- A basic web forum where members can discuss topics and comment on other member's posts as well as a search feature for searching topics in the forums.

6) The Profile Page-- The profile page will allow the user to customize their profile to include:
   - A profile picture
   - Set short and long term goals
   - Enter their best lifts
   - A graph that tracks their progress over time. The graph will include:
     - A view toggle to compare your progress to other lifters in your weight class
     - Where you are in relation to your goals
     - Highlights of personal records

- Profile information will be stored in a Profile model.

## Pages:

\*\*MVP = to be completed by capstone presentation date

- Landing Page \*\*MVP
- Sign-up Page \*\*MVP
- Home Page \*\*MVP
- Profile Page \*\*MVP
- Resource Page \*\*MVP
- Forum Page

## Functions:

- User sign-up form \*\*MVP
- User authentication \*\*MVP
- Profile customization
  - Add profile picture \*\*MVP
  - Add best lifts \*\*MVP
  - Set goals
  - View progress graph
- Forum
  - Forum search function

## **DATA MODEL**

- User/Profile model: 1 to 1
- Forum model: 1 to many
- User MODEL:
  - Username
  - Password
  - Email
- Profile MODEL:
  - Profile picture
  - Best lifts
  - Goals
  - Progress graph
  - <span style="color:green"> Display (ability to customize model) </span> <span style="color:cadetblue"> what do you mean by this? is the user going to be able to customise the data model? 0.o</span>
   <span style="color:green"> You can ignore that part. I don't even remember why I put it in there. I just want the user to be able to add and remove data from the graph.</span>

- Forum MODEL:
  - Forum posts

#

## MVP by presentation date:

<span style="color:cadetblue"> you need significnatly more functionality than this for your mvp. this is too basic for an mvp that you've had 70 in-class hours to work on.</span>
**I added these items

- user model
- profile model
- forum model **

- User sign-up form
- User authentication **
- User Profile
- User graph **


## **SCHEDULE**

1. Week:
   - App set-up and templates-- Day Mon-Wed
   - User model-- Day Wed-Fri
   - Profile model-- Day Fri-Sun
2. Week:
   - User sign-up form-- Day Mon-Tues
   - User authentication-- Day Tues-Fri
   - User profile-- Day Fri-Sun
3. Week:
   - User profile-- Day Mon-Tues
   - User progress graph--Day Tues-Sun
4. Week:
   - User progress graph-- Day Mon-Wed
   - Front-end-- Day Wed-Fri
   - Testing and debugging-- Day Fri-Sun
5. Week
   - Forum model-- Day Mon-Wed
   - Forum search function-- Day Wed-Fri

#

# INSTRUCTOR NOTES

- <span style="color:cadetblue"> how are you going to implement the forum?</span>
- <span style="color:green"> I will create a model for the forum in Django or use a forum package that has already been created.</span>

- <span style="color:cadetblue"> are there any external data sources, or other resources you could take advantage of to add any useful features/functionality to this? the app as it stands is a good idea, and ok as a capstone project. i'm just wodnering if there's a way that you can take it over the top and out of "just ok"</span>

- <span style="color:green"> I want to learn how to use web scraping to pull in the national powerlifting records by weight class and add them to the graph.</span>