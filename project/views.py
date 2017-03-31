from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from home_and_login.models import user_details
from project.models import project
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.defaultfilters import slugify
# import project from models
from .models import project


@login_required(login_url='../../')
def add_project_page(request):
    return render(request, 'project/add.html', {'form_file_upload':form_file_upload})


@login_required(login_url='../../')
def add_project(request):
    project_title = request.POST['project_title']
    project_type = request.POST['project_type']
    project_desc = request.POST['project_desc']
    user_profile_link = user_details.objects.filter(
        user_id=request.user.id).values_list('profile_link')[0][0]
    slugged_link = user_profile_link + '/' + slugify(project_title)
    user_id_in_action = request.user.id
    project_save = project.objects.create(
        user_id=user_id_in_action, title=project_title, project_type=project_type, description=project_desc, project_link=slugged_link)
    return HttpResponse("Done")


def show_project(request, requested_user, requested_profile_link):
    print(requested_user)
    print(requested_profile_link)
    requested_user_id = user_details.objects.filter(
        profile_link=requested_user).values_list('user_id')[0][0]
    requested_project_link = requested_user+'/'+requested_profile_link
    print(requested_project_link)
    if requested_user_id:
        project_details = project.objects.filter(user_id=requested_user_id, project_link=requested_project_link).values_list(
            'likes_total', 'comments_total', 'shares_total', 'title', 'description')
        if project_details:
            temp_dict = {}
            temp_dict['likes_total'] = project_details[0][1]
            temp_dict['comments_total'] = project_details[0][1]
            temp_dict['shares_total'] = project_details[0][2]
            temp_dict['title'] = project_details[0][3]
            temp_dict['description'] = project_details[0][4]
            one = user_details.objects.filter(user_id=requested_user_id).values_list(
                'full_name', 'profile_link', 'photo_link')
            temp_dict['full_name'] = one[0][0]
            temp_dict['profile_link'] = one[0][1]
            temp_dict['photo_link'] = one[0][2]
            temp_dict['liked'] = 0
            return render(request, 'user_profile/project_page.html',  {'project': temp_dict})
        else:
            return HttpResponse('No project')   