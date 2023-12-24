from pydantic import BaseModel
from typing import Optional
from enum import Enum

class carModel(str, Enum):
    civic = 'civic 1994 V-TEC'
    uno95 = 'Uno 1995'
    corolla = 'corolla XEI'
    meca = 'Mercedes GT 63s'
    
class carColor(str, Enum):
    preto = 'preto'
    azul = 'azul'
    branco = 'branco'
    cinza = 'cinza'
    vermelho = 'vermelho'
    
class Car(BaseModel):
    id: int
    owner: str
    model: carModel
    color: carColor
    