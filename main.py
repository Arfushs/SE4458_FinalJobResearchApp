from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from crud import router as job_router
from agent import router as agent_router
from scheduler import start_scheduler

app = FastAPI()

# API router'larını dahil et
app.include_router(job_router)
app.include_router(agent_router)

# CORS (Frontend'den erişim için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # localde geliştirirken hepsi açık
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Frontend klasörünü serve et
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# Zamanlayıcı başlat (bildirim servisi)
@app.on_event("startup")
def startup_event():
    start_scheduler()
