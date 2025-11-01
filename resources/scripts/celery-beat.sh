#!/bin/bash

set -e

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 2
  echo "Waiting postgress...."
done
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 2
  echo "Waiting redis...."
done

python3 manage.py compilemessages
celery -A config beat -l info

exit $?
