from fastapi import FastAPI
from app.routes import router
from app.agent.openclaw_agent import OpenClawAgent
from app.models import DeliveryRequest
from app.service import create_delivery

app = FastAPI(title="Delivery Booking System")

app.include_router(router)

openclaw_agent = OpenClawAgent()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(payload: dict):
    message = payload["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

    agent_response = openclaw_agent.process(message)

    if (
        agent_response.get("intent") == "create_delivery"
        and isinstance(agent_response.get("data"), dict)
    ):
        try:
            data = DeliveryRequest(**agent_response["data"])
            create_delivery(data)
        except Exception as e:
            print("Validation error:", e)

    return {"status": "ok"}