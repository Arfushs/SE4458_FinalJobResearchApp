from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class JobBase(BaseModel):
    position: str
    company: str
    city: str
    town: Optional[str] = None
    description: str
    updated_at: Optional[datetime] = None
    application_count: Optional[int] = 0

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: str

class JobSearch(BaseModel):
    city: Optional[str] = None
    position: Optional[str] = None
    town: Optional[str] = None
    work_type: Optional[str] = None


class JobApply(BaseModel):
    user_id: str
    job_id: str

class JobAlert(BaseModel):
    user_id: str
    city: Optional[str] = None
    position: Optional[str] = None

class SearchHistory(BaseModel):
    user_id: str
    query: str
    timestamp: Optional[datetime] = None
