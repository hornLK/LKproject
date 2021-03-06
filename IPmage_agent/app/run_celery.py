from celery import Celery

app = Celery('app',include=['app.auto_nmap'])
app.config_from_object('app.celeryconfig')

if __name__ == "__main__":
    app.start()

