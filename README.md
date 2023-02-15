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

## CI / CD
The project was originally built and deployed to a target environment via Jenkinsfile.  
I got sick of Jenkins and was told about [argocd](https://argo-cd.readthedocs.io/en/stable/) and 
[argo-workflows](https://argoproj.github.io/argo-workflows/) which are CI/CD tooling built for the k8s platform 
in that the argo resources are implemented as k8s Crds so very easy to deploy, update and generally just work with.

It was also deployed to k8s originally via arbitrary `kubectl` commands using static deploy specs.  This isn't very
"real world" so again I have gone for [helm](https://helm.sh/) which allows much more flexibility in customizing a 
deployment.

### Deploying argo-workflow (ci) and argocd to your cluster
Pretty simple job, just run the following to deploy the latest and greatest Argo CD stack: 
```shell
kubectl create ns argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

And this lot to deploy the workflow (CI) part of argo:
```shell
kubectl create ns argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.4.5/install.yaml
```

Full docs can be found [here for the workflow stack](https://argoproj.github.io/argo-workflows/) and 
[here for the CD stack](https://argo-cd.readthedocs.io/en/stable/).

### build-descriptors subdirectory
This subdirectory contains a directory for each workflow in argo.  So deployment of the build pipeline is a simple
```shell
kubectl apply -n argo -f build-descriptors/vets/argo.yaml
```
This will deploy the build pipeline for the vets application to argo. 

### deploy-descriptors subdirectory
Much like the build-descriptors held the build pipeline code, this contains all the pipeline code pertaining to deployment of a 
built image to the k8s cluster from dockerhub.  Every argocd project has its own subdirectory and then under that will
be a `chart` directory which contains the helm chart to deploy.

To 
```shell
kubectl apply -n argocd -f deploy-descriptors/vets/argocd.yaml
```
This will deploy the deployment pipelines to argocd.  Current configuration is roughly like this: 

git master branch -> production-vets namespace -> synced manually 
git develop branch -> dev-vets namespace -> synced automatically 
