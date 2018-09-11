from django.shortcuts import render, redirect
from profiles.models import Profile

# Create your views here.

def index(request):
	return render(request, "index.html", {"profiles":Profile.objects.all(), "current_profile":get_logged_in(request)})

def show(request, profile_id):

	profiles = Profile.objects.get(id=profile_id)

	# To the render function we can pass a dictionary to be accessed in the html
	return render(request, "profiles.html", {"profiles" : profiles})

def invite(request, profile_id):
	invited_profile = Profile.objects.get(id=profile_id)
	logged_in_profile = get_logged_in(request)
	logged_in_profile.invite(invited_profile)
	return redirect('index')

	
def get_logged_in(request):
	return Profile.objects.get(id=1)