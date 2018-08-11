from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r"^$", "profiles.views.index"),
	url(r"^profiles/(?P<profile_id>\d+)$", "profiles.views.show")
)
