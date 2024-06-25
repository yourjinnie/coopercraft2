#echo "BUILD START"
#python-3.12.1 -m pip install -r requirment.txt
#ppython-3.12.1 manage.py collectstatic --noinput --clear
#echo "BUILD END"
#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
