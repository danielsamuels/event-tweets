"""
Production settings for event_tweets project.

For an explanation of these settings, please see the Django documentation at:

<http://docs.djangoproject.com/en/dev/>

While many of these settings assume sensible defaults, you must provide values
for the site, database, media and email sections below.
"""
from __future__ import unicode_literals

import os
import sys


# The name of this site.  Used for branding in the online admin area.

SITE_NAME = "Example"

SITE_DOMAIN = "eventtweets.com"

PREPEND_WWW = True

ALLOWED_HOSTS = [
    SITE_DOMAIN,
    'www.{}'.format(SITE_DOMAIN)
]

SUIT_CONFIG = {
    'ADMIN_NAME': SITE_NAME
}

# Database settings.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "event_tweets",
        "USER": "event_tweets",
        "PASSWORD": "",
        "HOST": "",
        "PORT": ""
    }
}


# Absolute path to the directory where all uploaded media files are stored.

MEDIA_ROOT = "/var/www/event_tweets_media"

MEDIA_URL = "/media/"

FILE_UPLOAD_PERMISSIONS = 0o644


# Absolute path to the directory where static files will be collected.

STATIC_ROOT = "/var/www/event_tweets_static"

STATIC_URL = "/static/"


# Email settings.

EMAIL_HOST = "smtp.mandrillapp.com"

EMAIL_HOST_USER = "developers@onespacemedia.com"

EMAIL_HOST_PASSWORD = ""

EMAIL_PORT = 587

EMAIL_USE_TLS = True

SERVER_EMAIL = "{name} <notifications@{domain}>".format(
    name=SITE_NAME,
    domain=SITE_DOMAIN,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME


# Error reporting settings.  Use these to set up automatic error notifications.

ADMINS = (
    ("Onespacemedia Errors", "errors@onespacemedia.com"),
)

MANAGERS = ()

SEND_BROKEN_LINK_EMAILS = False


# Locale settings.

TIME_ZONE = "Europe/London"

LANGUAGE_CODE = "en-gb"

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Auto-discovery of project location.

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# A list of additional installed applications.

INSTALLED_APPS = (

    "django.contrib.sessions",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "suit",
    "django.contrib.admin",
    "django.contrib.sitemaps",

    "sorl.thumbnail",
    "compressor",

    "cms",

    "reversion",
    "watson",

    "cms.apps.media",

    "event_tweets.apps.site",

    'server_management',
    'django_extensions',
    'cachalot',
)


# Additional static file locations.

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

# Dispatch settings.

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "watson.middleware.SearchContextMiddleware",
    # "historylinks.middleware.HistoryLinkFallbackMiddleware",
    "cms.middleware.PublicationMiddleware",
    "cms.apps.pages.middleware.PageMiddleware",
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)


ROOT_URLCONF = "event_tweets.urls"

WSGI_APPLICATION = "event_tweets.wsgi.application"

PUBLICATION_MIDDLEWARE_EXCLUDE_URLS = (
    "^admin/.*",
)

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

SITE_ID = 1

# Absolute path to the directory where templates are stored.

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, "templates"),
)

TEMPLATE_LOADERS = (
    ("django.template.loaders.cached.Loader", (
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "cms.context_processors.settings",
    "cms.apps.pages.context_processors.pages",
)


# Namespace for cache keys, if using a process-shared cache.

CACHE_MIDDLEWARE_KEY_PREFIX = "event_tweets"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        'LOCATION': '127.0.0.1:11211',
    }
}


# A secret key used for cryptographic algorithms.

SECRET_KEY = "p4xoc%u70gg&jcmua42o4s&=02c0opk7-n+aatcyh$+$7t+w0b"


REDACTOR_OPTIONS = {
    "plugins": ["table", "imagemanager", "video", "filemanager"],
    "imageUpload": "/admin/media/file/redactor/upload/image/",
    "fileUpload": "/admin/media/file/redactor/upload/file/",
    "minHeight": 300,
    "formattingAdd": [
        {
            "tag": "a",
            "title": "Button",
            "class": "button primary",
        }
    ]
}


NEWS_APPROVAL_SYSTEM = False

GOOGLE_ANALYTICS = ''

# You can get your Client ID & Secret here: https://creativesdk.adobe.com/myapps.html
ADOBE_CREATIVE_SDK_ENABLED = False
ADOBE_CREATIVE_SDK_CLIENT_SECRET = ''
ADOBE_CREATIVE_SDK_CLIENT_ID = ''


SILENCED_SYSTEM_CHECKS = [
    '1_6.W001',
    # '1_6.W002'
]

if 'test' in sys.argv:
    # The CMS tests use test-only models, which won't be loaded if we only load
    # our real migration files, so point to a nonexistent one, which will make
    # the test runner fall back to 'syncdb' behavior.

    # Note: This will not catch a situation where a developer commits model
    # changes without the migration files.

    class DisableMigrations(object):

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return "notmigrations"

    MIGRATION_MODULES = DisableMigrations()
