from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# import project from models
from .models import project

@login_required(login_url='../../')
def add_project_page(request):
	return render(request, 'project/add.html')

@login_required(login_url='../../')
def add_project(request):
	project_title = request.POST['project_title']
	project_type = request.POST['project_type']
	project_desc = request.POST['project_desc']
	user_id_in_action = request.user.id
	project_save = project.objects.create(
            user_id=user_id_in_action, title=project_title, project_type=project_type,description=project_desc,project_link=User.first_name)
	return HttpResponse("Done")