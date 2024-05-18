"""
ASGI config for take_away project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import environ

from django.core.asgi import get_asgi_application


env = environ.Env(DEBUG=(bool, False))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'take_away.settings.{env("ENVIRONMENT")}')

application = get_asgi_application()
