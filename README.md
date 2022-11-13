## PIPENV
``All from Pipfile: pipenv install``

``Add to Pipefile: pipenv install <name>``

## DOCKER
``docker-compose up --build``

``API available at http://localhost:8080/docs``

## DATABASE

Connecting to the docker PG instance on your local can be done with 
`jdbc:postgresql://localhost:{PORT}:{POSTGRES_DB}` where port and postgres_db and username/password are from `.env`

### ALEMBIC

1. Make a database model change
2. docker-compose run {compose service that will have the py code and database creds} alembic revision --autogenerate -m "some description"
3. docker-compose run {compose service that will have the py code and database creds} alembic upgrade {head || hash_of_revision}
4. docker-compose run {compose service that will have the py code and database creds} alembic downgrade {-1 || hash_of_revision}

