from typing import Optional, List
from pydantic import BaseModel, validator
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# create 'Base' to save the 'declarative_base'
# this is the models of SQLAlchemy

Base = declarative_base()

# setting the Pydantic models for data entry into the API

# Pydantic Models

class CategoryCreate(BaseModel):
    id: Optional[int]
    name: str
    
    
class ProductCreate(BaseModel):
    id: Optional[int]
    name: str
    desc: Optional[str]
    category_id: int
    
# SQLAlchemy models to represent the tables in the database

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    products = relationship("Product", back_populates='category')

    
class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    desc = Column(String, nullable=True)
    
    category_id = Column(Integer, ForeignKey('category.id'))
    
    category = relationship("Category", back_populates="products")
    