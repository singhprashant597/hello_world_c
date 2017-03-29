from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import F

from home_and_login.models import user_details
from project.models import project
from .models import following_user

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
    return render(request, 'user_profile/owner_user_profile.html',  {'intro': fetched_values[0][0], 'full_name': fetched_values[0][1], 'photo_link': fetched_values[0][2], 'followers_total': fetched_values[0][3]})


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
        # check if following
        following = following_user.objects.filter(
            user_id=requested_profile_user_id, follower_id=requested_by_user_id)
        if not following:
            is_following = False
        else:
            is_following = True
    # return HttpResponse("Showing profile for " + fetched_values[0][1])
    print(fetched_values[0][2])
    return render(request, 'user_profile/user_profile.html',  {'intro': fetched_values[0][0], 'full_name': fetched_values[0][1], 'photo_link': fetched_values[0][2], 'followers_total': fetched_values[0][3], 'is_following': is_following})


def add_follower_to_user(request):
    print('Here')
    url_user = request.POST['url_user']
    # do the following with regular expressions
    for index in range(-2, -len(url_user), -1):
        if url_user[index] == '/':
            profile_link = url_user[index+1:-1]
            break
    user_id_in_action = request.user.id
    user_id_to_follow = user_details.objects.filter(
        profile_link=profile_link).values_list('user_id', flat='True')
    print(user_id_to_follow)
    following_user.objects.create(
        follower_id=user_id_in_action, user_id=user_id_to_follow[0])
    user_details.objects.filter(user_id=user_id_to_follow).update(
        followers_total=F('followers_total') + 1)
    user_details.objects.filter(user_id=user_id_in_action).update(
        following_total=F('following_total') + 1)
    user_id_to_follow_followers = user_details.objects.filter(
        user_id=user_id_to_follow).values_list('followers_total', flat=True)
    return JsonResponse({'total': user_id_to_follow_followers[0]})


def create_feed(request):
    user_id_in_action = request.user.id
    feed_posts = {}
    following_id_list = following_user.objects.filter(
        follower_id=user_id_in_action).values_list('user_id')
    if following_id_list:
        for user_id in following_id_list:
            print("sab thik")
            from project.models import project
            user_project_list = project.objects.filter(user_id=user_id)
            if user_project_list:
                for project in user_project_list:
                    temp_dict = {}
                    temp_dict['likes_total'] = project.likes_total
                    temp_dict['comments_total'] = project.comments_total
                    temp_dict['shares_total'] = project.shares_total
                    temp_dict['title'] = project.title
                    temp_dict['description'] = project.description
                    one = user_details.objects.filter(user_id=user_id).values_list(
                        'full_name', 'profile_link', 'photo_link')
                    temp_dict['full_name'] = one[0][0]
                    temp_dict['profile_link'] = one[0][1]
                    temp_dict['photo_link'] = one[0][2]
                    temp_dict['liked'] = 0
                    feed_posts['post: ' + str(project.id)] = temp_dict
    print("sending now ")
    return JsonResponse(feed_posts)


def owner_profile_feed(request, requested_profile_user_id):
    user_id_in_action = request.user.id
    feed_posts = {}
    from project.models import project
    user_project_list = project.objects.filter(user_id=user_id_in_action)
    if user_project_list:
        for project in user_project_list:
            temp_dict = {}
            temp_dict['likes_total'] = project.likes_total
            temp_dict['comments_total'] = project.comments_total
            temp_dict['shares_total'] = project.shares_total
            temp_dict['title'] = project.title
            temp_dict['description'] = project.description
            #change getting user_meta multiple times
            one = user_details.objects.filter(user_id=user_id_in_action).values_list(
                'full_name', 'profile_link', 'photo_link')
            temp_dict['full_name'] = one[0][0]
            temp_dict['profile_link'] = one[0][1]
            temp_dict['photo_link'] = one[0][2]
            temp_dict['liked'] = 0
            feed_posts['post: ' + str(project.id)] = temp_dict
    print("sending now ")
    return JsonResponse(feed_posts)


def user_profile_feed(request, requested_profile_link):
    print('YO' + requested_profile_link)
    requested_profile_user_id = user_details.objects.filter(
        profile_link=requested_profile_link).values_list('user_id')
    if not requested_profile_user_id:
        return HttpResponse("Profile not found")
    else:
        requested_by_user_id = request.user.id
        if requested_by_user_id == requested_profile_user_id[0][0]:
            print("same")
            return owner_profile_feed(request, requested_profile_user_id)
