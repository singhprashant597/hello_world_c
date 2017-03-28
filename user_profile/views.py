from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from home_and_login.models import user_details

# Create your views here.


def requested_owner_profile(request, requested_profile_user_id):
    print("in func: " + str(requested_profile_user_id))
    fetched_values = user_details.objects.filter(user_id=requested_profile_user_id).values_list(
        'intro', 'full_name', 'photo_link', 'followers_total')
    # work = company.objects.filter(
    #     user_work__user_id=requested_profile_user_id, user_work__rank='1').values_list('name', flat=True)
    # if not work:
    #     print("yeahsss")
    # profession_name = profession.objects.filter(
    #     user_work__user_id=requested_profile_user_id, user_work__rank='1').values_list('name', flat=True)
    # return render(request, 'user_profile/owner_user_profile.html',
    # {'full_name': fetched_values[0][1], 'photo_link': fetched_values[0][2],
    # 'followers_total': fetched_values[0][3], 'circle_total':
    # fetched_values[0][4], 'desc': fetched_values[0][0], 'profession_name':
    # profession_name, 'work': work})
    print(fetched_values[0][2])
    return render(request, 'user_profile/owner_user_profile.html',  {'intro': fetched_values[0][0], 'full_name': fetched_values[0][1], 'photo_link': fetched_values[0][2], 'followers_total':fetched_values[0][3]})


def show_user_profile(request, requested_profile_link):
    print(requested_profile_link)
    requested_profile_user_id = user_details.objects.filter(
        profile_link=requested_profile_link).values_list('user_id')
    if not requested_profile_user_id:
        return HttpResponse("Profile not found")
    else:
        requested_by_user_id = request.user.id
        if requested_by_user_id == requested_profile_user_id[0][0]:
            print("same")
            return requested_owner_profile(request, requested_profile_user_id)
        fetched_values = user_details.objects.filter(user_id=requested_profile_user_id).values_list(
            'intro', 'full_name', 'photo_link', 'followers_total')
    # return HttpResponse("Showing profile for " + fetched_values[0][1])
    print(fetched_values[0][2])
    return render(request, 'user_profile/user_profile.html',  {'intro': fetched_values[0][0], 'full_name': fetched_values[0][1], 'photo_link': fetched_values[0][2], 'followers_total':fetched_values[0][3]})
