FROM ubuntu:14.04

MAINTAINER @modernfidelity

# The following Github repos act as reference for running Django on Docker in AWS EB :
#  - https://github.com/AndrewSmiley/django-docker-eb
#  - https://github.com/glynjackson/django-docker-template


# Update packages
RUN apt-get update -y && apt-get upgrade -y

# Install Python Setuptools and some other tools for working with this container if attached to it
# RUN apt-get install -y tar git curl vim wget dialog net-tools build-essential
RUN apt-get install -y git curl vim wget net-tools build-essential
RUN apt-get install -y python python-dev python-distribute python-pip supervisor

# Copy the contents of this directory over to the container at location /src
ADD . /src


# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src && pip install -r /src/requirements.txt


# The port we are exposing needs to match the port we are binding GUNICORN too.
# See the reference-supervisord.conf file for the proper conf #
EXPOSE  8002

# Set the working directorly
WORKDIR /src

RUN python manage.py collectstatic --noinput


# Command to execute when we run the contaner. This is the default for sudo docker run for this image
CMD supervisord -c /src/supervisord.conf

