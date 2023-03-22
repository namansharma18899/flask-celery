# flask-celery
## Table of Contents
* [Setup](#setup)
* [Usgae](#usage)
## Setup
* Must have docker damen on your system installed
* Run the redis docker image
```
docker run -p 6379:6379 --name some-redis -d redis
```
* Install the dependencies in a virtualenv. (Create one if you don't have already)
```
$ cd flask-celery
$ virtualenv TestEnv
$ pip3 install -r requirements.txt
$ cd src/
$ FLASK_APP=app.py flask shell  #seperate_terminal
$ celery -A app.celery worker --loglevel=info #seperate_terminal
$ celery -A app.celery flower --port=5555 #seperate_terminal
```
## Usage
* Create new tasks in the flask shell 
$ from app import divide
$ task = divide.delay(1, 2)
$ print(task.state)
$ SUCCESS
* See the State of the tasks in runtime at the Flower dashboard
```
$ http://localhost:5555
```
![Flower Dashboard](https://github.com/namansharma18899/flask-celery/src/assets/flower.png?raw=true)