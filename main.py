# Importações necessárias do FastAPI, SQLAlchemy e modelos definidos

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, UserCreate, ItemCreate, User, Item
from database import engine, SessionLocal

# Criação de uma instância FastAPI

app = FastAPI()

# Criação das tabelas no banco de dados usando o SQLAlchemy

Base.metadata.create_all(bind=engine)

# Função para obter a sessão do banco de dados

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Definição de rotas da API

# Rota para criar um usuário

@app.post("/api/create_user", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    
    # Converte o modelo Pydantic UserCreate em uma instância da classe SQLAlchemy User
    
    db_user = User(**user.dict())
    
    # Adiciona o usuário ao banco de dados
    
    db.add(db_user)
    
    # Confirma as alterações no banco de dados
    
    db.commit()
    
    # Atualiza a instância do usuário no banco de dados
    
    db.refresh(db_user)
        
    return db_user

# Rota para criar um item

@app.post("/api/create_item", response_model=ItemCreate)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    
    # Converte o modelo Pydantic ItemCreate em uma instância da classe SQLAlchemy Item
    
    db_item = Item(**item.dict())
    
    # Adiciona o item ao banco de dados
    
    db.add(db_item)
    
    # Confirma as alterações no banco de dados
    
    db.commit()
    
    # Atualiza a instância do item no banco de dados
    
    db.refresh(db_item)
        
    return db_item
