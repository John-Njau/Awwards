from django.urls import path, re_path


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/',views.search_results,name='search'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('user/profile/<str:username>/', views.other_user_profile, name='other_user_profile'),
    path('update/profile/<str:username>/', views.updateprofile, name='updateprofile'),
    path('profile/contacts/<int:userId>/', views.contacts, name='contacts'),
    path('upload/project/', views.upload_project, name='upload_project'),
    path('project/details/<int:id>/', views.project_details, name='project_details'),
    path('add/review/<int:projectId>/', views.add_review, name='add_review'),
    # API endpoints
    path('api/project/rating/', views.project_ratings.as_view(), name='project_rating'),
    path('api/project/review/', views.project_reviews.as_view(), name='project_review'),

]
