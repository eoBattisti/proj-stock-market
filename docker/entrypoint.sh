#!/usr/bin/env bash

echo "Apply database migrations"
python manage.py migrate --fake-initial

python manage.py runserver 0.0.0.0:9000