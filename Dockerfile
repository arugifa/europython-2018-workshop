FROM python:3.6-alpine

ENV DATABASE_URL postgresql://user:password@localhost/database

RUN apk add --update \
    # PostgreSQL
    gcc libc-dev postgresql-dev

ADD . /src/
RUN pip install -r /src/requirements.txt

WORKDIR /src
ENTRYPOINT ["python", "manage.py"]
