from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException
from typing import Optional, List

class User(BaseModel):
    username: str
    email: str
    full_name: str = None
    
class Item(BaseModel):
    name: str
    description : Optional[str]
    price: float = None
    tags: List[str] = []
    owner: User
    
# validator is used for do the validation of some thing
    
    @validator('price')
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError('Price must be greater than "0"')
        return value
    