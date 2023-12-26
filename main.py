# Importações necessárias do FastAPI, SQLAlchemy e modelos definidos

from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models import Base, UserCreate, ItemCreate, User, Item
from database import engine, SessionLocal

# Criação de uma instância FastAPI

app = FastAPI()

# Criação das tabelas no banco de dados usando o SQLAlchemy

Base.metadata.create_all(bind=engine)

# Função para obter a sessão do banco de dados

def get_db():
    
# Cria uma instância da sessão do banco de dados usando SessionLocal()
   
    db = SessionLocal()  
    try:
        
# Retorna a sessão para o chamador da função como um gerador

        yield db  
    finally:
        
# Fecha a sessão do banco de dados no final do bloco `try` ou após a conclusão do gerador

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
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item) 
    return db_item

# Método GET para todos os usuários
# O 'Session' refere-se a sessão do banco de dados
# 'Depends' gerencia dependencias em rotas, usado para obter uma intancia de sessão de banco
# O código dentro da função de dependência (get_db) é executado antes da execução da função da rota.
# A instância criada pela função de dependência é injetada como argumento na função da rota.

@app.get("/api/users", response_model=List[UserCreate])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.put('/api/uptade_user/{user_id}', response_model=UserCreate)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    
    for key, value, in user_update.dict().items():
        setattr(db_user, key, value)
        
    db.commit()
    db.refresh(db_user)
    
    return db_user