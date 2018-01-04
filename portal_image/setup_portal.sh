#!/usr/bin/env bash
cd portal
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000