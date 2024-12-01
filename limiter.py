import redis


class Limiter:
    def __init__(self, host='localhost', port=6379, limit_pm=20):
        self.redis = redis.StrictRedis(host=host, port=port, decode_responses=True)
        self.limit_pm = limit_pm

    def limit(self, key):
        if self.redis.exists(key):
            count = int(self.redis.get(key))
            if count < self.limit_pm:
                self.redis.incr(key) # increment the key
                return True
            else:
                return False
        else:
            self.redis.set(key, 1) # set the key, here we could also set an expiry time but i want to erase all the keys at fixed intercals, so i used a cron job
            return True