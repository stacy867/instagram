# Instagram
## Instagram-App, 21st of October 2019
### By Stacy Murenzi
## Description
Instagram app is a web application where a user is able to create an account and post pictures for other users to like and comment 
## Code scaffolding
Run python3.6 manage.py runserver when you want to implement the features of the landing pages and other pages.
## BDD
### Behaviour
We want our application to:
1.Sign in to the application to start using and sign up if you do not have an account.
2.Upload images for others to view.
3.See my profile with all the images i posted ,username and bio.
4.Follow other users and see their images on my timeline.
5.Like an image and leave a comment on it.
## Inputs
1.search users by profile names.
2.Create a profile,registering,log in,leave a comment,etc
## Output 
1.Viewing posts other users have created
2.Viewing comments users has posted
3.Viewing likes of an image
## TDD
I test my project using Python3.6 manage.py test insta(my app-name).
## Setup/Installation Requirements
1.Your application should be accessible to users on both desktop and mobile formats. You must ensure that your application is responsive to different screen sizes.
2.Your application should have a clean, simple, well-organized user interface. Ensure you choose a consistent colour scheme and use appropriate fonts for your application. Also, you MUST create a mockup design for your application before you begin development.
3.Your Project should contain an Image model with the following properties:
a.Image
b.Image Name.
c.Image Caption.
d.Profile Foreign key
e.Likes
f.Comments
4.Create the Profile model with the following properties:
a.Profile Photo
b.Bio
5.Your Image model should contain at least the following methods:
a.save_image() - Save an image to the database.
b.delete_image() - Delete image from the database.
c.update_caption() - Update image caption in the database.
6.You should write tests for each of these methods and make sure you implement error handlers to prevent your application from crashing.
7.our project must have a search form that when submitted calls a search function in the view function and redirects to a search results page.
8.Your application should have a solid authentication system that allows users to sign in or register into the application before using it. When a user registers with your application they should receive a confirmation email.
## Technology used
Python3.6
Django
Heroku
Bootstrap4
## My link repository on above
## Contact me on stacymurenzi@gmail.com
## Title Licence
Copyright(c)2019 Stacy Murenzi