from .base import *

DEBUG = False

ALLOWED_HOSTS = ['mytestboiler.herokuapp.com']

import django_heroku

django_heroku.settings(locals())
