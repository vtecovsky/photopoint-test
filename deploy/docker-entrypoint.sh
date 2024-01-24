#!/bin/sh

set -e

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

# You can put other setup logic here
python manage.py makemigrations
python manage.py migrate

# Evaluating passed command:
exec "$@"