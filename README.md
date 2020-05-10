https://flask.palletsprojects.com/en/1.1.x/tutorial/

pip install flask pytest coverage
pip install -e . # installs project


export FLASK_APP=flaskr && export FLASK_ENV=development && flask run



## Using Celery for background tasks

This would normally be done with docker-compose?

### Manual

From inside flaskr

    # start redis in the background
    docker run -d -p 6379:6379 redis

    # start celery worker
    celery -A celery_ref worker -l info

    # start celery client
    # done by celery_ref/celery.py

    # test
    python
    from celery_ref import tasks
    res = tasks.add.delay(1,1)
    res.ready() # True
    res.get(timeout=1) # 2

### With app

    # start redis in the background
    docker run -d -p 6379:6379 redis

    # start celery worker
    celery worker -l info -A flaskr.tasks

    # start celery client
    # (started by flask via app.py + tasks.py)
    export FLASK_APP=flaskr && export FLASK_ENV=development && flask run

    # test
    visit http://127.0.0.1:5000/celery-check
    That should log in celery