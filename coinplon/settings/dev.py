from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^ibso@1phcy6)@2n%*kl=y25@x44tw+*af)w(+$n07v2n@(^nb"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS+=["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]+ MIDDLEWARE

INTERNAL_IPS=["127.0.0.1"]
try:
    from .local import *
except ImportError:
    pass
