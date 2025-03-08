web: gunicorn django_project.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn django_project.wsgi