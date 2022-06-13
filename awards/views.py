from django.db.models.functions import Cast
from django.forms import IntegerField
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.db.models import Avg

from .models import User, Profile, Project, UserContacts, Reviews
from .forms import ProjectForm, UpdateProfileForm, ProjectReviewForm


# Create your views here.
def home(request):
    allprojects = Project.objects.all()
    reviews = Reviews.objects.all()
    context = {
        'projects': allprojects,
        'reviews': reviews
    }
    return render(request, 'main/home.html', context)

# def upload_project(request):
#     return render(request, 'main/upload_project.html')

# def profile(request, profileId):
#     current_user = User.objects.get(pk=profileId)
def profile(request, userId):
    # current_user = request.user.id
    user_projects = Project.objects.filter(pk=userId).first()
    user_profile =Profile.objects.filter(user=userId).first()
    # ind_profile =User.objects.get(pk=current_user)

    context = {
        'profile': user_profile,
        'projects': user_projects
    }
    return render(request, 'profile/profile.html', context)


# def updateprofile(request, profileId):
#     current_user = User.objects.get(pk=profileId)

def updateprofile(request, userId):
    # current_user = request.user
    user_profile =User.objects.get(pk=userId)
    # profile_details = Profile.objects.filter(pk=current_user.id).first()
    profile_details = Profile.objects.filter(user=user_profile).first()
    form = UpdateProfileForm()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        # return redirect('profile', profileId=profile.id)
        return redirect('profile',userId=profile.id)
    
    return render(request, 'profile/updateprofile.html', {'form': form, 'profile':profile_details, 'current_user':user_profile})

# save review  
def add_review(request, projectId):
    project =Project.objects.get(pk=projectId)
    user = request.user
    review =Reviews.objects.create(
        user=user,
        project=project,
        review = request.POST['review'],
        review_rating = request.POST['review_rating']
    )
    
    avg_reviews=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('review_rating'))

    
    data = {
        'user': user.username,
        'review': request.POST['review'],
        'review_rating': request.POST['review_rating']
    }
    
    return JsonResponse({'bool':True, 'data':data, 'avg_reviews':avg_reviews})


def project_details(request, id):
    project = Project.objects.get(id=id)
    reviewForm = ProjectReviewForm()
    # reviews = Reviews.objects.filter(project=id)
    
    # check
    canAdd =True
    reviewCheck =Reviews.objects.filter(project=project, user=request.user).count()
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False
            
    
    # fetch reviews
    reviews = Reviews.objects.filter(project=project)
    
    # fetch average rating for all reviews
    # avg_reviews=Reviews.objects.filter(project=project).annotate(review_rating_int=Cast('review_rating', IntegerField()).aggregate(Avg('review_rating_int')))
    # avg_reviews=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('review_rating'))
    # avg_reviews = Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('review_rating'))

  
    context = {
        'project':project, 
               'form':reviewForm,
               'reviews':reviews,
               'canAdd':canAdd,
            #    'avg_reviews':avg_reviews
               }
    
    return render(request, 'main/project_details.html', context)


def search_results(request):
    if 'query' in request.GET and request.GET['query']:
        search_term = request.GET.get('query')
        searched_query = Project.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search/search.html', {"message": message, "projects": searched_query})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search/search.html', {"message": message})
    
    
    # query = request.GET['query']
    # data = Project.objects.filter(title__icontains=query).order_by('-id')
    # return render(request, 'search/search.html', {'data': data})


def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
    else:
        form = ProjectForm()
        
    return render(request, 'main/upload_project.html', {'form': form})
