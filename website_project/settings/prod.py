from .base import *
DEBUG = False

ALLOWED_HOSTS = ['mytesrtboiler.herokuapp.com']

import django_heroku

django_heroku.settings(locals())