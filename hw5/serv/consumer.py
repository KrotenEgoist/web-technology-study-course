from kafka import KafkaConsumer
import time
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
consumer = KafkaConsumer('task_queue')
redis = redis.Redis(connection_pool=pool)

for message in consumer:
    print(message)
    redis.set('task "{message}"', 'accepted')
    time.sleep(5)
    redis.set('task "{message}"', 'done')