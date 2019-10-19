from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

    

class Profile(models.Model):
    # bio= models.CharField(max_length =30,null=True)
    bio= HTMLField()
    profile_photo=models.ImageField(upload_to ='photos/',null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()     

    def update_profile(self):
        self.update()
        
    @classmethod
    def search_by_profile(cls,username):
        certain_user = cls.objects.filter(user_id__username__icontains=username)
        # profile = Profile.objects.filter(user__username__icontains=name)
        return  certain_user     

class Image(models.Model):
    image = models.ImageField(upload_to ='images/',null=True)
    image_name= models.CharField(max_length =30)
    image_caption= models.CharField(max_length =30,null=True)
    likes= models.IntegerField(null=True)
    comments= models.CharField(max_length =30,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)


    def __str__(self):
        return self.image_caption

    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()
    

    
    def update_caption(self):
        caption=self.image_caption.update()
        return caption    



class Comment(models.Model):
    feedback= models.CharField(max_length =30,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
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