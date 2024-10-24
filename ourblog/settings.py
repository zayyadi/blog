import os

# from rest_framework.settings import api_settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get("SECRET_KEY")


DEBUG = True

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
    "social_django",
    "blog",
    "crispy_forms",
    "crispy_bootstrap5",
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
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


AUTH_USER_MODEL = "users.CustomUser"
AUTH_USER_DEFAULT_GROUP = "blog-members"

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

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mailtrap.io"
EMAIL_HOST_USER = os.environ.get("EMAIL_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_FILE_PATH = os.getenv("EMAIL_FILE_PATH", os.path.join(BASE_DIR, "test-emails"))

EMAIL_USE_SSL: False

SITE_TITLE = os.getenv("SITE_TITLE", "Demo Site")
SITE_TAGLINE = os.getenv("SITE_TAGLINE", "Demo Site")
SITE_DESCRIPTION = "SITE_DESCRIPTION"
SITE_LOGO = os.getenv("SITE_LOGO", "http://localhost:8001/static/logo.png")
