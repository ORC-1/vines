from django import forms

from vinesF.models import videoID
from models import video
from models import users
from models import UserProfile
from models import viewcounter
from models import Hitbck2bck
from models import minihit
from models import emails
from django.forms.models import fields_for_model
from django.utils.six.moves import range
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import fields_for_model
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from django.contrib.auth import authenticate, login, logout #Import for processing Login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



#########################Form FOR PROCESSING NewVid###################################
class AddVidForm(forms.ModelForm):
    class Meta:
        model = video
        fields = ('primaryName','Origin','PreferredAudience', 'Link', 'file_path')

#########################ENF OF FORM FOR PROCESSING NewVid ###################################    

#########################Form FOR PROCESSING emailaddon###################################
class emailsForm(forms.ModelForm):
    class Meta:
        model = emails
        fields = ('email',)

#########################END OF FORM FOR PROCESSING EMAILS ################################### 

##########################User creation form and Processing #########################################
            
class NewUserForm(forms.Form):
    Name= forms.CharField(max_length=100, label= "Name")
    login= forms.CharField(max_length=25, label= "Login")
    password= forms.CharField(max_length=100, label= "Password")
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)
    phone= forms.CharField(max_length=14, label= "Phone")
    Birthday= forms.DateField()
    #Last_connection= forms.DateField(label= "Last_connection")
    email= forms.EmailField(label ="Email" )
    #date_created = models.DateField(verbose_name="date_created", auto_now_add=True )
    
    def clean(self):
        cleaned_data= super (NewUserForm, self).clean()
        password= self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data



        ################################ENHANCED USING SIMPLE 2 FIELD FORM USER CREATION FORM####################################
    
class SignupForm(UserCreationForm):
    first_name= forms.CharField(max_length=30, required=False)
    last_name= forms.CharField(max_length=30, required=False)
    email= forms.CharField(max_length=222, help_text='Required feild, please input your email address')

    class meta:
        model= User
        fields= ('username', 'first_name', 'last_name', 'email', 'password')    



##################################################SIGNING IN##########################################################
#class SigninForm(forms.Form):
    #username= forms.CharField(max_length=100, label= "Name")
    #password= forms.CharField(label= "Password", widget = forms.PasswordInput)
class SigninForm(forms.Form):
    username = forms.CharField(max_length=100,label="username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(SigninForm,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong login or password")
        return self.cleaned_data

##################################################END_OF_SIGNING IN FORM##########################################################

##################################################CONNECTION_FORM##########################################################

class Form_connection(forms.Form):
    username= forms.CharField(label="Login")
    password= forms.CharField(label="Password", widget=forms.PasswordInput)
    def clean2(self):
        cleaned_data = super(Form_connection,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not users(Name=username, password=password):
            raise forms.ValidationError("Wrong Login or Password or Both")
            
        return self.cleaned_data


##################################################END_OF_CONNECTION FORM##########################################################
