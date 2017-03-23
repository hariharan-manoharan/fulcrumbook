from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileForm


# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request, template, context)

@login_required
def userProfile(request):
	user = request.user
	context = {'user': user, 'template': 'userTimeline'}
	template = 'profile.html'
	return render(request, template, context)


@login_required
def userTimeline(request):
	user = request.user
	context = {'user': user, 'template': 'userTimeline'}
	template = 'profile.html'
	return render(request, template, context)


@login_required
def userGallery(request):
	user = request.user
	context = {'user': user, 'template': 'userGallery'}
	template = 'profile.html'
	return render(request, template, context)

@login_required
def userProfile_update(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')

    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    return render(request, 'updateProfile.html', context=locals())



