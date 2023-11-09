#!/usr/bin/env ash

# See if migrations need to be made and apply if so.
python -m manage migrate --check --no-input vets
if [[ $? != 0 ]]
then
    echo "Database had migrations that need to be applied or the db isn't ready."
    echo "Waiting 30 seconds attempting migrations"
    sleep 30
    python -m manage migrate --no-input --prune vets
fi

python -m manage $1
