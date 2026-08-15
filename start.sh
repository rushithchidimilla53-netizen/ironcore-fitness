#!/bin/sh

python manage.py migrate

exec gunicorn fitness_website.wsgi