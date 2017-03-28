from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.add_project_page),
    url(r'^add_final/$', views.add_project),
]
