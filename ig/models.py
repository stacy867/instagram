from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    

class Profile(models.Model):
    bio= models.CharField(max_length =30,null=True)
    profile_photo=models.ImageField(upload_to ='photos/',null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()     

    def update_profile(self):
        self.update() 

class Image(models.Model):
    image = models.ImageField(upload_to ='images/',null=True)
    image_name= models.CharField(max_length =30)
    image_caption= models.CharField(max_length =30,null=True)
    likes= models.IntegerField()
    comments= models.CharField(max_length =30,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)


    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()
    

    
    def update_caption(self):
        caption=self.image_caption.update()
        return caption    



class Comment(models.Model):
    feedback= models.CharField(max_length =30,null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,null=True)

    def __str__(self):
        return self.feedback

    
    def save_comment(self):
        self.save()  

    def delete_comment(self):
        self.delete()

    def update_comment(self):
        self.update()           

class Follow(models.Model):
    profile= models.ForeignKey(Profile,null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.profile          