"""
ASGI config for leadmanag project.
"""

from django.core.asgi import get_asgi_application
import os
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      os.getenv('DJANGO_SETTINGS_MODULE'))

application = get_asgi_application()
