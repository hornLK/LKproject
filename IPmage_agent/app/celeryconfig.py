broker_url = 'amqp://kk:123123@localhost:5672/web_dev'
result_backend = "redis://localhost:6379/0"
task_serializer = 'json'
result_serializer = "json"
accept_conten = ['json','msgpack']
timezone = 'Asia/Shanghai'
beat_schedule = {
    'div-30-seconds': {
        'task': 'app.auto_nmap.div',
        'schedule': 30.0,
        'args': (16, 16)
    },
    'namp_host-3600-seconds': {
        'task': 'app.auto_nmap.nmap_host',
        'schedule': 30.0
    }
}
