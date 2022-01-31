# fluffy-octo-telegram

[Django](https://docs.djangoproject.com/en/4.0/)
web-app with a single `api` app inside and a few tests that can be
ran against the api app.

Just used as a project to build pipelines around for devops learning


## Testing out / running the project

Ensure you have all of the project dependencies installed in your python 
virtualenv by running `pip install -r requirements.txt` from the root
of the project.

Then you can run the development server using the command `python mysite/manage.py runserver`
this will start the [local dev server](http://localhost:8000/) for you to use.  and you can visit
[admin page](http://localhost:8000/api-auth/login)

## Running the api projects unit tests

`python manage.py test api`

## Jenkinsfile

Very basic currently, has three stages:
* running api tests
* tagging git repo with build number


