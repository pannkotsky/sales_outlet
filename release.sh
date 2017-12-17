#!/usr/bin/env bash

python manage.py migrate --noinput
apt-get update && apt-get install -y gettext
python manage.py compilemessages
