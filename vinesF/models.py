# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from unittest.util import _MAX_LENGTH
#from datetime import date
from django.template.defaultfilters import default
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCount, HitCountMixin


# Create your models here.
class videoID(models.Model):
    videoIDs = models.IntegerField()
    def __str__(self): # __unicode__ on Python 2
        return self.videoIDs
    
class video(models.Model, HitCountMixin, ):
    Pra_choice= (
        ('Gn','geneal'),
        ('Af','Africa'),
        ('ot', 'Others'),
    )
    primaryName = models.CharField(max_length=100)
    Origin = models.CharField(max_length=200)
    PreferredAudience =models.CharField(max_length=40, choices= Pra_choice)
    #Date = models.DateField()
    IdNo = models.AutoField(primary_key=True)
    Link = models.URLField(null=True)
    file_path = models.FileField(upload_to='videos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
#     VPath= models.FilePathField(path=settings.MEDIA_ROOT2, null=True)
#     AddPath= models.CharField(max_length=200, null= True)
   # Recents = Date
    #Recent = Recents.extra(order_by = ['-is_recent'])
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')
    

    def __str__(self): # __unicode__ on Python 2
        return self.primaryName
    
    
class viewcounter(models.Model):
    videoId = models.ForeignKey(videoID, on_delete=models.CASCADE)
    NumViews = models.IntegerField(default=0)
    # hit_count_generic = GenericRelation(
    #     HitCount, object_id_field='object_pk',
    #     related_query_name='hit_count_generic_relation')


    def __str__(self): # __unicode__ on Python 2
        return self.viewcounter
    #print videoID
    

class users(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Name")
    login = models.CharField(max_length=25, verbose_name="Login")
    password = models.CharField(max_length=100, verbose_name="Password")
    phone = models.CharField(max_length=14, verbose_name= "Phone", null = False, default=None)
    Birthday = models.DateField(verbose_name="Birthday", null=True, default=None, blank=True)
    Last_connection = models.DateField(verbose_name="Last_connection", null=True, default=None, blank=True)
    email= models.EmailField(verbose_name="Email" )
    date_created = models.DateField(verbose_name="date_created", auto_now_add=True )
    ##Use when requiring creating a hash coded and secured user instance, preferably add to form
    ##new_user

    def __str__(self):
        return self.Name

class UserProfile(models.Model):
    user_auth= models.OneToOneField(User, primary_key= True)
    phone= models.CharField(max_length= 15, verbose_name= "Phone Number", null= True, default=None, blank= True )
    born_date= models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
    last_connexion= models.DateField(verbose_name="Date Of Last Connexion", null= True, blank= True, default= None)
    years_seniority = models.IntegerField(verbose_name="Seniority",default=0)
 
    def __str__(self):
        return self.user_auth.username
    
class Hitbck2bck(models.Model):
    # Lview = models.ForeignKey(video.IdNo) 
    Hitz = models.ForeignKey(video)
    def __str__(self): # __unicode__ on Python 2
        return self.Hitz.primaryName

class minihit(models.Model):
    # Lview = models.ForeignKey(video.IdNo) 
    mhit = models.ForeignKey(video)
    def __str__(self): # __unicode__ on Python 2
        return self.mhit.primaryName


class MostViewed(models.Model):
    MostViewes = models.ForeignKey(viewcounter) 
    def __str__(self): # __unicode__ on Python 2
        return self.MostViewes



class emails(models.Model):

    email= models.EmailField(verbose_name="Email" )

    def __str__(self): # __unicode__ on Python 2
        return self.email
        