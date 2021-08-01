import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('ak model', 'schoolmanagement.settings')
application = get_asgi_application()
