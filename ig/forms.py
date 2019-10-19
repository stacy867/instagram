from .models import Image,Profile,Comment
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name','comments','profile','likes', 'user']
        # widgets = {
        #     'likes': forms.CheckboxSelectMultiple(),
        # }

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id_id']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image']        
        