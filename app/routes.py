from fastapi import APIRouter
from app.models import DeliveryRequest
from app.service import create_delivery

router = APIRouter(prefix="/delivery", tags=["Delivery"])

@router.post("/")
def create_delivery_endpoint(data: DeliveryRequest):
    result = create_delivery(data)
    return {"status": "success", "message": result}