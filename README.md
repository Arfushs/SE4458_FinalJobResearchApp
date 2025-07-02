

---

```markdown
# Job Search Platform – SE4458 Final Project

A simple, service-oriented job search platform built using **FastAPI** (backend) and **HTML/CSS/JavaScript** (frontend). This system allows users to search and apply for jobs based on filters like city, district, and work type. The project supports pagination, caching, and containerization via Docker.

---

## 🚀 Features

- 🔍 Filter job listings by city, district, position, and work type
- 📚 Dynamic tag-based filters with removal support
- 🧠 AI Job Assistant (rule-based chatbot using backend agent route)
- 📜 Search history tracking for guest users
- 📩 Application submission via "Apply" button
- 🏙 Auto-load jobs in **Izmir** by default (first 5 shown on page load)
- 📦 Pagination support
- 🗂 Distributed caching implemented for job detail
- 🖼 Modal + separate job detail page views
- 🐳 Dockerfile for container-based deployment

---

## 🧱 Architecture

```

📦 app/
├── main.py                → FastAPI entry point
├── crud.py                → Business logic (CRUD operations)
├── database.py            → MongoDB connection
├── schemas.py             → Pydantic models
├── seed.py                → Initial job data seeding
├── static/
│   ├── index.html         → Main frontend interface
│   ├── style.css          → CSS styling
│   └── job\_detail.html    → Separate job detail page

````

---

## ⚙️ Setup Instructions

### 1. Requirements

- Python 3.10 or higher
- MongoDB (local or [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))
- Run: `pip install -r requirements.txt`

### 2. MongoDB Configuration

Update the connection string inside `database.py`:

```python
client = MongoClient("mongodb+srv://<username>:<password>@<cluster>.mongodb.net")
````

### 3. Seed Initial Job Data

```bash
python seed.py
```

### 4. Run the App

```bash
uvicorn main:app --reload
```

Access the app at: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker Usage

You can containerize the application with:

```bash
docker build -t job-app .
docker run -p 8000:8000 job-app
```

---

## ✅ Requirements Checklist (from Assignment PDF)

| Feature                                 | Status                       |
| --------------------------------------- |------------------------------|
| Functional UI (not identical to mockup) | ✅                            |
| RESTful services for all use cases      | ✅                            |
| Dockerfile (without image)              | ✅                            |
| Distributed Caching (job details)       | ✅                            |
| AI Job Assistant (non-realtime)         | ✅                            |
| Pagination Support                      | ✅                            |
| Cloud deployment (Azure/AWS)            | ⬜ Optional (currently local) |
| Cloud database (MongoDB Atlas)          | ✅                            |
| API Gateway                             | ⬜ Not implemented            |
| Hotel and Notification microservices    | ⬜ Not implemented            |
| Load Testing (Bonus +10 pts)            | ⬜ Not implemented            |

---

## 🔐 API Endpoints (Selected)

* `POST /search` – Search for jobs with filters
* `GET /jobs` – List jobs with pagination
* `POST /jobs` – Add new job
* `POST /apply` – Apply to a job
* `GET /jobs/{id}` – Get job details (with cached result)
* `GET /searches/{user_id}` – Get search history
* `POST /alerts` – Create job alert
* `POST /agent` – Ask AI Job Assistant

---

## 👤 Developer

**Arfus**

```

```
