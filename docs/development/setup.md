# Setting up a local development environment

This page documents the high level steps and a few gotchas / config steps out of the default that will get you up and 
running developing features.  It will detail the basic setup, including what the toolchain looks like and has looked 
like through the project history.  

## Software
In order to minimise the number of separate downloads and setup required to get kubernetes and the rest of the stack
running locally, I opted to use rancher desktop as my container runtime and kubernetes solution for local development.  
It has packages for all common operating systems and is easy to configure for what we need it for.  Most of the other
software is optional and only needs to be downloaded if you want/need to use it.

This list assumes you already have basic tools like git etc. installed!

| Name / Link                                   | Notes                                                       | 
|-----------------------------------------------|-------------------------------------------------------------|
| [Python 3](https://python.org)                | Currently project uses `3.11`, ensure pip is installed too! |
| [Rancher Desktop](https://rancherdesktop.io/) | The main development / local run platform (k3s)             |
| [Helm](https://helm.sh/)                      | For deploying things to k8s directly from your machine.     |
| [Terrform](https://www.terraform.io/)         | For building / bootstrapping resources (k8s cluster) in aws |
| [Sqlite3](https://www.sqlite.org/index.html)  | For looking in the local database file after tests etc.     | 

## Cloning the repo

If not already done, clone the repo now.
The documentation will give paths and commands relative to the root of the repository.  So clone and `cd` into it.
```shell
git clone https://github.com/w3s7y/fluffy-octo-telegram.git
cd fluffy-octo-telegram
```

## Setting up python
```shell
pip3 install poetry
poetry install
```

## Setting up rancher
After installing rancher you will want to open the Preferences and set the following: 
* navigate to the `Container Engine` section and select `dockerd (moby)`.
* navigate to the `Kubernetes` section and ensure k8s is `enabled`.

You can then test if kubernetes and the rest of rancher at large is functioning by running: 
```shell
kubectl get pods --all-namespaces
```

If you get a small table with a number of rows returned you are good to move on. 

### Host aliases
To use the Ingress rules we create, create some local hostfile entries.
```shell
# Host entries for fluffy-octo-telegram testing
127.0.0.1	dev.vets.internal production.vets.internal
# ci/cd entries
127.0.0.1	argocd.vets.internal workflows.vets.internal 
# Monitoring
127.0.0.1 	loki.vets.internal grafana.vets.internal alertmanager.vets.internal prometheus.vets.internal 
# user admin / secrets
127.0.0.1	reset.vets.internal admin.vets.internal vault.vets.internal
# pgadmin
127.0.0.1   pgadmin.dev.vets.internal pgadmin.production.vets.internal
```


### Deploy argocd
```shell
# Create a namespace in k8s for argo
kubectl create ns argocd
# Install argocd 
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

This will probably take a few minutes to pull the images down and do the init routines.  Check for when the server is
running: `kubectl get pods -n argocd`.

### Deploy remaining cluster services
```shell
helm upgrade -i cluster-services deploy-descriptors/cluster/chart --namespace argocd
```
This takes an age (it is deploying approx 10 namespaces and the entire backend stack for the app) so let it whirl for
5-10 mins while it all comes online. 

### Initialise the local vault instance
Now the cluster services are running in the cluster this includes hashicorp vault.  We can hit the UI and get 
it configured. 

### Creation of app secrets
This is done manually for now:
```shell
kubectl create ns dev-vets
kubectl create secret generic vets-app -n dev-vets \
  --from-literal=DJANGO_SECRET_KEY='<<<<<<<<<<<<<<<<<<< A VERY LONG RANDOM STRING >>>>>>>>>>>>>>>>>>>' \
  --from-literal=POSTGRES_PASSWORD='<<<<< A COMPLEX PASSWORD >>>>>'
```
Repeat for namespace `production-vets` as well.

This will be moved to a vault implementation of secrets soon.

### Deploy vets 
You can head over to the [Operations](../operations/index.md) section if you want to deploy the apps via argo.  

Here we can just use helm to get it deployed:
```shell
helm upgrade -i dev-vets deploy-descriptors/vets/chart -n dev-vets
```

## Validating everything is working

### Testing local python running
```shell
poetry run vets-app-manage migrate
poetry run vets-app-manage test
```

### Testing pods up on k8s 
```shell
kubectl get pods -n dev-vets
# Should return some running pods (a database pod and an app pod). 
```
