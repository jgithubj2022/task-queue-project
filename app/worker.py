#processes jobs
#workers consume job from task_queue
#producers push to task queue

import json
import client_redis import get_redis
import time

r = get_redis()
QUEUE_KEY = "task_queue"

def do_work(job): #task here to add number provided by itself
    x = job["x"]
    return {"id" : job["id"], "result" : x + x}

