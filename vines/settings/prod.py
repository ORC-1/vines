# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from .base import *


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': ,
    }
}
#overwrite setting here
#Security keys
#Database names and settings
#other productions settings