from __future__ import unicode_literals
"""vines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from vinesF import views
import utils
from utils import views
import vinesF
from vinesF import views
from django.conf import settings #Added for video not found error TroubleShooting 24.05.2018 --No Effect
from django.conf.urls.static import static #Added for video not found error TroubleShooting 24.05.2018 --No Effect


app= 'vinesF', 'utils',

urlpatterns = [
    url(r'^vinesF/',include('vinesF.urls')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    url(r'^admin/', admin.site.urls),
    url(r'^newvid', vinesF.views.newvid, name='newvid'),
    url(r'^emails', vinesF.views.emails, name='emails'),
    url(r'^newuser', views.newuser, name='newuser'),
    url(r'^connection$', views.connection, name="public_connection"),
    url(r'^logout$', views.logout, name="public_Logout"),
    url(r'^signup2/$', views.signup2, name="public_Signup2"),
    url(r'^signin/$', views.signin, name="public_Signin"),
    url(r'^js-settings/$', utils.views.render_js,{'template_name': 'settings.js'},name='js_settings',),
    # url(r'^accounts/',include('allauth.urls')),

    
    
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


