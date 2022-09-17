#!/usr/bin/env bash

echo "Migrate..."
python manage.py migrate --noinput
echo "Migrated!"

echo "Loading fixtures..."
python manage.py loaddata */fixtures/*.json
echo "Done!"

echo "Starting Celery..."
(watchmedo auto-restart --directory=/setup/ --pattern "*tasks.py"  --recursive -- \
celery -A setup beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler \
) &

echo "\tStarting workers (1 worker, 3 if necessary)..."
(watchmedo auto-restart --directory=/setup/ --pattern "*tasks.py"  --recursive -- \
celery -A setup worker -l info -Q default --autoscale=3,1 --without-mingle --without-gossip \
-n default.%h) &
echo "Celery started!"


python manage.py runserver 0.0.0.0:9000