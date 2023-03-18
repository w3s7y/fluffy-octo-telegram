#!/usr/bin/env ash

python3 manage.py migrate --check --no-input
if [[ $? != 0 ]]
then
    python3 manage.py migrate --no-input --prune
fi

python3 manage.py runserver $1
