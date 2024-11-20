
# Inspira - Django REST Framework API

This repository is the back-end API which used by my front-end application INSPIRA.
The API includes 2 custom models Profiles and Posts. All API endpoints will serve a specific purpose and will be tested to prevent any errors. 
Logged in users can create/edit/delete posts and comments.

You can rewiew the front-en application here - [Inspira](https://github.com/asyaharoyan/inspira)

## Contents

- [**Entity Relationship Diagram**](#entity-relationship-diagram)
- [**Database**](#database)
- [**Models**](#models)
- [**Testing**](#testing)
  - [**Manual Testing**](#manual-testing)
  - [**PEP8 Validation**](#pep8-validation)
  - [**Bugs Fixed**](#bugs-fixed)
  - [**Bugs Unresolved**](#bugs-unresolved)
- [**Technologies Used**](#technologies-used)
- [**Deployment To Heroku**](#deployment-to-heroku)
- [**Cloning This Project**](#cloning-and-setting-up-this-project)
- [**Credits**](#credits)
  - [**Content**](#content)
  - [**Media**](#media)
- [**Acknowledgments**](#acknowledgements)



# Entity Relationship Diagram

To visualize the connections between the models in the Inspira app, I have created a relationships diagram. This diagram provides a clear representation of how the models **Profiles, Posts, Comments, Followers, and Likes** interact with each other.

![Diagram](documentation/images/relationships-diagram.png)

# Database

# Models

## Profiles model

The Profiles model is a custom model designed for the Inspira app. It stores all relevant information required for designers, architects, and painters to create and manage their professional profiles within the platform.
Each user in the app has a corresponding profile, establishing a one-to-one relationship with the built-in User model.

Relationships:

- One-to-One with the User model.
- One-to-Many with the Post model (a user can create multiple posts).
- Many-to-Many with the Follower model (a user can follow or be followed by others).

![Profiles](documentation/images/profiles.png)

## Post model

The Post model is a custom model specifically designed for the Inspira app. It has been created to store all relevant data for a post, including details related to style, profession, and location, ensuring tailored functionality for the app's unique requirements.

Relationships:

- Many-to-One with the Profiles model (a profile can create multiple posts, but each post belongs to one profile).
- One-to-Many with the Comment model (a post can have multiple comments).
- One-to-Many with the Like model (a post can be liked by multiple users).


![Post](documentation/images/post.png)

## Comment model

The Comment model is a pre-existing model sourced from a functional API. It stores information about the commenter, including their identity, the time the comment was made, and the content of the comment.

Relationships:

- Many-to-One with the Post model (each comment belongs to one post, but a post can have multiple comments).
- Many-to-One with the Profiles model (each comment is made by one profile, but a profile can make multiple comments).

![Comment](documentation/images/comment.png)

## Like model

The Like model is a pre-existing model sourced from a functional API. It is responsible for storing data about users who have liked specific posts, capturing the relationship between users and their liked content.

Relationships:

- Many-to-One with the Post model (a post can be liked by multiple users, but each like is associated with one post).
- Many-to-One with the Profiles model (each like is associated with one profile, but a profile can like multiple posts).

![Like](documentation/images/like.png)

## Follower model

The Follower model is a pre-existing model obtained from a functioning API. It is designed to store and manage data related to user followers, including relationships between users and their followers.

Relationships:

- Many-to-Many with the Profiles model (a profile can follow and be followed by multiple other profiles).

![Follower](documentation/images/follower.png)


# Testing

  ## Manual Testing

  ## PEP8 Validation

  All the code has gone through PREP8 validation. There were a few errors which has been fixed.

  **api-inspira**

  permissions.py

  ![Permissions](documentation/images/api-permissions.png)

  serializers.py

  ![Serializers](documentation/images/api-seializers.png)

  views.py

  ![Views](documentation/images/api-views.png)

  wsgi.py

  ![WSGI](documentation/images/api-wsgi.png)

  
  **comments**

  models.py

  ![Models](documentation/images/comments-models.png)

  serializers.py

  ![Serializers](documentation/images/comments-serializers.png)

  views.py

  ![Views](documentation/images/comments-views.png)


  **followers**

  models.py

  ![Models](documentation/images/followers-models.png)

  serializers.py

  ![Serializers](documentation/images/followers-serializer.png)

  views.py

  ![Views](documentation/images/follower-view.png)


  **likes**

  models.py

  ![Models](documentation/images/likes-models.png)

  serializers.py

  ![Serializers](documentation/images/likes-serializers.png)

  views.py

  ![Views](documentation/images/likes-views.png)


  **posts**

  models.py

  ![Models](documentation/images/post-models.png)

  serializers.py

  ![Serializers](documentation/images/post-serializers.png)

  views.py

  ![Views](documentation/images/post-views.png)


  **profiles**

  models.py

  ![Models](documentation/images/profiles-models.png)

  serializers.py

  ![Serializers](documentation/images/profiles-serializers.png)

  views.py

  ![Views](documentation/images/profiles-views.png)


  ## Bugs Fixed
  

  ## Bugs Unresolved

  There are no unresolved bugs.

# Technologies Used

In this project has been used **Python** programming language, **Django** framework and **Django REST** framework. 

# Deployment To Heroku

The project was deployed to Heroku. The deployment process is as follows:

Firstly we need to create a new repository in GitHub where our project files will be located.

Once the repository has been crated, it has been pulled to GitPod.

Now it's time to install Django and some additional packages

 - Install Django by typing pip install 'django<4'
 - Create our new project by typing django-admin startproject drf_api_deployment_process .
 - Install cloudinary storage by typing pip install django-cloudinary-storage
 - Install Pillow by typing pip install Pillow

Now we need to add our newly installed apps to our settings.py file

# Cloning This Project

# Credits

  ## Content

  ## Media

# Acknowledgments

