import redis
import time
import sys

def consumer():
    first_smallest = second_smallest = 0
    r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
    while True:
        val = r.blpop('queue')
        consumed_val = int(val[1])
        if first_smallest == 0:
            first_smallest = consumed_val
        elif consumed_val > first_smallest and consumed_val < second_smallest:
            second_smallest = consumed_val
        elif consumed_val < first_smallest:
            second_smallest = first_smallest
            first_smallest = consumed_val
        print("Consuming: ", val[1])
        if first_smallest == 0 or second_smallest == 0:
           print("Waiting for 2 smallest numbers...")
        else:
           print("Two smallest integers:", first_smallest, second_smallest)

if __name__ == '__main__':
    print("Starting consumer: ")
    consumer()
