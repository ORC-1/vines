# -*- coding: utf-8 -*-
#System libraries
from __future__ import unicode_literals
import datetime
import web
from web.form import notnull

#Django modules

from django.views import generic 
# from django import forms
from .forms import *
from django.template.context_processors import request
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.expressions import OrderBy
from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout #Import for processing Login
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#Home App models
from models import *
# Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Hit Counter
#Search
from simple_search import search_form_factory



# Views.

def index(request):
    Movie = video.objects.all().order_by('-uploaded_at')
   
# Latest section oder first by the most recent, randomize and limit to n...
    Latexn = video.objects.all().order_by("?").order_by('-uploaded_at').order_by("?")[:2]
    Mview = video.objects.all().order_by("?").order_by('-uploaded_at').order_by("?")[:4]

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(Movie, 9)
    try:
        vine = paginator.page(page)
    except PageNotAnInteger:
        vine = paginator.page(1)
    except EmptyPage:
        vine = paginator.page(paginator.num_pages)
    # End of pagination
    
    #Hit counter    
    hitz= Hitbck2bck.objects.select_related('Hitz').all().order_by('-id')[:2]
    minihitz= minihit.objects.select_related('mhit').all()[:4]


    #End of Latest video view section

    #search
#     if request.method == 'GET': # If the form is submitted

#         search_query = request.GET.get('search_box', None)
#         SearchForm = search_form_factory(video.objects.all(),
#                                  ['^title', 'description'])
# # @render(request,'vine/index.html')
#     # def search(request):
#     form = SearchForm(request.GET or {})
#     if form.is_valid():
#         results = form.get_queryset()
#     else:
#         results = MyModel.objects.none()

        
    context = {
        "Mview": Mview,
        "vine": vine,              
        'video': Movie,
        "Latexn": Latexn,
        "hitz": hitz,
        "minihitz":minihitz,
        # 'form': form,
        # 'results': results,
    }

    return render(request, 'vine/index.html', context)


#########################VIEW FOR PROCESSING NewVid###################################
@login_required   
def newvid(request):
    if request.POST:
        form= AddVidForm(request.POST, request.FILES)
        if form.is_valid():            
            form.save()            
            return HttpResponse("New Video added")
        else:
            return render(request,'vine/Newvid.html', {'form':form})
    else:
        form= AddVidForm()
        return render(request,'vine/Newvid.html', {'form':form})
        
#########################End Of VIEW FOR PROCESSING NewVid ################################### 

#########################VIEW FOR PROCESSING email###################################
def emails(request):
    if request.POST:
        form= emailsForm(request.POST)
        if form.is_valid():            
            form.save()            
            return HttpResponse("email added, thank you for subscribing ")
            # time.sleep(3)
            return render(request,'vine/emails.html', {'form':form})

        else:
            return render(request,'vine/emails.html', {'form':form})
    else:
        form = emailsForm()
        return render(request,'vine/emails.html', {'form':form})
        
#########################End Of VIEW FOR PROCESSING NewVid ###################################            
            

    
    
#########################VIEW FOR PROCESSING New User###################################
    
def newuser(request):
    if request.POST:
        form= NewUserForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']  
            login= form.cleaned_data['login']
            password= form.cleaned_data['password']    
            phone= form.cleaned_data['phone']    
            Birthday= form.cleaned_data['Birthday']
            #Last_connection= form.clean_data['Last_connection']
            email= form.cleaned_data['email']
            FreshUser = User.objects.create_user(username = login, email =email, password=password)
            #FreshUser= users(Name=Name, login=login, password=password, phone=phone, Birthday=Birthday, email=email)
            #FreshUser= users(Name=Name, login=login, password=password, phone=phone, Birthday=Birthday, Last_connection=Last_connection, email=email)
            FreshUser.is_active = True    #switch off to enable email verification
            #FreshUser.last_name=Name
            FreshUser.save()
            Fresh= UserProfile(user_auth=FreshUser, phone=phone, Birthday=Birthday )
            Fresh.save()
            #return HttpResponseRedirect(reverse('public_empty'))
            return HttpResponse("New User Added")
        else:
            return render(request, 'vine/NewUser.html', {'form':form})
            
            
    else:
        form= NewUserForm()
        return render(request, 'vine/NewUser.html', {'form':form})

            
#########################END OF VIEW FOR PROCESSING NewUser ###########################################
        
#########################VIEW FOR PROCESSING LOGIN (error 22-01-2018)###################################


##################################################VIEW_FOR_PROCESSING_CONNECTION_FORM##########################################################

def connection(request):
    if request.POST:
        form= Form_connection(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            user= users(Name=username, password=password)
            if user:
                login(request, user)
                #return HttpResponse("You are now connected")

            else:
                return render(request, 'vine/connection.html', {'form' :form})
                
                
    else:
        form= Form_connection()
        return render(request, 'vine/connection.html', {'form' :form})
##################################################VIEW_FOR_PROCESSING_CONNECTION_FORM##########################################################

  

                
#########################END OF VIEW FOR PROCESSING LOGIN (error 22-01-2018)###################################

##########################Django assisted logout function################################################
def logout(request):
    logout(request)
    return render(request, 'vine/Logout.html')
##########################END OF Django assisted logout function################################################
def signup2(request):
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            form.is_active = True 
            form.save()
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password1')
            user= authenticate(username=username, password=raw_password)
            if user:
                login=(request, user)
                return redirect('newvid')
    else:
        form= SignupForm()
    return render(request, 'vine/signup.html', {'form':form})        

################################END OF ENHANCED USING SIMPLE 2 FIELD FORM USER CREATION FORM####################################

##################################################SIGNING IN##########################################################
def signin(request):
    if request.method == 'POST':
        form= SigninForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password')
            user= authenticate(username=username, password=raw_password)
            if user:
                login=(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])   
            
                    return redirect('/newvid')
    #if request.GET.get('next') is not None:
        #return redirect(request.GET['next'])
            #if not user:
               # return HttpResponse("Wrong Password or User.")
                
    else:
        form= SigninForm()
    return render(request, 'vine/Signin.html', {'form':form})   

##################################################END OF SIGNING IN##########################################################         
