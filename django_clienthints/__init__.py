# flake8: noqa
from importlib.metadata import version

import django


__version__ = version('django-clienthints')

if django.VERSION < (3, 2):
    default_app_config = 'django_clienthints.apps.ClientHintsConfig'
