FROM python:alpine3.16
MAINTAINER theshipyard

RUN apk update \
	&& apk add postgresql-client

WORKDIR /usr/src/app
COPY ./application/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./application .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
