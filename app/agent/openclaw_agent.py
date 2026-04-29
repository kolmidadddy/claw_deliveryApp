class OpenClawAgent:
    def process(self, message: str):
        if "delivery" in message.lower():
            return {
                "intent": "create_delivery",
                "data": {
                    "customer_name": "ABC Sdn Bhd",
                    "customer_code": "C001",
                    "delivery_date": "2026-05-01",
                    "delivery_address": "Petaling Jaya",
                    "items": "3 boxes",
                    "itemCode": "ITM001",
                    "attn_name": "John",
                    "attn_num": "0123456789",
                    "vehicle_type": "van"
                }
            }

        return {"intent": "unknown", "data": {}}

# class OpenClawAgent:
#     def __init__(self):
#         # initialize your OpenClaw client / config here
#         pass

#     def process(self, message: str):
#         # Step 1: Send message to OpenClaw (LLM / workflow)
#         # Step 2: Extract structured data
#         # Step 3: Decide what to do

#         print(f"Received message: {message}")

#         # TEMP mock logic (replace later with real OpenClaw)
#         if "delivery" in message.lower():
#             return {
#                 "intent": "create_delivery",
#                 "data": {
#                     "customer_name": "Test",
#                     "customer_code": "C001",
#                     "delivery_date": "2026-05-01",
#                     "delivery_address": "PJ",
#                     "items": "Boxes",
#                     "itemCode": "ITM01",
#                     "attn_name": "John",
#                     "attn_num": "0123456789",
#                     "vehicle_type": "van"
#                 }
#             }

#         return {"intent": "unknown"}

