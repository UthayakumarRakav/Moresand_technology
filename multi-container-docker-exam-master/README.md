
# Multi-container-docker-setup
This is a multi-container simple program by integrating flask, nginx and postgresql in a docker environment

# Components
- helloapp : python flask app which is used to submit messages and show the list of messages avaialble in the database
- postgres : postgresql database which hold the messages table 
- proxy: exposing the hello app output to the public using reverse proxy

# prerequisite
you already have installed docker into your local system

# Exam tasks
# task 1 :
 Clone this project into your local environment and start this application. You can see the message data is not persistance over restarts of this setup. Do changes the persist the data over restarts.  (data directory for Postgres database denoted by PGDATA environment variable.) 

# task 2 :
 implement nginx reverse proxy configuration on ./nginx/default.conf file which expose helloapp to public and add nginx component to the docker-compose.yaml (http://localhost should route the trafic to helloapp application) 


