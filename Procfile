release: python manage.py migrate --noinput

web: gunicorn project_conf.wsgi --log-file -
