from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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