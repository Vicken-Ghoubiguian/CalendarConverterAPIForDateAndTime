# WorldSwissKnifeAPI 🇨🇭🔪

Rest API which is also a swiss knife and to which you can add all the features you want, and like many others, it's a REST API just for experimenting and laughing 🇨🇭🔪...

## Contents

* [Introduction](#introduction),
* [Presentation](#presentation),
* [Features](#features),
* [Project's structure](#project_s_structure),
* [Project's development](#project_s_development),
* [Deployment](#deployment),
    * [Source code](#source_code),
    * [Docker](#docker)
      * [Requirements](#requirements),    
      * [From DockerHub](#from_dockerhub),
      * [From Dockerfile](#from_dockerfile)
    * [Heroku](#heroku)
    * [Balena](#balena)
* [Conclusion](#conclusion)
* [Useful links](#useful_links)

<a name="introduction"></a>
## Introduction

<a name="presentation"></a>
## Presentation

<a name="features"></a>
## Features

Of course, other features can be added to this API. To learn how and have a manual guide, please go [here]()...

<a name="project_s_structure"></a>
## Project's structure



<a name="project_s_development"></a>
## Project's development



<a name="deployment"></a>
## Deployment



<a name="source_code"></a>
### Source code

Firstly, you need to clone the corresponding repository from GitHub, using the following command :

```bash
git clone https://github.com/Vicken-Ghoubiguian/WorldSwissKnifeAPI
```

Second, you must position yourself in the `WorldSwissKnifeAPI` directory thus generated, again using the following command :

```bash
cd WorldSwissKnifeAPI
```

Thirdly, you must install all of the required Python packages listed in the `requirements.txt` file :

```bash
pip3 install -r requirements.txt
```

Fourthly and lastly, you must launch the `main.py` file using the following command :

```bash
python3 main.py
```

This command is equivalent to this one below :

```bash
python main.py
```

It's now the time to enjoy yourself 😸...

<a name="docker"></a>
### Docker

<a name="requirements"></a>
### Requirements

<a name="from_dockerhub"></a>
#### From DockerHub

The Docker image on Docker Hub is available [just here](https://hub.docker.com/repository/docker/wicken/worldswissknifeapi)...

First, to get started, you need to pull this Docker image through this command bellow :

```bash
docker pull wicken/worldswissknifeapi:latest
```

Secondly and finally, you have to run a new Docker container from this Docker image using the command bellow :

```bash
docker container run -d --name worldswissknifeapi -p 80:80 wicken/worldswissknifeapi:latest
```

It's done now... So enjoy yourself 😸...

<a name="from_dockerfile"></a>
#### From Dockerfile



```bash
git clone https://github.com/Vicken-Ghoubiguian/WorldSwissKnifeAPI
```



```bash
cd WorldSwissKnifeAPI
```



```bash
docker image build -t worldswissknifeapi:latest .
```



```bash
docker container run -d --name worldswissknifeapi -p 80:80 worldswissknifeapi:latest
```

NOW... enjoy yourself 😸...

<a name="heroku"></a>
### Heroku

<a name="balena"></a>
### Balena



<a name="conclusion"></a>
## Conclusion



<a name="useful_links"></a>
## Useful links

* [Welcome to Flask-RESTX’s documentation! - Official documentation](https://flask-restx.readthedocs.io/en/latest/),
     * [API Docs: inputs - Official documentation](https://flask-restful.readthedocs.io/en/latest/api.html#inputs),
* [Flask API Documentation using Flask-Restx (Swagger for Flask) - Medium](https://abhtri.medium.com/flask-api-documentation-using-flask-restx-swagger-for-flask-84be13d70e0),
* [Request Parsing](https://flask-restful.readthedocs.io/en/latest/reqparse.html),
* [Scaling your project - Official documentation](https://flask-restx.readthedocs.io/en/latest/scaling.html),
* [List All TimeZones in Python - PYnative](https://pynative.com/list-all-timezones-in-python/#h-get-list-of-all-timezones-name),
* [Python List append() - Programiz](https://www.programiz.com/python-programming/methods/list/append),
* [pycountry 22.1.10 - pypi](https://pypi.org/project/pycountry/),
* [Flagpedia.net](https://flagpedia.net),
* [Embed country flag images over CDN (HTTP API) - Flagpedia.net](https://flagpedia.net/download/api),
* [Python strftime() - Programiz](https://www.programiz.com/python-programming/datetime/strftime),
* [convertdate - GitHub](https://github.com/fitnr/convertdate),
* [convertdate - PyPi](https://pypi.org/project/convertdate/),
* [convertdate - Official documentation](https://convertdate.readthedocs.io/en/latest/index.html),
* [Flagpedia.net](https://flagpedia.net),
* [Embed country flag images over CDN (HTTP API) - Flagpedia.net](https://flagpedia.net/download/api),
* [Python How to Download a File from a URL - codingem.com](https://www.codingem.com/python-download-file-from-url/),
* [Pushing and Pulling to and from Docker Hub - R Docker tutorial](https://jsta.github.io/r-docker-tutorial/04-Dockerhub.html)
