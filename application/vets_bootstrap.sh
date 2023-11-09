#!/usr/bin/env ash

# See if migrations need to be made and apply if so.
python3 -m application.manage migrate --check --no-input vets
if [[ $? != 0 ]]
then
    echo "Database had migrations that need to be applied or the db isn't ready."
    echo "Waiting 30 seconds attempting migrations"
    sleep 30
    python3 -m application.manage migrate --no-input --prune vets
fi

python3 -m application.manage runserver $1
