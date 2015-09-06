uwsgi --uid www-data --wsgi-file manage.py --env DJANGO_SETTINGS_MODULE=settings.base -s /tmp/jiajiale.sock --chmod-socket=666
