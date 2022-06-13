from django.urls import path, re_path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf import settings
# from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search',views.search_results,name='search'),
    # path('profile/<int:profileId>', views.profile, name='profile'),
    # path('update/profile/<int:profileId>', views.updateprofile, name='updateprofile'),
    path('profile/<int:userId>', views.profile, name='profile'),
    path('update/profile/<int:userId>', views.updateprofile, name='updateprofile'),
    path('upload/project/', views.upload_project, name='upload_project'),
    path('project/details/<int:id>', views.project_details, name='project_details'),
    path('add/review/<int:projectId>', views.add_review, name='add_review'),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)