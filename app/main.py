from fastapi import FastAPI
from app.routes import delivery

app = FastAPI(title="Delivery Booking System")

# Register routes
app.include_router(delivery.router)

@app.get("/")
def root():
    return {"message": "API is running"}