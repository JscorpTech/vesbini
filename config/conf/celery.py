from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "moysklad": {
        "task": "core.apps.api.tasks.moysklad.moysklad",
        "schedule": crontab(minute="*/5"),
    },
}
