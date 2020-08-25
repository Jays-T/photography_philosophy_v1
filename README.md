# <a href="#">Lanthus Clark</a>

* This project is currently purely for educational purposes.

# CONTENTS

* UX
  * <a href="#Owner-Goals">Owner Goals</a>
  * <a href="#User-Goals">User Goals</a>
  * <a href="#User-Stories">User Stories</a>
  * <a href="#My-Strategy">Strategy</a>
  * <a href="#Structure">Structure</a>
* <a href="#User-Interface">UI</a>
* <a href="#Features">Features</a>
* <a href="#Scope">Scope</a>
* <a href="#Information-Architecture">Information Architecture</a>
* <a href="#Defensive-Design">Defensive Design</a>
* <a href="#Technologies">Technologies Used</a>
* <a href="#Sources">Sites Sourced from</a>
* <a href="#Testing">Testing</a>
* <a href="#Bugs">Bugs</a>
* <a href="#Deployment">Deployment</a>
* <a href="#Credits">Credits</a>

<img src="/wireframes/responsive-900x544.png"/>

# **UX**

# Owner Goals

#### As the owner, my initial goals are:

* 

#### Long-term goals for the owner are:

* 

# User Goals

#### For the user the goals are:

* To be able to:

# User Stories

1. "As a **Photography enthusiast** "
2. "As a **Random User** "
3. "As a **Fan of the Site Owner** "


# My Strategy

*

# Structure

<img src="#"/>

# User Interface

* Initial concept

<img src="/media/wireframes/milestone_4_wireframes.png"/>

* 
* Fonts

  * 

# Features

- [x] Register User Account
- [x] 
- [x] 
- [x] 
- [x] 

# Features still to implement

- [ ] 
- [ ] 
- [ ] 
- [ ] 



# Scope

* This is a fully functional web store

# Information Architecture

* 

# Defensive Design

* 

# Technologies

* <a href="https://html.com/" target="_blank">HTML</a> - for overall UI structure
* <a href="https://css-tricks.com/" target="_blank">Css</a> - to style the site
* <a href="https://www.getbootstrap.com" target="_blank">Bootstrap 4.5.0</a> - for grid structure and responsive design
* <a href="https://www.fontawesome.com" target="_blank">Font Awesome</a> - for icons
* <a href="#" target="_blank">Django</a> - as my framework
* <a href="https://www.python.com" target="_blank">Python</a> - for app routes and CRUD functionality
* <a href="https://jinja.palletsprojects.com/en/2.11.x" target="_blank">Jinja</a> - for templating, data routing and page information populating
* <a href="https://mongodb.com" target="_blank">MongoDB</a> - for the Database
* <a href="https://www.jquery.com/" target="_blank">jQuery</a> - used by Bootstrap and for various site actions
* <a href="https://www.gitpod.io/" target="_blank">Gitpod</a> - as my development environment
* <a href="https://www.github.com/" target="_blank">GitHub</a> - for version control
* <a href="https://www.heroku.com" target="_blank">Heroku</a> - for deployment


# Sources

* <a href="https://www.w3schools.com">w3schools</a> - For general knowledge or whenever I was stuck on something simple
* <a href="https://docs.mongodb.com/">MongoDB Docs</a> - for questions relating to database interaction
* <a href="https://css-tricks.com/">Css Tricks</a> - to solve styling and element placement issues
* <a href="https://fonts.google.com/">Google Fonts</a> - for fonts

# Testing

* Testing was done regularly throughout the entire process 
* Each function was tested and re-tested
* Defensive Design was tested by manually adding endpoints from areas where access should not be allowed
* Site navigation and links tested thoroughly, navigation breaks also tested using the back and forward buttons

* All HTML validated with <a href="https://validator.w3.org/">w3 validator</a>
  * The HTML validator returned errors due to the jinja templating used to structure the site
* All CSS validated with <a href="https://jigsaw.w3.org/css-validator/">w3 css validator</a>

* I used various code and syntax checkers during the entire process and before project submission

**Checkers Used**
* <a href="https://extendsclass.com/python-tester.html">Python Syntax Checker</a>
* <a href="http://pep8online.com/">Python Checker</a>
* <a href="https://esprima.org/demo/validate.html">Esprima JavaScript Checker</a>
* <a href="https://jshint.com/">JsHint JavaScript Checker</a>

## This site has been tested manually

Browsers tested: 
* Chrome
* Microsoft Edge

Phones tested: 
* Huawei P20Lite
* iPhone 6
* Xaomi Mi 9

* Site also tested with Chrome's built in 'Inspect Element' preview panes simulating the iPad Pro, iPad, iPhone X, iPhone 6/7/8 plus, iPhone 6/7/8, iPhone 5 SE, Pixel 2 XL, Pixel 2 and Galaxy S5
* JS and jQuery code tested on <a href="https://www.repl.it" target="_blank">ReplIt</a>
* Entire site tested extensively with console log and print() - once functions/routes were found to be working as intended console.log and print() commands were removed
* All inter-site links tested on all pages across devices and found to be working
* All outward links directed at other sites tested and found to be working and opening in a new tab
* While watching the console log in real time, no major errors were found across the site

# Bugs

**Major Bugs**
* 

# Deployment

* This project and all project files are hosted on GitHub via my GitHub repository at <a href="https://github.com/Jays-T/photography_philosophy_v1" target="_blank"></a>
* I coded the project using GitPod as my development environment. 
* This project is also hosted and deployed with Heroku
* To deploy the project using Heroku
   1. Register an account at <a href="https://heroku.com" target="_blank">Heroku</a>
   2. Go to Heroku site, login and create a new app. Set a name for this app and select the closest region.
   3. In the Deploy tab of your App dashboard in Heroku, choose Deployment method. I chose Heroku Git, using Heroku CLI and logged in via the terminal using the command: heroku login
   4. In GitPod, create a requirements.txt file using the command pip3 freeze > requirements.txt in the terminal.
   5. Create a Procfile using the commant echo web: python app.py > Procfile in the terminal.
   6. Login to Heroku via the terminal using command heroku login
   7. Commit your changes using: git add and git commit -m "commit message here"
   7. Push your changes using: git push heroku master
   8. In your Heroku Dashboard, Go to the Settings of your app and then Reveal Config Vars and set the values as follows (remove the spaces and '<'>'from the MONGO_URI):

   | KEY         | VALUE                                                                                         |
   | :---        | :---                                                                                          |
   | IP          | 0.0.0.0                                                                                       | 
   | PORT        | 5000                                                                                          |
   | MONGO_URI   | mongodb+srv://root:< your password >@cluster0-r5ils.mongodb.net/< your dbname >               |
   |             | ?retryWrites=true&w=majority                                                                  |
   | SECRET_KEY  | <your_secret_key>                                                                             |
   
   9. From Heroku you can now click 'Open App'. If all steps were completed correctly the app should run successfully
   10. You can also access your app using this url type:  https://<your app name>.herokuapp.com/<endpoint>


## There are no differences between the currently deployed site and the development version at this time.

## To run the project locally

To clone this project from GitHub:

* Under the repository name, click "Clone or download".
  1. In the Clone with HTTPs section, copy the clone URL for the repository ( For this repository: https://github.com/Jays-T/photography_philosophy_v1.git ).
  2. In your local IDE open Git Bash.
  3. Change the current working directory to the location where you want the cloned directory to be made.
  4. Type git clone, and then paste the URL you copied in Step 3.
  5. The command should look like this:  git clone https://github.com/Jays-T/the-band-room.git
  6. Press enter and your local clone will be created and the response should be something like this:
> * $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> * Cloning into `Spoon-Knife`...
> * remote: Counting objects: 10, done.
> * remote: Compressing objects: 100% (8/8), done.
> * remove: Total 10 (delta 1), reused 10 (delta 1)
> * Unpacking objects: 100% (10/10), done.
* For further reading and troubleshooting on cloning a repository from GitHub you can go <a href="https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository" target="_blank">here</a>.

  7. Technologies to install

# To preview in your browser

If you are using gitpod as your IDE:
The project runs only from the Master branch the main directory of which is:  /workspace/the-band-room
When in the main directory enter the following into the terminal command prompt
1. python3 manage.py runserver
2. This will run the contents of the directory on a local web server, on port 8080.
3. If you are working in Gitpod this will give you an option to 'open browser' which will open the default route '/' and load the landing page
4. If you want to stop the local server from running, in the command prompt simply press crtl + C


# Credits

**Code**

* Major credits go to <a href="https://github.com/ckz8780" target="_blank">Chris Zielinski</a> and the <a href="https://github.com/ckz8780/boutique_ado_v1" target="_blank">Boutique Ado Project</a>
* I referred to the above project many times during this process


## Content

* Text on the site was written by myself

## Media

* All images on the site taken by and are property of Lanthus Clark and his person. 
* The <a href="https://realfavicongenerator.net/favicon" target="_blank">favicon generator</a> used for favicon

## Acknowledgements

## Thank you to my mentor **@rheyannmagcalas_mentor** for her advice given througout my journey with Code Institute
## Thank you to Niel from StudentCare at Code Institute for his advice on CRUD functionality and making sure the basics are done right.
## Thank you to h4xnoodle for your advice and consistently reminding me not to overcomplicate things.

## Thank you to all the staff at Code Institute - From the instructors to the mentors, the people in slack who give of their time each day to help and advise us who are learning,
## to those creating the course material to those crafting the UX to those constructing and developing the backend. Thank you so much!

# FAIR-USE COPYRIGHT DISCLAIMER

* This version is for educational use.