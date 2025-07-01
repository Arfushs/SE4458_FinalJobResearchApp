from pymongo import MongoClient

# MongoDB bağlantı cümleni buraya yapıştır (şifreni gizli tut)
MONGO_URL = "mongodb+srv://admin:admin123@cluster0.aq9yqcw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URL)

# "jobsearch" isimli veritabanını kullan
db = client["jobsearch"]

# Koleksiyonlara erişim
searches_collection = db["searches"]
alerts_collection = db["alerts"]
jobs_collection = db["jobs"]  # iş ilanlarını da MongoDB'de tutacağız
