from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.db.models import Avg


from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import ReviewSerializer, RatingsSerializer
from .models import User, Profile, Project, UserContacts, Reviews, Ratings
from .forms import ProjectForm, UpdateProfileForm, ProjectReviewForm, UserContactForm


# Create your views here.
def home(request):
    allprojects = Project.objects.all()
    reviews = Reviews.objects.all()
    
    
    context = {
        'projects': allprojects,
        'reviews': reviews,
        
    }
    return render(request, 'main/home.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    context = {
        'user': user,
       
    }
    
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/accounts/login/')
def other_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_projects = Project.objects.filter(user=user)

    context = {
        'user': user,
        'project': user_projects,
    }
    
    return render(request, 'profile/user_profile.html', context)

    
    
@login_required(login_url='/accounts/login/')
def updateprofile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = Profile.objects.get(id=user.id)
    
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile', username)
    
    else:
        form = UpdateProfileForm()

    return render(request, 'profile/updateprofile.html',
                  {'form': form, 
                   'profile': user_profile, 
                   'current_user': user_profile})

    # user = get_object_or_404(User, username=username)
    # user_profile =Project.objects.get(id=user.id)

    # if request.method == 'POST':
    #     form = UpdateProfileForm(request.POST, request.FILES, instance=user_profile)
        
    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         profile.user = user
    #         profile.save()
    #     return redirect('profile',username)
    
    # else:
    #     form = UpdateProfileForm()
        
        
    # context = {
    #     'form': form, 
    #     'profile':user_profile, 
        
    # }
    
    # return render(request, 'profile/updateprofile.html', context)


# save review  
def add_review(request, projectId):
    project =Project.objects.get(pk=projectId)
    user = request.user
    review =Reviews.objects.create(
        user=user,
        project=project,
        review = request.POST['review'],
        usability_rating = request.POST['usability_rating'],
        content_rating = request.POST['content_rating'],
        design_rating = request.POST['design_rating'],
        
    )
    
    avg_usability=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('usability_rating'))
    avg_content=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('content_rating'))
    avg_design=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('design_rating'))
    # avg_ratings=(avg_usability + avg_content + avg_design)/3


    
    data = {
        'user': user.username,
        'review': request.POST['review'],
        'usability_rating' : request.POST['usability_rating'],
        'content_rating' : request.POST['content_rating'],
        'design_rating' : request.POST['design_rating'],
        
    }
    
    return JsonResponse({'bool':True, 'data':data})

@login_required(login_url='/accounts/login/')
def project_details(request, id):
    project = Project.objects.get(id=id)
    reviewForm = ProjectReviewForm()
    
    # check
    canAdd =True
    reviewCheck =Reviews.objects.filter(project=project, user=request.user).count()
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False
            
    
    # fetch reviews
    reviews = Reviews.objects.filter(project=project)
    
    # fetch average rating for all reviews
    avg_usability=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('usability_rating'))
    avg_content=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('content_rating'))
    avg_design=Reviews.objects.filter(project=project).aggregate(avg_rating=Avg('design_rating'))

  
    context = {
            'project':project, 
            'form':reviewForm,
            'reviews':reviews,
            'canAdd':canAdd,
            
            'avg_content':avg_content,
            'avg_usability':avg_usability,
            'avg_design':avg_design,
           
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

@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def contacts(request, userId):
    user = User.objects.get(pk=userId)
    user_contacts = UserContacts.objects.get(id=user.id)
    
    if request.method == 'POST':
        form = UserContactForm(request.POST, request.FILES)
        
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = user
            contact.save()
        return redirect('profile', user.username)
    
    else:
        form = UserContactForm()
    
    context = {
        'contacts': contacts,
        'form': form,
        'user': user
    }
    
    return render(request, 'profile/contact-info.html', context)

# API views

class project_ratings(APIView):
    def get(self, request, format=None):
        all_ratings = Ratings.objects.all()
        serializers = RatingsSerializer(all_ratings, many=True)
        return Response(serializers.data)
    
    
    def post(self, request, format=None):
        serializers = RatingsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class project_reviews(APIView):
    def get(self, request, format=None):
        all_reviews = Reviews.objects.all()
        serializers = ReviewSerializer(all_reviews, many=True)
        return Response(serializers.data)
    
    
    def post(self, request, format=None):
        serializers = ReviewSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)