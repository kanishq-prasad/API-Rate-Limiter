# this file is run by the cron job to reset the counter

import redis


def reset_counters():
    redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    keys = redis_client.keys('*')
    print("keys:")
    print(keys)
    for key in keys:
        redis_client.delete(key)
    return True

if __name__ == '__main__':
    reset_counters()
