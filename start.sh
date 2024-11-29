# !/bin/sh

echo "starting users"

source ./venv/Scripts/activate

# pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
