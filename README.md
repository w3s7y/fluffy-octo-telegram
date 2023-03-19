# fluffy-octo-telegram

A [Django](https://docs.djangoproject.com/) and [Rest Framework](https://www.django-rest-framework.org/)
application with a `vets` application (Django learning playground).

This project was originally a pure django learning environment, it has since been extended to also act as my
[argocd](https://argo-cd.readthedocs.io/en/stable/), 
[argo-workflow](https://argoproj.github.io/argo-workflows/) and
[helm](https://helm.sh/) playground and as such has been updated to include build and deploy
descriptors / helm charts as necessary for using Argo as the build/deploy platform. 

## Vets
So the main part of this project is essentially a booking system for vet surgeries.  To this end the api has 
models for a `client`, a `vet`, a `pet`, `appointment` and so on.

[An attempt was made](https://github.com/w3s7y/fluffy-octo-telegram/issues?q=label%3Astory) at user stories to track 
features I'm pursuing.

# Dockerhub
[Here](https://hub.docker.com/repository/docker/theshipyard/vets-app/general) you will find the built version
of `vets-app`  

# The wiki
The technical documentation has moved to 
[the wiki](https://github.com/w3s7y/fluffy-octo-telegram/wiki).
