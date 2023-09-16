from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from PIL import Image

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email", "password", "password2",)
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email address already exists.")
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",)
        
        
class ProfileUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    
    image = forms.ImageField(label="Image",widget=forms.FileInput(), required=False,error_messages={"invalid":("image files only")})
    
    class Meta:
        model = Profile
        fields =("bio","date_of_birth","image",)
        
    def save(self,*args,**kwargs):
        img = super().save(*args,**kwargs)
        
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('x')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        
        if x and y and w and h:
            image = Image.open(img.image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((300,300),Image.ANTIALIAS)
            resized_image.save(img.image.path)
            
        return img