import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_job(job_id: str):
    cached = r.get(f"job:{job_id}")
    if cached:
        return json.loads(cached)
    return None

def set_cached_job(job_id: str, job_data: dict, ttl: int = 3600):
    r.set(f"job:{job_id}", json.dumps(job_data), ex=ttl)
