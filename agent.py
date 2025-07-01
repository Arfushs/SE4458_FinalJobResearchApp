from fastapi import APIRouter

router = APIRouter()

@router.post("/agent")
def agent_response(message: dict):
    query = message.get("message", "").lower()

    # Basit cevaplar
    if "web" in query and "istanbul" in query:
        return {
            "response": [
                {
                    "position": "Frontend Developer",
                    "company": "Company A",
                    "city": "Istanbul"
                },
                {
                    "position": "Junior Web Developer",
                    "company": "Company B",
                    "city": "Istanbul"
                }
            ]
        }
    else:
        return {"response": "Üzgünüm, uygun iş bulamadım."}
