import redis

def get_redis(): #def of fuunction  imported redis for strong caching and keyvalue storing of cahced data
    return redis.Redis(host = "redis", port =6379, decode_response = True)
    #connection to redis host and default port of 6379

    