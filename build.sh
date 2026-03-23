#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    u = User.objects.create_superuser('admin', 'dharshinidr05@gmail.com', 'admin1234')
    u.is_staff = True
    u.is_superuser = True
    u.save()
    print('Superuser created')
else:
    u = User.objects.get(username='admin')
    u.is_staff = True
    u.is_superuser = True
    u.set_password('admin1234')
    u.save()
    print('Superuser updated')
"
