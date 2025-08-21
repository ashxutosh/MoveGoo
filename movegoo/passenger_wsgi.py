import os
import sys

from movegoo.wsgi import application

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = 'movegoo.settings'