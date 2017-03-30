from django.db import models
from django.contrib.auth.models import User
import datetime

class project(models.Model):
    project_type_choices = (
        ('Med', 'Medical'),
        ('Lit', 'Literature'),
    )
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 120)
    project_type = models.CharField(
        max_length=200,
        choices=project_type_choices,
        default = 'NO'
    )
    ref_id = models.CharField()
    project_link = models.URLField(default='error.html')
    likes_total = models.IntegerField(default=0)
    comments_total = models.IntegerField(default=0)
    shares_total = models.IntegerField(default=0)
    following_total = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    description = models.TextField()
    #add achievements

    #like model

    class Like(models.Model):
        user = models.ForeignKey(user)
        date_time = models.DateTimeField(auto_now_add=True)

        
#college detail///

class School(models.Model)
 college_name = models.CharField()
 address= models.TextField()
 city= models.CharField()
 total_projects= models.IntegerField(default=0)
 total_users = models.IntegerField(default=0)

#academic_detail//

user_id = 
work_id = 
profession_id = models.TextField()

# work place and profession
class work(models.Model)
company = models.CharField()
city = models.CharField()

class profession(models.Model)
    designation = models.CharField()

 #user profile  
  class stream(models.Model)
  stream_type = ()
  stream_total_user = models.IntegerField(default=0)
  stream_total_project = models.IntegerField(default=0)

  class sub_stream(models.Model)
  sub_stream_name=()
  stream= models.Foreignkey(stream)
  sub_stream_total_user = models.IntegerField(default=0)
  sub_stream_total_project = models.IntegerField(default=0)
