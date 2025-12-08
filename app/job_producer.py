#creates jobs
import json
import time
from client_redis import get_redis

r = get_radis() #set get_redis i made in client_redis variable

QUEUE_KEY = "trasks_queue"
CACHE_PREFIX = "result:"#so before our chached results shows result

def cache_get(job_id):#retrieves a value from redis using key
    return r.get(f"{CACHE_PREFIX}{job_id}")
    #if the redis doesnt return none it returns result: our job id!

def cache_set(job_id,value,ttl=60):
    r.setex(f"{CACHE_PREFIX}{job_id}", ttl, json.dumps(value))
    #setex member function of redis sets a string value for a key 
    #and sets a TTL expiration time in seconds I.E this is 60 seconds
    #converts python object into json string format. since redi can only store strings so anytime you want to store a dict, list or object i must convert
def enqeueu(job):
    r.lpush(QUEUE_KEY,json.dump(job))#lpush add to beginning of list
    r.publish("events",json.dumps({"type": "job.enqueued", "job_id": job["id"]}))

if __name__ == "__main__":
    for i in range(1,6):#makes 5 jobs and queues
        job = { #dictionary object for id tasks and number of jobs
            "id" : f"job-{i}",#id identifer for job
            "task": "square",
            "x" : i#job number in term of loop
        }#below if cached alrdy skip cacheing process
        if (cache_get(job["id"])):#if when cache_get is called job has id
            print(f"[CACHE HIT] {job['id']}")
            continue

        enqueue(job)
        print(f"[ENQUEUED] {job['id']}")
        time.sleep(0.5)

        