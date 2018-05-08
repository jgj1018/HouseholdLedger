#!/usr/bin/env bash
python3 $PWD/wait-for-db.py

python3 manage.py migrate && python3 manage.py createsuper && python3 manage.py runserver 0.0.0.0:8000