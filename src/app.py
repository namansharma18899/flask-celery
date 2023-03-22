# from flask import Flask
# from src.celery import celery_init_app

# app = Flask(__name__)
# app.config.from_mapping(
#     CELERY=dict(
#         broker_url="redis://localhost",
#         result_backend="redis://localhost",
#         task_ignore_result=True,
#     ),
# )
# celery_app = celery_init_app(app)

from celery import Celery
from flask import Flask

app = Flask(__name__)

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@app.route("/")
def hello():
    return "Hello, World!"


@celery.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y