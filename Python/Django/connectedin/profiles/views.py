from django.shortcuts import render
from profiles.models import Profile

# Create your views here.

def index(request):
	return render(request, "index.html")

def show(request, profile_id):

	profiles = Profile()

	if (int(profile_id) == 1):
		profiles = Profile(name="Alan Turing", email="alan@turing.com", phone="23071912")
	elif (int(profile_id) == 2):
		profiles = Profile(name="Ada Lovelace", email="ada@lovelace.com", phone="10121815")
	

	# To the render function we can pass a dictionary to be accessed in the html
	return render(request, "profiles.html", {"profiles" : profiles})