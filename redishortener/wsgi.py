"""
WSGI config for redishortener project.

"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redishortener.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
