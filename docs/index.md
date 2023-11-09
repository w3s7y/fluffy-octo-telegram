# Vets
Welcome to the documentation for `fluffy-octo-telegram` (or the "Vets" application).

For what it is, head over to the [Architecture](architecture/index.md) section which details what the 
application "looks like" and its core functionality.  It is also where the design wireframes, mockups etc. are.

## Running the project
There are a couple of ways to run the project, the suitability of each is dependent on individuals current dev setups 
etc. 

### Method 1: Quick and dirty - using python and poetry 
If you already have python and poetry installed you can just clone the repo, migrate the database and start the 
application:
```shell
# Set some env vars for running app locally.
export DJANGO_CACHE=local
export DJANGO_SECRET_KEY=some_long_random_string_0123456789
export DJANGO_DATABASE=local
export DJANGO_DEBUG=True

# Clone repo and cd into dir. 
git clone https://github.com/w3s7y/fluffy-octo-telegram.git
cd fluffy-octo-telegram

# Install python dependencies, migrate db and run local server (http://localhost:8000/vets/admin). 
poetry install
poetry run vets-app-manage migrate
poetry run vets-app-manage createsuperuser
poetry run vets-app-manage runserver
```

### Method 2: Complete development setup
If you don't already have a development environment for python you will probably want to setup a new one with all
the bells and whistles, head over to the [Development](development/setup.md) section to get setup. 

## The kanban board
The project in-flight status, milestones etc. are all over on github projects: 
[here](https://github.com/users/w3s7y/projects/2/views/1)

## Links
*note: only work if you have setup the local k8s environment*

* [vets dev environment](https://dev.vets.internal/vets/auth/login/?next=/vets/admin)
* [vets production environment](https://production.vets.internal/vets/auth/login/?next=/vets/admin)
* [argocd](https://argocd.vets.internal/)
* [argo-workflows](https://workflows.vets.internal/)
* [vault](https://vault.vets.internal/)
* [grafana](https://grafana.vets.internal/login)
* [ldap server console](https://admin.vets.internal)
* [ldap server password reset tool](https://reset.vets.internal)

### Links to documentation
* [Django core documentation](https://docs.djangoproject.com/)
* [Django rest_framework](https://www.django-rest-framework.org/)
* [minikube](https://minikube.sigs.k8s.io/docs)
* [helm](https://helm.sh/docs)
* [argo CD](https://argo-cd.readthedocs.io/en/stable/)
* [argo workflows](https://argoproj.github.io/argo-workflows/workflow-concepts/)
* [argo workflow examples](https://github.com/argoproj/argo-workflows/tree/master/examples)
* [argo events](https://argoproj.github.io/argo-events/concepts/architecture/)
* [argo event examples](https://github.com/argoproj/argo-events/tree/master/examples)
