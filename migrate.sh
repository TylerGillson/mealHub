#!/bin/bash
python3 manage.py dumpdata > dump.json
python3 manage.py migrate
python3 manage.py loaddata dump.json