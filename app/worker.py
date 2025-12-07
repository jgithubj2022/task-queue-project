#processes jobs
import json
import time
from client_redis import get_redis

r = get_radis() #set get_redis to member variable

QUEUE_KEY = "trasks_queue"
CACHE_PREFIX = "result:"#so before our chached results shows result

def cache_get(job_id):#retrieves a value from redis using key
    return r.get(f"{CACHE_PREFIX}{job_id}")
    #if the redis doesnt return none it returns result: our job id!

def cache_set(job_id,value,ttl=60):
    r.setex(f"{CACHE_PREFIX}{job_id}", )