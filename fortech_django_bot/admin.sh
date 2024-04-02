#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput


sleep 3

python manage.py runserver 0.0.0.0:8080
