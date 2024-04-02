#!/bin/sh

sleep 3

python manage.py migrate --noinput
python manage.py collectstatic --noinput

python manage.py run_bot

