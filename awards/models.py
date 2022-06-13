from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    # created_at = models.DateTimeField(auto_now_add=True)
    
    
    def get_user_projects(self):
        return self.projects.all()
    
    
    def __str__(self):
        return self.user.username
 
# @login_required(login_url='/accounts/login/')   
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

# Project Review


# @login_required(login_url='/accounts/login/')
class Reviews(models.Model):
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
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField(blank=True, null=True)
    design_rating = models.IntegerField( choices=RATING,default=0,blank=True)
    usability_rating = models.IntegerField( choices=RATING,default=0,blank=True)
    content_rating = models.IntegerField( choices=RATING,default=0,blank=True)
    average_rating = models.DecimalField(default=0,blank=True, decimal_places=2, max_digits=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    
    def get_review_rating(self):
        return self.review_rating
        
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name_plural = 'Reviews'

     

# @login_required(login_url='/accounts/login/')
class Ratings(models.Model):
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
        (10,'10'),
    )
     
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    design_rating = models.IntegerField( choices=RATING,default=0,blank=True)
    usability_rating = models.IntegerField( choices=RATING,default=0,blank=True)
    content_rating = models.IntegerField( choices=RATING,default=0,blank=True)
    average_rating = models.DecimalField(default=0,blank=True, decimal_places=2, max_digits=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    
    def save_rating(self, rating):
        self.rating = rating
        self.save()
    
    
    @classmethod
    def get_rating(cls, id):
        ratings = Ratings.objects.filter(project_id=id).all
        return ratings
        
    
    def __str__(self):
        return self.user.username    
    
    
    class Meta:
        verbose_name_plural = 'Ratings'