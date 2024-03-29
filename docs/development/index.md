# Development

The following intends to act as a quick reference handbook for developing vets. 


## Creating a development environment
You will find the inital setup for a complete dev environment over on the [Setup](setup.md) page.

## Project layout
    pyproject.toml              # Project poetry configuration file.
    mkdocs.yml                  # Documentation generator configuration file.
    .github/                    # CI Pipeline definitions
    docs/                       # Documentation root
    src/                        # Source files for vets application
        manage.py               # Main management script for django (shortcut `poetry run vets-app-manage`)
        vets/                   # Vets  (django application)
            models.py           # Database model (table) definitions
            testing/            # Test modules
            views/              # Custom (vets) views
        djangorestapi/          # Django project module (top-level django project directory)
    terraform/                  # Terraform modules to build k8s cluster and bootstrap in aws
    build-descriptors/          # UNUSED: Old CI pipelines from argo-workflows (use github actions now)
    deploy-descriptors/         # Helm charts
        cluster/                # Chart for deploying cluster services via argocd.
        vets/
            chart/              # Chart for deploying vets application (vanilla helm/k8s)
            argocd.yaml         # CRDs for deploying dev and production envs via argocd. 

## Environment Variables
Reference table of all environment variables the app reads, mostly on boot to populate / select values from settings
files.

| Name              | Default                                | Description                                                                                                                                           | 
|-------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| DJANGO_CACHE      | local                                  | cache selection ('local' or 'redis')                                                                                                                  |
| DJANGO_SECRET_KEY | None                                   | secret key for encrypted strings in db                                                                                                                | 
| DJANGO_DATABASE   | local                                  | database selection ('local' or 'main') local starts in-mem db for testing.  <br/>'main' reads env vars defined below to connect to postgres database. | 
| DJANGO_DEBUG      | False                                  | Turn on debugging                                                                                                                                     | 
| POSTGRES_NAME     | vets                                   | database name to connect to                                                                                                                           | 
| POSTGRES_USER     | vets-app                               | username to use to connect to db                                                                                                                      | 
| POSTGRES_PASSWORD | None                                   | database password                                                                                                                                     | 
| POSTGRES_HOST     | vets-database                          | hostname to connect to                                                                                                                                | 
| POSTGRES_PORT     | 5432                                   | Postgres port number                                                                                                                                  |
| REDIS_MASTER      | redis-master.redis.svc.cluster.local   | Master redis instance                                                                                                                                 |
| REDIS_REPLICAS    | redis-replicas.redis.svc.cluster.local | Redis replicas l/b address                                                                                                                            |
| REDIS_PORT        | 6379                                   | Redis port number                                                                                                                                     |

