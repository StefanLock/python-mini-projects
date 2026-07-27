from fastapi import FastAPI
from redis import Redis
from rq import Queue
import os

from tasks import long_running_task

# Use an environment variable, falling back to 'redis' for Docker
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
redis_conn = Redis(host=REDIS_HOST, port=6379)
task_queue = Queue("default", connection=redis_conn)
    
app = FastAPI()

@app.post("/enqueue-task/", status_code=202)
def enqueue_task(payload: dict):
    job = task_queue.enqueue(long_running_task, payload)
    return {"message": "Task enqueued", "job_id": job.id}