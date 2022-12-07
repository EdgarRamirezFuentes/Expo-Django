"""
WSGI config for NewtworkAdmin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from channels.routing import ProtocolTypeRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewtworkAdmin.settings')

#application = ProtocolTypeRouter({
 #   'http': get_wsgi_application()
#})

application = get_wsgi_application()


