from hostel.celery import app

from .funk_otchet import send

@app.task
def send_spam_send(user_email, name):
    send(user_email, name)

