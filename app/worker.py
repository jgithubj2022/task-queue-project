#processes jobs
#workers consume job from task_queue
#producers push to task queue

import json
from client_redis import get_redis
import time

r = get_redis()
QUEUE_KEY = "task_queue"

def do_work(job): #task here to add number provided by itself
    x = job["x"]
    return {"id" : job["id"], "result" : x + x}

def cache_result(job_id,value,ttl=120): #lasts 120 seconds
    r.setex(f"result:{job_id}", ttl, json.dumps(value))

def main():
    print("[WORKER READY] Waiting for task... ;")
    while True:
        _, job_raw = r.brpop(QUEUE_KEY, timeout = 0)
        job = json.loads(job_raw)
        job_id = job["id"]

        r.publish("events", json.dumps({"type" : "job.started", "job_id" : job_id}))
        try:
            result = do_work(job)
            cache_result(job_id,result)
            r.publish("events", json.dumps({"type" : "job.succeeded", "job_id": job_id}))
            print(f"[DONE] {job_id} -> {result}")
        except Exception as e:
            r.publish("events",json.dumps({"type" : "job.failed", "job_id" : job_id}))
            #"aftertype "is a key, "jobfailed" is a string liter, "job_id" is a key, and job_id is a var for value
            print(f"[ERROR] {job_id} : {e}")
    if __name__ == "__main__":
        main()