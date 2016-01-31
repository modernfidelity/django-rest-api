
Django REST API
===============

This is a simple starting point when developing REST APIs in python using the Django REST Framework (3.x)

## Install

Clone the repo and then run the following commands. (local builds)

> pip install -r ./requirements.txt

## Docker

You will need to build the image and run a container.

The docker build exposes Nginx on port 9000 which passes requests to Gunicorn (WSGI) and in turns 
handle the Django application.
 
It is built on the official Ubuntu 14.04 LTS image.


## Useful Docker Commands (use with care)

- View docker images
```
docker images
```
- List actively running images (add -l to include stopped containers)
```
docker ps
```
- View container logs
```
docker logs -f <containerID>
```
- Stop container
```
docker stop <containerID>
```
- Delete non tagged images
```
for i in `docker images|grep \<none\>|awk '{print $3}'`;do docker rmi $i;done
```
- Delete containers
```
docker rm -f `docker ps --no-trunc -a -q`
```


## Reference

 - [Ubuntu](http://www.ubuntu.com/ "Ubuntu")
 - [Docker](https://www.docker.com/ "Docker")
 - [Python Virtual Environments](https://virtualenv.readthedocs.org/en/latest/userguide.html#usage "")
 - [Standards Guide PEP8](https://www.python.org/dev/peps/pep-0008/ "")
 - [Django 1.9.x Documentation](http://media.readthedocs.org/pdf/django/1.9.x/django.pdf "")









