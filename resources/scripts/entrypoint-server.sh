#!/bin/bash
python3 manage.py collectstatic --noinput

gunicorn config.wsgi:application -b 0.0.0.0:8000 --workers 4 # $(($(nproc) * 2 + 1)) 



exit $?


