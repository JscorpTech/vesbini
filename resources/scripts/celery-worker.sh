
#!/bin/bash

set -e

while ! nc -z db 5432; do
  sleep 2
  echo "Waiting postgress...."
done
while ! nc -z redis 6379; do
  sleep 2
  echo "Waiting redis...."
done

celery -A config worker -l info

exit $?


