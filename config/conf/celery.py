from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "moysklad": {
        "task": "core.apps.api.tasks.moysklad.moysklad",
        "schedule": crontab(minute="*/60"),
    },
    "stores": {
        "task": "core.apps.api.tasks.moysklad.stores",
        "schedule": crontab(minute="*/30"),
    },
    # "retailshift": {
    #     "task": "core.apps.api.tasks.moysklad.retailshift",
    #     "schedule": crontab(hour=0, minute=0),
    # },
}
