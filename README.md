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
I have mapped them out as [user stories](https://github.com/w3s7y/fluffy-octo-telegram/issues?q=label%3Astory)

## Testing out / running the project
Ensure you have all the project dependencies installed in your python 
virtualenv by running `pip install -r application/requirements.txt` from the root
of the project.

Apply the migrations to the database:
```shell
python application/manage.py migrate
```

Then you can run the development server using the command 
```shell
python application/manage.py runserver
```
this will start the [local server](http://localhost:8000/vets/vets/) for you to use.  and you can visit the
[admin page](http://localhost:8000/api-auth/login?next=/admin)

## Running the projects unit tests (all tests in all apps)
`python application/manage.py test`

## Building the project locally
You _should_ never really need to do this as the image is built and deployed to dockerhub 
as part of the build pipeline, but it is here for completeness. 
```shell
docker build -t vets-app:<some tag> .
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

## Deploying the cluster
I will skip over the installation of minikube or whatever other kubernetes offering you are using.  It is assumed 
you cluster is already up, has `ingress-nginx` installed, and you can `kubectl` it. 

### Deploying ArgoCD
As argoCD is the main driver for deploying, just run the following to deploy the latest and greatest Argo CD stack: 
```shell
kubectl create ns argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl wait --for=condition=Available=true deployment/argocd-server -n argocd
```
Full docs can be found [here](https://argo-cd.readthedocs.io/en/stable/).

### Deploying the rest of the stack (logging, monitoring, argo workflows etc.)
First up are a few config objects and secrets which will be used by upcoming deployments:

### Elasticsearch trial enterprise license
```shell
kubectl create ns logging
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: eck-trial-license
  namespace: logging
  labels:
    license.k8s.elastic.co/type: enterprise_trial
  annotations:
    elastic.co/eula: accepted
EOF
```

### deploy all the cluster-wide services
Done as an argocd project and set of apps all wrapped up in a helm chart just run:
```shell
helm install cluster-services deploy-descriptors/cluster/chart --namespace argocd
```
This deploys a lot to the cluster!  have at least 10gb of memory free!

### Deploying CD pipelines for vets-app
```shell
kubectl apply -n argocd -f deploy-descriptors/vets/argocd.yaml
```
This will create the deployment pipelines for two envs of vets app in the cluster which uses the helm chart from the 
same directory to deploy.

In the current configuration, the `dev` environment uses the `develop` branch and the `production` environment uses
`master` as its source for deployment charts.

## Accessing the cluster http services (minikube)
To do this I use `minikube tunnel` which exposes the clusters ingress objects over localhost 
so just some local host file hacks are the simplest way for quick and dirty testing. 

```shell
# Hosts for fluffy-octo
127.0.0.1	dev.vets production.vets
# ci/cd entries
127.0.0.1	argocd.vets.internal workflows.vets.internal 
# Logging
127.0.0.1	kibana.vets.internal 
# Monitoring
127.0.0.1 	grafana.vets.internal alertmanager.vets.internal prometheus.vets.internal 
# user admin / secrets
127.0.0.1	reset.vets.internal admin.vets.internal vault.vets.internal
```
Then you can use `https://` for all the endpoints as the ingress controller deploys its own self-signed cert. 