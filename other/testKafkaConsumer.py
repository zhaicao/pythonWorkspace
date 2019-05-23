from kafka import KafkaConsumer

consumer = KafkaConsumer('test_zc', bootstrap_servers=['10.202.228.30:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)