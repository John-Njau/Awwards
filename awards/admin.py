from django.contrib import admin

from .models import Project, Profile, UserContacts, Ratings, Reviews

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(UserContacts)

admin.site.register(Ratings)

class ReviewAdmin(admin.ModelAdmin):
    list_display= ('user', 'project', 'review', 'get_usability_rating','get_design_rating','get_content_rating', 'get_average_rating')
admin.site.register(Reviews, ReviewAdmin)
