from redis import Redis

cache = Redis(host='redis', port=6379)
cache.incr(name="times", amount= 1)
print(cache.get("times"))


