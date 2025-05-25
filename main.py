from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sajikan file statis (HTML, CSS, JS)
app.mount("/website", StaticFiles(directory="website"), name="website")

@app.get("/")
def serve_homepage():
    return FileResponse("website/index.html")

# Data dummy pelampung
dummy_floaters = [
    {"mac_address": "AA:BB:CC:DD", "position": {"lat": 1.1, "lng": 2.2}, "id": 1},
    {"mac_address": "EE:FF:GG:HH", "position": {"lat": 3.3, "lng": 4.4}, "id": 2}
]

@app.get("/floaters_position")
def get_floaters_position():
    return dummy_floaters

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

class Device(BaseModel):
    mac_address: str

@app.post("/last_log")
def get_sensor_data(device: Device):
    return {
        "mac_address": device.mac_address,
        "sensor": "simulated data",
        "value": 99.9
    }
