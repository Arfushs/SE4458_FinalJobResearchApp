from apscheduler.schedulers.background import BackgroundScheduler
from database import alerts_collection, jobs_collection
from datetime import datetime

def check_alerts():
    print("[Bildirim] Yeni iş ilanları kontrol ediliyor...")
    alerts = alerts_collection.find()
    jobs = list(jobs_collection.find())

    for alert in alerts:
        for job in jobs:
            if alert.get("city", "").lower() in job.get("city", "").lower():
                print(f"🔔 {alert['user_id']} kullanıcısı için eşleşen ilan: {job['position']} - {job['city']}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_alerts, "interval", minutes=5)
    scheduler.start()
