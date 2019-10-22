from django.test import TestCase
from .models import Image,Comment,Profile
from django.contrib.auth.models import User
# Create your tests here.

class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        
        self.user=User.objects.create(id=1,username='stacy')
        self.profile=Profile.objects.create(id=1,bio='hello',profile_photo='IMG-20181015-WA0007-1.jpg',user=self.user)
        self.dog=Image(id=1,image_name='dog',image_caption='hello',comments='commented by me',likes='1',user=self.user)
       

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.dog,Image))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.user,User))


    def test_save_method(self):
        self.dog.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete(self):
        self.dog.save_image()
        image=Image.objects.filter(image_name="dog").first()
        delete=Image.objects.filter(id=image.id).delete()
        images=Image.objects.all()
        print(images)
        self.assertTrue(len(images)==0) 

    def test_display(self):
        self.dog.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)==1)

class ProfileTestClass(TestCase):
    def setUp(self):

        self.user=User.objects.create(id=1,username='stacy')
        self.profile=Profile.objects.create(id=2,bio='hello',profile_photo='IMG-20181015-WA0007-1.jpg',user=self.user)

    #testing instance
    def test_instance(self):
        
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.user,User))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_display(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==1)

    def test_delete(self):
        self.profile.save_profile()
        profile=Profile.objects.filter(bio="hello").first()
        delete=Profile.objects.filter(id=profile.id).delete()
        profiles=Profile.objects.all()
        print(profiles)
        self.assertTrue(len(profiles)==0) 
             

class CommentTestClass(TestCase):
    def setUp(self):
        self.user=User.objects.create(id=1,username='stacy')
        self.dog=Image.objects.create(id=1,image_name='dog',image_caption='hello',comments='commented by me',likes='1',user=self.user)
        self.comment=Comment.objects.create(feedback='hello',user=self.user,image=self.dog)
       
    def test_instance(self):
        
        self.assertTrue(isinstance(self.comment,Comment))
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.dog,Image))

    def test_display(self):
        self.comment.save_comment()
        comments=Comment.objects.all()
        self.assertTrue(len(comments)==1)

    def test_delete(self):
        self.comment.save_comment()
        comment=Comment.objects.filter(feedback="hello").first()
        delete=Comment.objects.filter(id=comment.id).delete()
        comments=Comment.objects.all()
        print(comments)
        self.assertTrue(len(comments)==0) 
         
         
