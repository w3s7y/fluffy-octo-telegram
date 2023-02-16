# fluffy-octo-telegram

A [Django](https://docs.djangoproject.com/en/4.0/) and [Rest Framework](https://www.django-rest-framework.org/)
application with all the djangorestapi tutorial apps and my `vets` projects (My Django learning playground).

This project was originally a pure django learning environment, it has since been extended to also act as my
[argocd](https://argo-cd.readthedocs.io/en/stable/), 
[argo-workflow](https://argoproj.github.io/argo-workflows/) and
[helm](https://helm.sh/) playground and as such has been updated to include build and deploy
descriptors / helm charts as necessary for using Argo as the build/deploy platform. 

## Vets
So the "meat and taters" of this project is essentially a booking system for vet surgeries.  To this end the api has 
models for a `client`, a `vet`, a `pet`, `appointment` and so on.

As this is my own project the requirements are fairly simple and only used as a rough guide to what I want to achieve 
here.  
I have mapped them out as [several user stories](https://github.com/w3s7y/fluffy-octo-telegram/issues?q=label%3Astory) 
for ease of delivery.

## Testing out / running the project
Ensure you have all the project dependencies installed in your python 
virtualenv by running `pip install -r application/requirements.txt` from the root
of the project.

Then you can run the development server using the command `python application/manage.py runserver`
this will start the [local dev server](http://localhost:8000/admin) for you to use.  and you can visit
[admin page](http://localhost:8000/api-auth/login)

## Running the projects unit tests (all tests in all apps)
`python application/manage.py test`

## Building the project locally
You _should_ never really need to do this as the image is built and deployed to dockerhub 
as part of the build pipeline, but it is here for completeness. 
```shell
docker build -t theshipyard/vets-app:<some tag> .
```
Where `some tag` is just the image tag, if you are testing something _really_ out there please avoid the semver tags and 
use something personal like `bw-my-super-janky-build` and delete the tag from the hub when you are finished. 

## Django apps
The following is a list and quick description of the django applications in this project. 

| Name          | Description                                                                                                                                        | 
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| djangorestapi | The django project itself, has the project-wide `urls.py` and the projects `settings.py`                                                           |
| api           | [Rest Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/) just for reference                                         |
| snippets      | [Rest Framework Longer tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) - A pastebin API clone                           |
| vets          | The "main" application.  A pretend backend API for a vets surgery (including checking in and out clients pets, surgery times, vet timetables etc.) |
| vets-ui       | Currently not there (future playing around) will be the UI for the frontend in some language or other if I ever get there                          | 

## Deploying argocd to the cluster
Pretty simple job, just run the following to deploy the latest and greatest Argo CD stack: 
```shell
kubectl create ns argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
Wait for this to all come up

Full docs can be found [here for the workflow stack](https://argoproj.github.io/argo-workflows/) and 
[here for the CD stack](https://argo-cd.readthedocs.io/en/stable/).

## Deploying the rest of the stack (logging, monitoring, argo workflows etc.)
Done as an argocd project and set of apps just run:
```shell
kubectl apply -n argocd -f deploy-descriptors/cluster/apps.yaml
```
This deploys a lot to the cluster!  have at least 10gb of memory free!

### build-descriptors subdirectory
This subdirectory contains a directory for each workflow in argo.  So deployment of the build pipeline is a simple
```shell
kubectl apply -n argo -f build-descriptors/vets/workflow.yaml
```
This will submit a workflow to argo for the vets application to be tested, built and pushed 

### Deploying CD pipelines for vets app
```shell
kubectl apply -n argocd -f deploy-descriptors/vets/argocd.yaml
```
This will create the deployment pipelines for two envs of vets app in the cluster which uses the helm chart from the 
same directory to deploy.
