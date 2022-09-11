<h1 align="center">Kettlebellion Website</h1>

[View the live project here.](https://kettlebellion.herokuapp.com)

This is the website about kettlebell workouts. It is designed to bring kettlebell enthusiasts together and provide them with the platform where they can share their favourite workouts.

<h2 align="center"><img src=""></h2>

## Table of Content
 
  * [Design](#design)
    + [Colour Sceme](#colour-scheme)
    + [Typography](#typography)
    + [Imagery](#imagery)
  
  * [User Stories](#user-stories)
    + [Admin](#admin)
    + [First Time Visitor](#first-time-visitor)
    + [Registered Visitor](#registered-visitor)

  * [Code Validation](#code-validation)
    + [PEP8 apps.py](#pep8-appspy)
    + [PEP8 forms.py](#pep8-formspy)
    + [PEP8 models.py](#pep8-modelspy)
    + [PEP8 urls.py](#pep8-urlspy)

  * [Manual Testing](#manual-testing)

  * [Bugs](#bugs)

  * [Deployment](#deployment)
    + [Deploying on Heroku](#deploying-on-heroku)

  * [Future Features](#future-features)

  * [Technologies Used](#technologies-used)

  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)


-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are  dark grey, and white.
    -   #### Typography
        -   The Goudy Bookletter font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Montserrat is a clean font that it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is important. The large hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.
    
    <p align="right">(<a href="#table-of-content">back to top</a>)</p>


-    ### User Stories

     #### Admin

        1. As an Admin I want to navigate the admin panel so that I can create, read, update and delete the content.

     #### First Time Visitor

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.

        2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content I am interested in.

        3. As a First Time Visitor, I want to sign up for an account so that I can contribute to the community.

     #### Registered Visitor

        1. As a Registered Visitor, I want to login/logout so that I can have the right create, edit and delete my posts.

        2. As a Registered Visitor, I want to like other registered users' posts so that the most popular posts can get noticed.

     <p align="right">(<a href="#table-of-content">back to top</a>)</p>

-   ### Code Validation

    #### W3C HTML Validation

    #### W3C CSS Validation

    ![Image](static/media/readme_imgs/CSS_validation.png)

    #### PEP8 views.py

    ![Image](static/media/readme_imgs/pep8_views.png)

    #### PEP8 apps.py

    ![Image](static/media/readme_imgs/pep8_apps.png)

    #### PEP8 forms.py

    ![Image](static/media/readme_imgs/pep8_forms.png)

    #### PEP8 models.py

    ![Image](static/media/readme_imgs/pep8_models.png)

    #### PEP8 urls.py

    ![Image](static/media/readme_imgs/pep8_urls.png)

-   ### Manual Testing

    -   #### Registration Form

        Message alert appears if password is too short or username is duplicated.

        ![Image](static/media/readme_imgs/password_accountname.png)


        <p align="right">(<a href="#table-of-content">back to top</a>)</p>

    -   #### Login Form

        The username and password must be identical to the data used during registration of account.

        ![image](static/media/readme_imgs/login_input.png)

    -   #### Admin Form

        The username and password must be identical to the data used during registration of account.

        ![image](static/media/readme_imgs/admin_input.png)

    <p align="right">(<a href="#table-of-content">back to top</a>)</p>

    -   #### Admin Approval

        Admin can approve new workouts by selecting drafts and publishing them.

        ![image](static/media/readme_imgs/admin_approve_draft.png)

        ![image](static/media/readme_imgs/admin_approve_publish.png)

        Admin can appove new comments by using dropdown menu option.

        ![image](static/media/readme_imgs/comments_approval1.png)

        ![image](static/media/readme_imgs/comments_approval2.png)

    -   #### Confirmation Messages

        Upon user login/logout or workout/comment submission/update/deletion confirmation messages appear accordingly.

        ![image](static/media/readme_imgs/login_success.png)

        ![image](static/media/readme_imgs/logout_success.png)

        ![image](static/media/readme_imgs/update_success.png)

        ![image](static/media/readme_imgs/delete_success.png)

        ![image](static/media/readme_imgs/comment_awaiting.png)


    -   ##### Warning Messages

        New workout title must be unique, otherwise an alert message appears with an explanation on what caused the error.

        ![image](static/media/readme_imgs/already_exists.png)

    
    <p align="right">(<a href="#table-of-content">back to top</a>)</p>

-   ### Further Testing

    -   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
    -   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
    -   A large amount of testing was done to ensure that all pages were linking correctly.
    -   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

    The W3C Markup Validator, W3C CSS Validator. Lighthouse and Am I Responsive Services were used to validate every page of the project to ensure there were no syntax errors in the project.

    ![image](static/media/readme_imgs/lighthouse_result2.png)

    ![image](static/media/readme_imgs/CSS_validation.png)

    ![image](static/media/readme_imgs/comment_awaiting.png)

    ![image](static/media/readme_imgs/comment_awaiting.png)


-   ### Bugs

    -   During the early deployment an error occurred in the application and the webpage could not be served. The application logs showed error code H10. 
        1. This was solved by correcting a typing error in Heroku app name (ketllebelllion instead of ketllebellion).
        2. Further debugging also revealed wrong folder name in Procfile (kettlebellion-blog instead of kettlebellion).
        3. During the debugging DEBUG flag was changed to False caused by confusion, but changed to True again until the day of the production deployment.

    -   When creating my first view the website pages did not render and TemplateDoesNotExist at/ error was showing.
        - This was solved by fixing the path in setting.py by changing  TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') to TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates/blog').
    -   CSS file did not render for django-allauth login.html which was solved by installing ```pip install django-bootstrap5```.

     <p align="right">(<a href="#table-of-content">back to top</a>)</p>

-   ###  Deployment

    -   This project was developed using [GitPod](https://gitpod.io/ "GitPod") - an open-source developer platform. The code was tracked by [Git](https://git-scm.com/ "Git") - open-source distributed version control system, and hosted at [GitHub](https://github.com/ "Link to GitHub") - code hosting platfrom for version control and collaboration. 

    -   #### Deploying on Heroku
    To deploy this page to Heroku from its GitHub repository, the following steps were taken:

    1. Create Heroku App:
        - Click "New" tab in the dashboard and choose "Create new app" from dropdown menu.
        - Type your app name and select the location.

    2. Attach the PostgreSQL database, Cloudinary API and PORT 8000 for improved compatibility with various Python libraries:
        - Click "Resources" tab in the app dashboard menu and search for Heroku Postgres in the "Add-ons" bar.
        - Click "Settings" tab in the app dashboard menu, click "Reveal Config Vars" and copy the string value for DATABASE_URL key. Click "Add".
        - Type CLOUDINARY_URL in the next KEY field and paste the Cloudinary API Environment Variable in the VALUE field. Click "Add".
        - Type PORT in the next KEY field and 8000 in the VALUE field. Click "Add".

    3. Prepare the environment and settings.py file in Gitpod:
        - Create an env.py file in the same directory where manage.py is located. 
        - In env.py add the DATABASE_URL, SECRET_KEY and CLOUDINARY_URL.
        ``` 
        import os
        os.environ["DATABASE_URL"] = " _here paste the DATABASE_URL key that was copied in step 2_ "
        os.environ["SECRET_KEY"] = " _here create an unique secret key value and copy-paste this secret key value to Heroku "Config Vars" beneath DATABASE_URL created in step 2)_ "
        os.environ["CLOUDINARY_URL"] = " _here paste Cloudinary API Environment Variable provided after registration_ "
        ```
        - Reference env.py in settings.py, replace insecure key with the secret environment variable and  wire up Heroku Postgres database.
        ```
        import os
        import dj_database_url
        if os.path.isfile('env.py'):
            import env

        SECRET_KEY = os.environ.get('SECRET_KEY')
        
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
        ```
        - Link app to Cloudinary in settings.py by adding Cloudinary libraries to INSTALLED_APPS section and by directing Django to Cloudinary for media and static files storage.
        ```
        INSTALLED_APPS = [
            'cloudinary_storage',
            'cloudinary',
        ]

        STATIC_URL = '/static/'
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ```
        - Direct Django to to templates location in settings.py by adding in a templates directory beneath BASE_DIR and by changing ```'DIRS': []``` to ```'DIRS':[TEMPLATES_DIR]``` in TEMPLATES.

        ```
        TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

        ```
        - Add Heroku app name to ALLOWED_HOSTS in settings.py.
        ```
        ALLOWED_HOSTS = ['heroku_app_name.herokuapp.com', 'localhost']
        ```

    4. Create three new directories (media, static, templates) and a new file Procfile next to manage.py in Gitpod.
        - Add 'web: gunicorn app_directory_name.wsgi' to Procfile.
    5. Deploy the project on Heroku using GitHub as the deployment method.
        - Click "Deploy" tab in the app dashboard menu and click GitHub in "Deployment Method" section.
        - Type your GitHub repo name in the search bar and click "Connect".
        - Click "Deploy Branch" in "Manual Deploy" section and wait for the successful deployment message.
        - Click "Open app".
    
    <p align="right">(<a href="#table-of-content">back to top</a>)</p>

-   ### Future Features

    - User profile customization could be added to an account.

    - A contact form could be included

    - A page with instructionals for each move could be included.

-   ### Technologies Used

    - [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - [CSS](https://en.wikipedia.org/wiki/CSS)
    - [JavaScript](https://www.javascript.com/)
    - [Python](https://www.python.org/)
    - [Django](https://www.djangoproject.com/)
    - [Bootstrap](https://getbootstrap.com/)
    - [Heroku](https://www.heroku.com/)
    - [Heroku PostgreSQL](https://www.heroku.com/postgres)
    - [Cloudinary](https://cloudinary.com/?&utm_campaign=1329&utm_content=instapagelogocta-selfservetest)
    - [Summernote](https://summernote.org/)
    - [GitHub](https://github.com/PipedreamHQ/pipedream/tree/master/components/github?gclid=Cj0KCQjw6_CYBhDjARIsABnuSzr60SsXPdtb6AaOdzb493O46pdGVPiO4Df1kNou-G7YzOXujifSNjkaAj6ZEALw_wcB#github-api-integration-platform)
    [GitPod](www.gitpod.io)
    - [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
    - [Am I Responsive](https://ui.dev/amiresponsive)
    - [Google Fonts](https://fonts.google.com/)
    - [Font Awesome](https://fontawesome.com/)
    - [Pep8](http://pep8online.com/)
    - [W3C Markup Validation Service](https://validator.w3.org/)
    - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

    <p align="right">(<a href="#table-of-content">back to top</a>)</p>

-   ### Credits

    -    #### Content

    The code for the admin panel is taken from Code hink Therefore I Blog.

    The code for post modification is taken from GitHub user IrishBecky91's project Student Rations.

    -   #### Media

        -   [Istockphoto](https://www.istockphoto.com) - used to downloag images for free.
        -   [Stack Overflow](www.stackoverflow.com) - used to search for code related errors and bugs.
        -   [Slack](www.slack.com) - is used to connect with fellow coders and ask for help if stuck.

    -   #### Acknowledgements

        -   Code Institute walk through tutorial I Think Therefore I Blog that was the basis for my project.

        -   GitHub user Irishbecky91 whose Student Rations project inspired me to create my blog design.

        -   Django documentation, YouTube tutorials and Stackoverflow were my general references throughout the project.

        -   Tutor support at Code Institute for their support.
    
    <p align="right">(<a href="#table-of-content">back to top</a>)</p>
