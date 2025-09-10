from config.env import env

APPS = [
    "channels",
    "cacheops",
    "django_ckeditor_5",
    "drf_spectacular",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_redis",
    "rest_framework_simplejwt",
    "django_core",
    "core.apps.accounts.apps.AccountsConfig",
    "click_up",
    "payme",
]

if env.bool("SILK_ENABLED", False):
    APPS += [
        "silk",
    ]
