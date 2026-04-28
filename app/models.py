from pydantic import BaseModel

class DeliveryRequest(BaseModel):
    vehicle_type: str | None = None
    customer_name: str
    customer_code: str
    delivery_date: str
    delivery_address: str
    items: str
    itemCode: str
    attn_name: str
    attn_num: str