from django import forms


from tinymce.models import HTMLField

from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, FileInput, URLInput, EmailInput, PasswordInput, NumberInput, DateInput, TimeInput, CheckboxInput, Select, RadioSelect, Textarea


from .models import User, Profile, Project, UserContacts, Reviews


class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=230)
    mobile = forms.CharField(max_length=230, widget=forms.TextInput(attrs={'type': 'number'}))
    address = forms.CharField(max_length=230)
    
    class Meta:
        model = User
        fields = ('full_name','mobile','address','password1', 'password2')
    


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url']
        
        
        widgets ={
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Project Description'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'Project Image'}),
            'url': URLInput(attrs={'class': 'form-control', 'placeholder': 'Project URL'}),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']
        
        widgets ={
            'profile_pic': FileInput(attrs={'class': 'form-control'}),
            'bio': TextInput(attrs={'class': 'form-control', 'placeholder': 'Update Bio'}),
        }
        
class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContacts
        fields = ['phone_no', 'email', 'linkedin', 'github', 'twitter']
        
        widgets ={
            'phone_no': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Update Phone No'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Update Email'}),
            'linkedin': URLInput(attrs={'class': 'form-control', 'placeholder': 'Update LinkedIn'}),
            'github' : URLInput(attrs={'class': 'form-control', 'placeholder': 'Update Github'}),
            'twitter' : URLInput(attrs={'class': 'form-control', 'placeholder': 'Update Twitter'}),
        }


# review form
class ProjectReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['review', 'review_rating']
        
        widgets={
            'review':TextInput(attrs={'class': 'form-control'}),
            'review_rating': TextInput(attrs={'class': 'form-control'})
        }