#!/bin/bash

while ! nc -z db 5432; do
  sleep 2
  echo "Waiting postgress...."
done

python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
python3 manage.py compilemessages

gunicorn config.wsgi:application -b 0.0.0.0:8000 --workers 6 --worker-class gevent --worker-connections 10000 # $(($(nproc) * 2 + 1)) 

exit $?


