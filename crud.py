from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId
from database import jobs_collection, searches_collection, alerts_collection
from schemas import JobCreate, JobSearch, JobApply, JobAlert, SearchHistory
from fastapi import Body
from fastapi import Request

router = APIRouter()


@router.post("/jobs")
def create_job(job: JobCreate):
    job_dict = job.dict()
    job_dict["updated_at"] = datetime.utcnow()
    job_dict["application_count"] = 0
    result = jobs_collection.insert_one(job_dict)
    return {"id": str(result.inserted_id), **job_dict}


@router.get("/jobs")
def list_jobs():
    jobs = list(jobs_collection.find().limit(10))
    for job in jobs:
        job["id"] = str(job["_id"])
        del job["_id"]
    return jobs


@router.post("/search")
def search_jobs(search: JobSearch, request: Request):
    query = {}

    def normalize(text):
        return text.lower().replace("i", "ı").replace("ı", "i")

    if search.city:
        query["city"] = { "$regex": normalize(search.city), "$options": "i" }
    if search.position:
        query["position"] = { "$regex": normalize(search.position), "$options": "i" }
    if search.town:
        query["town"] = { "$regex": normalize(search.town), "$options": "i" }
    if search.work_type:
        query["work_type"] = { "$regex": normalize(search.work_type), "$options": "i" }

    # Pagination parametreleri URL'den alınır
    page = int(request.query_params.get("page", 1))
    limit = int(request.query_params.get("limit", 10))
    skip = (page - 1) * limit

    # Arama geçmişine kaydet
    searches_collection.insert_one({
        "user_id": "guest",
        "query": f"{search.city or ''} {search.position or ''}",
        "timestamp": datetime.utcnow()
    })

    jobs = list(jobs_collection.find(query).skip(skip).limit(limit))
    for job in jobs:
        job["id"] = str(job["_id"])
        del job["_id"]
    return jobs


@router.post("/apply")
def apply_job(data: JobApply = Body(...)):
    job = jobs_collection.find_one({"_id": ObjectId(data.job_id)})
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    jobs_collection.update_one(
        {"_id": ObjectId(data.job_id)},
        {"$inc": {"application_count": 1}}
    )
    return {"message": "Başvuru başarıyla alındı."}


@router.post("/alerts")
def create_alert(alert: JobAlert):
    alerts_collection.insert_one({
        **alert.dict(),
        "created_at": datetime.utcnow()
    })
    return {"message": "İş alarmı oluşturuldu."}

@router.get("/searches/{user_id}")
def get_search_history(user_id: str):
    history = list(searches_collection.find({"user_id": user_id}).sort("timestamp", -1).limit(5))
    return [h["query"] for h in history]

from cache import get_cached_job, set_cached_job

@router.get("/jobs/{job_id}")
def get_job_detail(job_id: str):
    cached = get_cached_job(job_id)
    if cached:
        return cached

    job = jobs_collection.find_one({"_id": ObjectId(job_id)})
    if not job:
        raise HTTPException(status_code=404, detail="İş bulunamadı.")

    job["id"] = str(job["_id"])
    del job["_id"]

    related = list(jobs_collection.find({
        "_id": { "$ne": ObjectId(job_id) },
        "city": job["city"],
        "position": { "$regex": job["position"].split()[0], "$options": "i" }
    }).limit(3))

    for r in related:
        r["id"] = str(r["_id"])
        del r["_id"]

    result = {
        "job": job,
        "related": related
    }

    set_cached_job(job_id, result, ttl=3600)  # 1 saatlik cache
    return result

