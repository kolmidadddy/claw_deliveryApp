from fastapi import APIRouter
from app.models.delivery import DeliveryRequest
from app.services.delivery_services import create_delivery

router = APIRouter(prefix="/delivery", tags=["Delivery"])

@router.post("/")
def create_delivery_endpoint(data: DeliveryRequest):
    result = create_delivery(data)
    return {"status": "success", "message": result}