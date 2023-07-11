# Build a website using React, Python, DJANGO & MYSQL(RPDM)
DevOps approach towards building a webshop using RPDM. "You build it, you run it culture"

# steps

- 1) One Build the website and Test it locally 
- 2) Package it into a container
- 3) Deploy and host it on AWS or Hetzner as a microservice
- 4) Create a domain & Setup a load balancer
``
## I
Install Python, mysql, nodejs and django module on venv
Postman to test your API - ( curl -o- "https://dl-cli.pstmn.io/install/linux64.sh" | sh)

* pip install django
* pip install djangorestframework
* pip install django-cors-headers 
* django-admin startproject fruitboss // cd fruitboss
* python manage.py runserver ## to run a test server

##  II - build an application
* python manage.py startapp EmployeeApp
> go to settings.py under INSTALLED_APPS add 'rest_framework, corsheaders, and EmployeeApp(the newly created app)

## III - create your models
* Create your models in employeeApp models.py
* install pip install pymysql to connect to the mysql DB
> Then add the database connecting in settings.py
* pip install pymysql
* python3 manage.py makemigrations EmployeeApp
* pip install cryptography #for mysql sql caching_sha2_password authentication test#
##  IV - Migrate Database
* python manage.py migrate EmployeeApp
| Add employeeApp.serializer.py for the python data -> <By convertin an object or data structure into a format that can be store or transmitted and later reconstructed>
 - Add EmployeeApp.urls, EmployeeApp.views.py
* python manage.py runserver ## to run a built server
* Test again - python manage.py runserver

## V - Test API using Postman