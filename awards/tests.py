from django.test import TestCase

from .models import Profile, Project, UserContacts, Reviews


class ProfileTestClass(TestCase):
    '''
    
    '''
    def setUp(self):
        self.profile = Profile(user_id='1',profile_pic='profile_pic.jpg', bio='bio')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Project.objects.all()
        self.assert_True(len(profiles) > 0)


class ProjectTestClass(TestCase):
    ''''''
    def setUp(self):
        self.profile = Profile(profile_pic='profile_pic.jpg', bio='bio')
        self.profile.save()
        
        self.project = Project(title='title', description='description', user=self.profile)
        self.project.save()
        
    
    def tearDown(self):
        Profile.objects.all().delete()
        
        
    def test_search_by_title(self):
        self.project.save()
        projects = Project.search_by_title('title')
        self.assertTrue(len(projects) > 0)
    

class ReviewsTestClass(TestCase):
    pass



class UserContactsTestClass(TestCase):
    pass