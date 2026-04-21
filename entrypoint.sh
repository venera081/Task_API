python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn Task_Manager_API.wsgi:application --bind 0.0.0.0:8000