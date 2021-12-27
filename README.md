<h1 align="center">BCN RUN</h1>


BCN RUN is a running club based in Barcelona, Spain for runners of all ability. The members meet up to three times per week for different difficulty level runs in different locations around the city. Members of the club are able to log in to the club website, which allows them access to book a run on a specific date, and to amend that booking if they so wish. Joining the club is quick and easy and guarantees you a wonderful running experience!

<a href="https://bcn-run.herokuapp.com/" target="_blank">View the live project here.</a>

<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640594768/mock-up_agcxgu.png"></h2>

## User Experience (UX)

-   ### User stories

An Agile approach was taken to the planning and execution of this project, which included user stories of differing importance. 
You can find the project board <a href="https://github.com/EllieThurlwell/project-four/projects/1" target="_blank">here.</a>

1. As a user I can easily view information about the club so that I can decide whether I want to join.
2. In order to register as a member, as a user I can provide my details to sign up to the club.
3. In order to find out where the events take place, as a user I can view and interact with points on a map.
4. As a user I can log in to the site so that I have access to the bookings area. 
5. In order to make a booking on a particular day, as a user I can view a calendar and select an available day.
6. In order to make alterations to my booking, as a user I can access, edit, and/or delete my current booking(s).
7. As a user I can contact the running club so that I can give feedback or receive assistance.
8. In order to know my actions on the site have been successful as a user I can see on screen success messages.


-   ### Design
    -   #### Template
        -   The site uses the <a href="https://startbootstrap.com/theme/freelancer" target="_blank">Freelancer</a> bootstrap theme as the basis for its design. This was chosen based on visiblity of important information, cleanliness of design, and responsiveness. The bold colours of the homepage are echoed across the site in buttons and links to give a sense of cohesion without distracting the user. The fonts are clean and easy to read.
    -   #### Imagery
        -   Imagery is used on the site where it fits a specific purpose. The homepage banner image immediately lets the user know what the site is about, while the images on the events page show the meeting place for each run so the user knows the exact locations.
       

*   ### Wireframes

    -   Wireframes for desktop and mobile view, for all planned pages of the site.
    <h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640596685/wireframes_nuvhe2.png"></h2>

## Features

-   Responsive across a variety of screen sizes

-   Registration, login and logout capabilities

-   Feedback for user actions throughout

-   Database models to store user and site data

-   Event bookings and amending

-   Interactive map with custom cluster points

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

- [Django:](https://docs.djangoproject.com/en/4.0/)
    - Fullstack Django framework was used to build the application.
- [Bootstrap:](https://getbootstrap.com/)
    - Bootstrap was used for the design template and layout.
- [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add title icon and to create the favicon.
- [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
- [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
- [Heroku:](https://www.heroku.com/)
    - Heroku was used for the deployment of the project.
- [Cloudinary:](https://cloudinary.com/)
    - Cloudinary was used to store static files.
- [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to check validity of code used throughout the project.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
    - No errors in HTML code
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - No errors in either custom or template CSS
-   [Pep8online Validator](http://pep8online.com/)
    - No errors in Python code
-   [Lighthouse](https://developers.google.com/web/tools/lighthouse) 
    - 95 Performance score 

### Testing User Stories

1. As a user I can easily view information about the club so that I can decide whether I want to join.
    - The homepage is clean and simple, with a short tag line about the club and further information found below. 
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599864/home_vtwt4t.png"></h2>

2. In order to register as a member, as a user I can provide my details to sign up to the club.
    - The Join Us page features a simple form where the user can input their details and be added to the club as a member.
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599864/join_p9yw2e.png"></h2>

3. In order to find out where the events take place, as a user I can view and interact with points on a map.
    - The Events page features a Google Maps map with a cluster of points which can be zoomed into and interacted with, which show the three locations the club meets for runs.
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599864/map_hzfq3m.png"></h2>

4. As a user I can log in to the site so that I have access to the bookings area. 
    - Registered users can log in to their account quickly and easily via the Log In form.
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599864/login_r5q73o.png"></h2>

5. In order to make a booking on a particular day, as a user I can view a calendar and select an available day.
    - The bookings page is available for logged in members and features a short form to book a run. The date field has an expandable calendar allowing users to select a day to book.
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599864/calendar_e9djr4.png"></h2>

6. In order to make alterations to my booking, as a user I can access, edit, and/or delete my current booking(s).
    - Members who are logged in on the site have access to their bookings in order to manage them. They can edit the booking, for example to change the date, and they can cancel their booking completely.
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599863/booking_mupwut.png"></h2>

7. As a user I can contact the running club so that I can give feedback or receive assistance.
    - There is a simple to understand form on the Contact page which allows both site users and logged in members to contact the club should they wish.
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599864/contact_qedgqi.png"></h2>

8. In order to know my actions on the site have been successful as a user I can see on screen success messages.
    - When the user clicks any submit button a message displays to let them know the action has been successful. This occurs on login, log out, sending a message, booking a run, editing a booking, and deleting a booking.
<h2 align="center"><img src="https://res.cloudinary.com/elliecloud94/image/upload/v1640599864/success_jzs7g5.png"></h2>


### Further Testing

-   The website was tested on Google Chrome, Safari and Brave browsers on both desktop and mobile, and Firefox on desktop.
-   The website was viewed on a variety of devices including MacBook, laptop, iPad Air, iPhone 7 plus, iPhone 12 mini, Samsung Galaxy Note8 and Samsung Galaxy Note20 Ultra.
-   Friends and family members were asked to review the site and all functionality to point out any issues. One person got a server error when trying to create an account with the repeat password different than the original. When this was subsequently tested the "You must type the same password each time" message successfully displayed. No other issues or unusual behaviour was reported.
-   Family memebers who are avid runners were asked to test the site from a target audience point of view and with prior experience of club and fitness booking sites. Feedback was positive about both the design and content of the site, and also the functionality for booking and editing runs.

## Future development

-   On a future version of this site some additional features would be implemented:
    - The user would receive an email notification when they sign up to become a member.
    - The user would only be able to book a run on dates when there is an event taking place. On the calendar only those dates would be available to select.
    - The user would receive an email notification when they make, edit, and/or delete a booking on the site.
    - The user would be asked to confirm that they wish to delete a booking before the task is carried out.

## Deployment

### Heroku

- Fork or clone the repository
- Create a new Heroku app
- Set the buildbacks to Python
- Link the Heroku app to the Github repository
- Click button to Deploy

Before final deploy ensure that Debug is set to False and delete DISABLE_COLLECTSTATIC in Config Vars

## Credits

### Code

-   Gitpod workspace came from this Code Institute [template](https://github.com/Code-Institute-Org/gitpod-full-template).
-   Layout of README file came from this Code Institute [sample](https://github.com/Code-Institute-Solutions/SampleREADME).
-   Initial Django app setup along with feedback messages was informed by the Code Institute 'I Think Therefore I Blog' walkthrough
-   Google Maps API code was used for the map on the Events page. All code was taken and then amended from the API documentation.
-   CSS and JavaScript code from the Freelancer template was used to ensure consistent styling and responsive design.

### Content

-   All content was created by the developer.

### Media

All images are used under the Unsplash license of free use.
-   Homepage image from [Rob Wilson](https://unsplash.com/photos/1_bK_F0U43o)
-   Events images from [Enes](https://unsplash.com/photos/f-DvU93UhTs), [Mattia Bericchia](https://unsplash.com/photos/mnuIw2iTb7w), and [David Rüsseler](https://unsplash.com/photos/E0xK8SrIzYA)


### Other

-   The implementation of a datepicker (calendar) on the booking form was informed by [this](https://stackoverflow.com/questions/31548373/django-1-8-django-crispy-forms-is-there-a-simple-easy-way-of-implementing-a) question on Stack Overflow.
-   Many thanks to Code Institute tutor support and mentor [Akshat Garg](https://github.com/akshatnitd) for their help during this project.