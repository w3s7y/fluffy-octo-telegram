# fluffy-octo-telegram

[Django](https://docs.djangoproject.com/en/4.0/) and [Rest Framework](https://www.django-rest-framework.org/)
web-app with all the tutorial apps and my play projects (My Django learning playground).  

Also used as an "app" for build/test/deploy in CI/CD pipelines.

## Testing out / running the project

Ensure you have all of the project dependencies installed in your python 
virtualenv by running `pip install -r application/requirements.txt` from the root
of the project.

Then you can run the development server using the command `python application/manage.py runserver`
this will start the [local dev server](http://localhost:8000/admin) for you to use.  and you can visit
[admin page](http://localhost:8000/api-auth/login)

## Running the projects unit tests (all tests in all apps)

`python application/manage.py test`

## Django apps

The following is a list and quick description of the apps in this project. 

* djangorestapi - The django project itself, has the project-wide `urls.py` and the projects `settings.py`
* api - [Rest Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
* snippets - [Rest Framework Longer tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) - A pastebin API clone
* vets - Pretend backend API for a vets surgery (including checking in and out clients pets, surgery times, vet timetables etc.)

## Argo-CI integration 


## Argo-CD integration
Under the `deploy-descriptors` dir there are some `argocd-*.yaml` files which are used to deploy the top-level project
and then the application sets in that project to argocd.

Think: `kubectl apply -f deploy-descriptors/argocd-*.yaml`

This will deploy the deployment pipelines to argocd.  Current configuration is roughly like this: 

git master branch -> prod-vets namespace -> synced manually 
git develop branch -> dev-vets namespace -> synced automatically 
