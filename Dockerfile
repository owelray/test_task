# Dockerfile
# Pull base image
FROM python:3.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
RUN pip install pipenv
RUN pip install celery
RUN pip install djangorestframework
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Copy project
COPY . /code/