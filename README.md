# fluffy-octo-telegram
[![Vets CI / CD Workflow](https://github.com/w3s7y/fluffy-octo-telegram/actions/workflows/vets.yml/badge.svg)](https://github.com/w3s7y/fluffy-octo-telegram/actions/workflows/vets.yml)

A [Django](https://docs.djangoproject.com/) and [Rest Framework](https://www.django-rest-framework.org/)
application with a `vets` application (Django learning playground).

This project was originally a pure django learning environment, it has since been extended to include platform options
as well (k8s infra) and has become a bit of a playground for that as well. 

## Vets application
The main app of the project is a booking system for vet surgeries.  To this end the api has 
models for a `client`, a `vet`, a `pet`, `appointment` and so on.

[User Stories](https://github.com/w3s7y/fluffy-octo-telegram/issues?q=label%3Astory) to track features I'm pursuing.

# Container Image Builds
[On Dockerhub](https://hub.docker.com/repository/docker/theshipyard/vets-app/general) 
you will find the released versions of `vets-app`.  

# The documentation
All the documentation has recently moved out of github wiki and into `docs/` and is a `mkdocs-material` based site:
[The Documentation](https://w3s7y.github.io/fluffy-octo-telegram/).
