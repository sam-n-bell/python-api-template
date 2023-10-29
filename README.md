# DO THIS FIRST
Nothing is going to work until the instances of {{template_name}} are replaced in this project.
### For Windows
From a terminal/Powershell window inside this project directory, run `.\name_replacer.sh <SomeNameWithoutThe<>Signs>`
### For Mac
run `make rename` (not tested yet)

## PIPENV
``All from Pipfile: pipenv install``

``Add to Pipefile: pipenv install <name>``

## DOCKER
``docker-compose up --build``

``API available at http://localhost:8080/docs``

## DATABASE

Connecting to the docker PG instance on your local can be done with 
`jdbc:{{YourAppName}}_db://localhost:{PORT}:{POSTGRES_DB}` where port and postgres_db and username/password are from `.env`

### ALEMBIC

1. Make a database model change
2. docker-compose run {compose service that will have the py code and database creds} alembic revision --autogenerate -m "some description"
3. docker-compose run {compose service that will have the py code and database creds} alembic upgrade {head || revision-hash}
4. docker-compose run {compose service that will have the py code and database creds} alembic downgrade {-1 || revision-hash}


# BLACK, ISORT & FLAKE8
```
pipenv run format
pipenv run sort
pipenv run lint
```

# TESTS
```
from main project directory, inside a terminal window enter/run `pytest`
```