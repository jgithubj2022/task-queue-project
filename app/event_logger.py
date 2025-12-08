import json
from client_redis import get_redis

r = get_redis()
channel = "events"
pubsub = r.pubsub()
pubsub.subscribe(channel)

print(f"[EVENTS LOGGER] Logging on channel '{channel}'...")
for message in pubsub.listen():
    if message["type"] == "message":
        data = json.loads(message["data"]) 
        event_type = data.get("type")
        job_id = data.get("job_id")
        print(f"[EVENT] {event_type}-> {job_id}")