DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

import django_heroku

django_heroku.settings(locals())