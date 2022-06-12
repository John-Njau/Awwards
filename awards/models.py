from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

import datetime as dt


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    image = CloudinaryField('Awards/project_images')
    description = HTMLField()
    url = models.URLField(blank=False)
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
    @classmethod
    def search_by_title(cls, search_term):
        results = cls.objects.filter(title__icontains=search_term)
        return results
    
    
    # class Meta:
    #     ordering = ['-uploaded_at']
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('Awards/profiles')
    bio = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
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
    
#  Project review   
#  RATING=[(
#      (1, '1'),
#      (2, '2'),
#      (3, '3'),
#      (4, '4'),
#      (5, '5'),
#  )]

# Product Review
RATING = (
    (1, '1'),
    (2,'2'), 
    (3 ,'3'), 
    (4,'4'),
    (5, '5'),
    (6,'6'),
    (7,'7'),
    (8,'8'),
    (9,'9'),
    (10,'10') 
)
    
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    review = HTMLField()
    review_rating = models.CharField( choices=RATING,max_length=150)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    
    def get_review_rating(self):
        return self.review_rating
        
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name_plural = 'Reviews'
    
    
class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username    
    
    
    class Meta:
        verbose_name_plural = 'Ratings'