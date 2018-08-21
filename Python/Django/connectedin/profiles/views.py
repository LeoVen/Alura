from django.shortcuts import render
from profiles.models import Profile

# Create your views here.

def index(request):
	return render(request, "index.html", {"profiles":Profile.objects.all()})

def show(request, profile_id):

	profiles = Profile.objects.get(id=profile_id)

	# To the render function we can pass a dictionary to be accessed in the html
	return render(request, "profiles.html", {"profiles" : profiles})