from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.add_project_page),
    url(r'^add_final/$', views.add_project),
    url(r'^project/$', views.add_project),
    url(r'^(?P<requested_user>[-\w]+)/(?P<requested_profile_link>[^/]+)/$', views.show_project),
]
