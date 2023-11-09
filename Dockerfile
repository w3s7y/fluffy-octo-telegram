FROM python:3.11-alpine3.17
MAINTAINER theshipyard

RUN apk update \
	&& apk add postgresql-client

WORKDIR /usr/src/app

COPY ./fluffy_octo_telegram-* .
RUN pip install fluffy_octo_telegram-*
COPY application/vets_bootstrap.sh .
RUN chmod 755 ./vets_bootstrap.sh

# Adding this in temporarily so you can makemigrations in the container
# Remove once 0001_inital migration is stable and committed to repo (0.3.0)
RUN chown nobody vets/migrations

USER nobody
EXPOSE 8000
CMD ["./vets_bootstrap.sh", "0.0.0.0:8000"]
