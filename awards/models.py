from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/')
    description = models.TextField()
    url = models.URLField(blank=False)
    
    def __str__(self):
        return self.user.username
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='media/profiles/')
    bio = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def get_user_projects(self):
        return self.projects.all()
    
    def __str__(self):
        return self.user.username
    
    
class UserContacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    phone_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255,blank=True,null=True)
    github = models.CharField(max_length=255,blank=True,null=True)
    twitter = models.CharField(max_length=255,blank=True,null=True)
    
    
    class Meta:
        verbose_name_plural = 'User Contacts'
        
        
    def __str__(self):
        return self.user.username
    