serve:
	python3 manage.py runserver 8000

migrations:
	python3 manage.py makemigrations awards

migrate:
	python3 manage.py migrate awards

super:
	python3 manage.py createsuperuser

shell:
	Python3 manage.py shell

tests: 
	python3 manage.py test

check: 
	python3 manage.py check awards

migrateheroku: 
	heroku run python3 manage.py migrate

heroku:
	heroku create

push: 
	git push heroku master