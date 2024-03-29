import os
from pathlib import Path

# from rest_framework.settings import api_settings

from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get("SECRET_KEY")


DEBUG = False

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # "debug_toolbar",
    "crispy_forms",
    "social_django",
    "blog",
    "mptt",
    "taggit",
    "django_social_share",
    "users",
    # "import_export",
    # DRF settings
    # "rest_framework",
    # "rest_framework.authtoken",
    # "allauth",
    # "allauth.account",
    # "allauth.socialaccount",
    # "allauth.socialaccount.providers.github",
    # "knox",
]

INSTALLED_APPS += ("django_summernote",)

SITE_ID = 1
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "0.0.0.0",
    "localhost",
    # ...
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "ourblog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                # 'blog.views.category_list',
            ],
        },
    },
]


# DEBUG_TOOLBAR_PANELS = [
#     "debug_toolbar.panels.versions.VersionsPanel",
#     "debug_toolbar.panels.timer.TimerPanel",
#     "debug_toolbar.panels.settings.SettingsPanel",
#     "debug_toolbar.panels.headers.HeadersPanel",
#     "debug_toolbar.panels.request.RequestPanel",
#     "debug_toolbar.panels.sql.SQLPanel",
#     "debug_toolbar.panels.staticfiles.StaticFilesPanel",
#     "debug_toolbar.panels.templates.TemplatesPanel",
#     "debug_toolbar.panels.cache.CachePanel",
#     "debug_toolbar.panels.signals.SignalsPanel",
#     "debug_toolbar.panels.logging.LoggingPanel",
#     "debug_toolbar.panels.redirects.RedirectsPanel",
# ]

WSGI_APPLICATION = "ourblog.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.twitter.TwitterOAuth",
    "social_core.backends.facebook.FacebookOAuth2",
)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = "/static/"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
CRISPY_TEMPLATE_PACK = "bootstrap4"


LOGIN_REDIRECT_URL = "blog:articles"
LOGIN_URL = "users:login"
ACCOUNT_LOGOUT_REDIRECT_URL = "users:logout"
SUMMERNOTE_THEME = "bs4"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
SOCIAL_AUTH_LOGIN_ERROR_URL = "users:settings"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "blog:articles"
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_GITHUB_KEY = os.environ.get("client_id")
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get("client_secret")

X_FRAME_OPTIONS = "SAMEORIGIN"


# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = True
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get("EMAIL")
# EMAIL_HOST_PASSWORD = os.environ.get("PASS")


# DRF settings

# """ REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework.authentication.TokenAuthentication",
#     )
# }


# REST_KNOX = {
#     "SECURE_HASH_ALGORITHM": "cryptography.hazmat.primitives.hashes.SHA512",
#     "AUTH_TOKEN_CHARACTER_LENGTH": 64,
#     "TOKEN_TTL": timedelta(hours=10),
#     "USER_SERIALIZER": "knox.serializers.UserSerializer",
#     "TOKEN_LIMIT_PER_USER": None,
#     "AUTO_REFRESH": False,
#     "EXPIRY_DATETIME_FORMAT": api_settings.DATETIME_FORMAT,
# } """
