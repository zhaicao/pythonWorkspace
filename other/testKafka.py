import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='10.202.228.30:9092')

msg_dict = {
    "sleep_time": 10,
    "db_config": {
        "database": "test_1",
        "host": "123",
        "user": "root",
        "password": "root"
    },
    "table": "msg",
    "msg": "Hello World"
}
msg = json.dumps(msg_dict)
print(type(msg))
producer.send("test_zc", b'test')
producer.close()