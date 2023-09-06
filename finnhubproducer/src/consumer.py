from kafka import KafkaConsumer
import json
consumer = KafkaConsumer(
            'stocks',
            bootstrap_servers='kafka:29092',
            auto_offset_reset='earliest',
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)
topic_name='stocks'
consumer.subscribe(topics=[topic_name])
consumer.subscription()
for message in consumer:
      print ("%s:%d:%d: key=%s value=%s\n" % 
             (message.topic, message.partition,message.offset, 
              message.key, message.value))

# from snakebite.client import Client


# client = Client('localhost', 9000)

# for x in client.ls(['/']):
#     print (x)
