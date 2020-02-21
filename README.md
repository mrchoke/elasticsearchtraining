# Git clone

```
$ git clone  https://github.com/mrchoke/elasticsearchtraining
```

and then

```
$ cd elasticsearchtraining
```

# Docker

## Setup Environments
### Copy .env
```
$ cp defualt.env .env
```
### Manual Edit
```
ELK_VERSION=7.6.0
PROJECT_NAME=Training
ES_PORT=2000
KIBANA_PORT=2001

USERNAME=test
DUID=1000
```

### Auto script
```
$ ./config.sh
```
Output

```
Porject name: TRAIN
ELK version: 7.6.0
ES port: 2222
Kibana port: 3333
==============================
Project = TRAIN
USERNAME =  es10
UID =  1011
ELK =  7.6.0
ES Port =  2222
Kibana Port =  3333
==============================%
```
## Before start
**Linux host only**

###Add below to /etc/sysctl.conf
```
vm.max_map_count=262144
```
and apply

```
$ sudo sysctl -p
```


## Start Docker services
First time
```
$ docker-compose up -d
```

Check docker services

```
$ docker-compose ps
```
Output

```
             Name                           Command               State                Ports
----------------------------------------------------------------------------------------------------------
elasticsearchtraining_es_1       /usr/local/bin/docker-entr ...   Up      0.0.0.0:2222->9200/tcp, 9300/tcp
elasticsearchtraining_kibana_1   /usr/local/bin/dumb-init - ...   Up      0.0.0.0:3333->5601/tcp
```

## Test Elasticsearch server

```
$ curl localhost:{your_port}
```
Example
```
$ curl localhost:2000
```
If Work you can see

```
{
  "name" : "es",
  "cluster_name" : "es-cluster",
  "cluster_uuid" : "55OPFHcoR0W5OjZVMEC4Fg",
  "version" : {
    "number" : "7.6.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "7f634e9f44834fbc12724506cc1da681b0c3b1e3",
    "build_date" : "2020-02-06T00:09:00.449973Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```
## Kibana

Open web browser

```
http://kibana-ip:kibana-port
```
Example
```
http://localhost:3333
```
