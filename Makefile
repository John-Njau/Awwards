serve:
	python manage.py runserver 8000

migrations:
	python manage.py makemigrations awards
	python manage.py migrate awards

super:
	python manage.py createsuperuser

shell:
	Python manage.py shell

tests: 
	python manage.py test

check: 
	python manage.py check awards