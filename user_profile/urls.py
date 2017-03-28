from django.conf.urls import url
from . import views

urlpatterns = [
   	url(r'^(?P<requested_profile_link>[^/]+)/$', views.show_user_profile),
]
