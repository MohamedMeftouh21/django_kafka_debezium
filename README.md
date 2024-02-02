#  Django with Kafka, Debezium, and Faust for Email Sending using Change Data Capture (CDC)


This example demonstrates how to use Django along with Kafka, Debezium, and Faust to send emails triggered by changes in the database through Change Data Capture. 


## Prerequisites
- [Django](https://www.djangoproject.com/)
- [Kafka](https://kafka.apache.org/)
- [Debezium](https://debezium.io/)
- [Faust](https://faust.readthedocs.io/)
  
 
    
## Requirements
You need to install [Docker](https://www.docker.com/)
 and [Docker-Compose](https://docs.docker.com/compose/).

## Build

             docker-compose up -d 
## Migrate databases

             docker-compose exec web python manage.py migrate
#### Createsuperuser

             docker-compose exec web python manage.py createsuperuser
