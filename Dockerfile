FROM python:3.10


WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile /usr/src/app
COPY Pipfile.lock /usr/src/app

RUN pipenv install --system --deploy

COPY . /usr/src/app

ENV PYTHONPATH = /usr/src/app

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

