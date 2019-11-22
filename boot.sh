#!/bin/sh
export FLASK_APP=microblog.py
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:demoapp
