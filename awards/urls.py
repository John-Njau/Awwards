from django.urls import path, re_path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf import settings
# from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('profile/<int:profileId>', views.profile, name='profile'),
    # path('update/profile/<int:profileId>', views.updateprofile, name='updateprofile'),
    path('profile/', views.profile, name='profile'),
    path('update/profile/', views.updateprofile, name='updateprofile'),
    path('project/details/', views.project_details, name='project_details'),
    path('upload/new', views.upload_project, name='upload_project'),
    path('add/review/<int:profileId>', views.add_review, name='add_review'),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)