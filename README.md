# ridez_api

[![Build Status](https://travis-ci.org/patpatpatpatpat/ridez_api.svg?branch=master)](https://travis-ci.org/patpatpatpatpat/ridez_api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

RESTful API using DRF for managing ride info. Check out the project's [documentation](http://patpatpatpatpat.github.io/ridez_api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

## Start the dev server for local development:
```bash
docker-compose up
```

## Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## Examples
```bash
docker-compose run --rm web python manage.py showmigrations
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py createsuperuser
```

### Steps to test
1. Create a superuser: `docker-compose run --rm web python manage.py createsuperuser`
2. Go http://localhost:8000/admin/, modify the created user's Role to `Admin`
3. Create Users/Rides via Django admin
4. Go to http://localhost:8000/api/v1/rides/ to test the API using a browser
