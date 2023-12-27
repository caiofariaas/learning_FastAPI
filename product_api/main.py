from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models import *
from database import *

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
@app.post('/api/v2/create_category', response_model=CategoryCreate)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    
    # Convertendo o modelo pydantic para SQLAlchemy
    
    db_category = Category(**category.dict())
    
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.post('/api/v2/create_product', response_model=ProductCreate)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return db_product

@app.get('/api/v2/products', response_model=List[ProductCreate])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    
    return products
    

@app.get('/api/v2/categories',response_model=List[CategoryCreate])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    
    return categories

# @app.put('/api/v2/update_product/{prod_id}', response_model=ProductCreate)
# def update_user(prod_id: int, prod_update: ProductCreate, db: Session = Depends(get_db)):
    
#     db_prod = db.query(Product).filter(Product.id == prod_id).first()
    
#     if not db_prod:
#         raise HTTPException(status_code=404, detail='Product not found')
    
#     for key, value, in prod_update.dict().items():
#         setattr(db_prod, key,  value)
        
#     db.commit()
#     db.refresh(db_prod)
    
#     return db_prod

@app.delete('/api/v2/delete_product/{prod_id}')
def delete_product(prod_id: int, db: Session = Depends(get_db)):
    
    db_prod = db.query(Product).filter(Product.id == prod_id).first()
    
    if db_prod:
        db.delete(db_prod)
        db.commit()
        return{'message': f'product with id {prod_id} deleted', "Deleted_product": db_prod }
    
    else:
        raise HTTPException(status_code=404, detail="Product Not Found")
    
@app.delete('/api/v2/delete_category/{categ_id}')
def delete_category(categ_id: int, db: Session = Depends(get_db)):
    
    db_categ = db.query(Category).filter(Category.id == categ_id).first()
    
    if db_categ:
        
        db.delete(db_categ)
        db.commit()
        
        return{'message': f'category with ID {categ_id} deleted', 'Deleted_category': db_categ}
    
    else:
        raise HTTPException(status_code=404, detail='category not found')

