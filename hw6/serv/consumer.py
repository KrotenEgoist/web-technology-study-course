from kafka import KafkaConsumer
import time
import redis
from circuitbreaker import circuit
from healthcheck import HealthCheck


def redis_correct():
    redis_ = redis.Redis(connection_pool=pool)


@circuit
def set_pool():
    return redis.ConnectionPool(host='localhost', port=6379, db=0)


def main():
    consumer = KafkaConsumer('task_queue')
    redis_ = redis.Redis(connection_pool=pool)
    health.add_check(redis_correct)
    health.run()
    for message in consumer:
        print(message)
        redis_.set(f'task "{message}"', 'accepted')
        time.sleep(10)
        redis_.set(f'task "{message}"', 'done')


pool = set_pool()
main()
