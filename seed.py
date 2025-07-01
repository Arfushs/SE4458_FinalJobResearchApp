from pymongo import MongoClient
from datetime import datetime
import random

MONGO_URL = "mongodb+srv://admin:admin123@cluster0.aq9yqcw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client["jobsearch"]
jobs = db["jobs"]
jobs.delete_many({})  # önce tüm ilanları sil

cities = ["Izmir", "Istanbul", "Ankara", "Bursa", "Antalya"]
towns = {
    "Izmir": ["Konak", "Bornova", "Karşıyaka"],
    "Istanbul": ["Kadikoy", "Sisli", "Besiktas"],
    "Ankara": ["Cankaya", "Kecioren", "Yenimahalle"],
    "Bursa": ["Osmangazi", "Nilufer", "Yildirim"],
    "Antalya": ["Muratpasa", "Konyaalti", "Kepez"]
}
positions = [
    "React Developer", "Frontend Developer", "Backend Developer",
    "Full Stack Developer", "Mobile Developer", "Web Developer",
    "DevOps Engineer", "QA Tester", "Data Analyst",
    "Project Manager", "UI/UX Designer", "AI Engineer",
    "ML Engineer", "Cyber Security Analyst", "Java Developer",
    "Python Developer", "Golang Developer", "Flutter Developer",
    "React Native Developer", "Cloud Engineer", "IT Support",
    "System Admin", "Database Admin", "Product Manager", "Intern"
]

work_types = ["Remote", "Onsite", "Hybrid"]

sample_jobs = []
for i in range(25):
    city = "Izmir" if i < 5 else random.choice(cities)
    town = random.choice(towns[city])
    job = {
        "position": positions[i],
        "company": f"Company {chr(65 + i)}",
        "city": city,
        "town": town,
        "work_type": random.choice(work_types),
        "description": f"{positions[i]} pozisyonu için iş ilanı.",
        "updated_at": datetime.utcnow(),
        "application_count": random.randint(0, 10)
    }
    sample_jobs.append(job)

jobs.insert_many(sample_jobs)
print("✅ 25 iş ilanı başarıyla eklendi (town & work_type dahil)")
