# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from vinesF.models import video
from vinesF.models import viewcounter
from vinesF.models import users, Hitbck2bck, MostViewed, minihit, emails

# Register your models here.

admin.site.register(video)
admin.site.register(viewcounter)
admin.site.register(users)
admin.site.register(Hitbck2bck)
admin.site.register(MostViewed)
admin.site.register(minihit)
admin.site.register(emails)