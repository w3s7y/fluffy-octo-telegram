FROM python:3.11-alpine3.17
MAINTAINER theshipyard

RUN apk update \
	&& apk add postgresql-client

WORKDIR /usr/src/app
COPY ./application/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./application .

USER nobody
EXPOSE 8000
CMD ["./vets_bootstrap.sh", "0.0.0.0:8000"]
