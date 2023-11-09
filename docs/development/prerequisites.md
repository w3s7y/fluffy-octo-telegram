# Prerequisites

## Software
In order to minimise the number of separate downloads and setup required to get kubernetes and the rest of the stack 
running locally, I opted to use rancher desktop as my container runtime and kubernetes solution for local development.  
It has packages for all common operating systems and is easy to configure for what we need it for.  Most of the other 
software is optional and only needs to be downloaded if you want/need to use it.

| Name / Link                                   | Notes                                                       | 
|-----------------------------------------------|-------------------------------------------------------------|
| [Python 3](https://python.org)                | Currently project uses `3.11`                               |
| [Rancher Desktop](https://rancherdesktop.io/) | The main development / local run platform (k3s)             |
| [Terrform](https://www.terraform.io/)         | For building / bootstrapping resources (k8s cluster) in aws |
| [Sqlite3](https://www.sqlite.org/index.html)  | For looking in the local database file after tests etc.     | 

## Clone the repo

The documentation will give paths and commands relative to the root of the repository.  So clone and `cd` into
it. 
```shell
git clone https://github.com/w3s7y/fluffy-octo-telegram.git
cd fluffy-octo-telegram
```
