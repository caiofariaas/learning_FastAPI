from fastapi import FastAPI, HTTPException
from typing import Optional, List
from models import Car, carColor, carModel

from uuid import uuid1
from pydantic import BaseModel

app = FastAPI()

db: List[Car] = [
    Car(
        id = 1,
        owner='Caio Farias',
        model= carModel.civic,
        color= carColor.preto
        
        )
]

@app.get('/')
async def root():
    return {'hello': 'world'}

@app.get('/api/v1/users')
async def fetch_users():
    return db

@app.post('/api/v1/add_car', response_model=Car)
async def add_car(car: Car):
    Car.id = str(uuid1())
    db.append(car)
    
    return car

@app.delete('/api/v1/car/{car_id}')
async def delete_car(car_id: int):
    # Assuming db is a list of Car objects
    car_to_delete = None
    
    for car in db:
        if car.id == car_id:
            car_to_delete = car
            break
    
    if car_to_delete:
        db.remove(car_to_delete)
        return {"message": "Car deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Car not found")