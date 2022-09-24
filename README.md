# COMP8967-Group-12-AuthApp-assign-1
Create an Authentication app. Use any front-end libraries of your choice (React, Angular, Vue etc.). Create your API. Don’t look at the existing solution. Fulfill user stories below: User story: I can register a new account User story: I can log in User story: I can log in or register with at least one of the following services: Google or Facebook User story: I can sign out User story: I can see my profile details User story: I can edit my details including photo, name, bio, phone, email and password User story: I can upload a new photo or provide an image URL Icon: https://google.github.io/material-design-icons/

### Basic Features of The App
    
* Register – Users can register and create a new profile
* Login - Registered users can login using username and password
* Social Apps Login – Users can login using their GitHub or Google account
* User Profile - Once logged in, users can create and update additional information such as avatar and bio in the profile page
* Update Profile – Users can update their information such as username, email, password, avatar and bio
* Remember me – Cookie Option, users don’t have to provide credentials every time they hit the site
* Forgot Password – Users can easily retrieve their password if they forget it 
* Admin Panel – admin can CRUD users

### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
2. Run the following commands
    * pip install -r requirements.txt
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser
    * python manage.py runserver
   
3. Open a browser and go to http://localhost:8000/

