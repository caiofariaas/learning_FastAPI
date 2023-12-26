# Importações necessárias do SQLAlchemy e Pydantic

from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Criação da base para modelos do SQLAlchemy

Base = declarative_base()

# Definição de modelos Pydantic para entrada de dados na API

# Modelo Pydantic para criar um usuário

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: Optional[str]

# Modelo Pydantic para criar um item

class ItemCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    owner_id: int

# Definição de modelos SQLAlchemy para representar tabelas no banco de dados

# Modelo SQLAlchemy para a tabela 'items'

class Item(Base):
    __tablename__ = 'items'
    
# 'primary_key' garante que o valor dessa coluna será unico
# Por isso o usamos em 'id'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    
# owner_id é uma coluna que tem um valor inteiro
# 'ForeignKey("users.id")' indica que essa coluna é uma chave que faz referencia a coluna 'id' da tabela 'users'
# ou seja, ela armazena ID's de usuários da tabela 'users' 

    owner_id = Column(Integer, ForeignKey("users.id"))
    
# é um atributo que representa esse relacionamento com objetos da classe 'User'
# 'relationship' indica que a um relaionamento entre a tabela 'Item e a tabela 'User'
# 'back_populates='items'' especifica que existe um atributo correspondente na classe 'User'
    
    owner = relationship("User", back_populates="items")

# Modelo SQLAlchemy para a tabela 'users'

class User(Base):
   
# Define o nome da tabela no banco
    
    __tablename__ = 'users'
   
# Colunas
   
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    full_name = Column(String)

    # Relacionamento com a tabela 'items'
    
    items = relationship("Item", back_populates="owner")
