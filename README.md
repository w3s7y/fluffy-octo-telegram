# fluffy-octo-telegram

[Django](https://docs.djangoproject.com/en/4.0/) and [Rest Framework](https://www.django-rest-framework.org/)
web-app with all the tutorial apps and my play projects (My Django learning playground).  

Also used as an "app" for build/test/deploy in CI/CD pipelines.

## Testing out / running the project

Ensure you have all of the project dependencies installed in your python 
virtualenv by running `pip install -r requirements.txt` from the root
of the project.

Then you can run the development server using the command `python mysite/manage.py runserver`
this will start the [local dev server](http://localhost:8000/admin) for you to use.  and you can visit
[admin page](http://localhost:8000/api-auth/login)

## Running the projects unit tests (all tests in all apps)

`python manage.py test`

## Django apps

The following is a list and quick description of the apps in this project. 

* djangorestapi - The django project itself, has the project-wide `urls.py` and the projects `settings.py`
* api - [Rest Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
* snippets - [Rest Framework Longer tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) - A pastebin API clone
* vets - Pretend backend API for a vets surgery (including checking in and out clients pets, surgery times, vet timetables etc.)

## Jenkinsfile

Very basic currently, has three stages:
* running api tests
* tagging git repo with build number


