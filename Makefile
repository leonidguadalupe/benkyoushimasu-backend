.PHONY: clean total-clean test image coverage up down shell

clean:
	find . -name "*.pyc" -delete

total-clean: clean
	- find . -name "*~" -o -name "*.swp" | xargs rm

test: clean
	python3 manage.py test

image: total-clean
	docker build -t legends.azurecr.io/legends-backend -f docker/Dockerfile .

coverage: clean
	coverage run --source='.' --branch --omit="*/migrations/*","*/settings.py","*/wsgi.py","*/apps.py","manage.py" manage.py test
	coverage report

up:
	docker-compose -f docker/docker-compose.yml up --force-recreate

down:
	docker-compose -f docker/docker-compose.yml down -v

shell:
	docker exec -it docker_app_1 sh
