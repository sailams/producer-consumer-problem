import redis
import time
import sys
import random
from datetime import datetime

def producer():
    r = redis.Redis()

    random.seed(datetime.now())

    while True:
        i = random.randint(1,123)
		r.rpush('queue',i)
        time.sleep(1)

if __name__ == '__main__':
    print("Starting producer: ")
    producer()