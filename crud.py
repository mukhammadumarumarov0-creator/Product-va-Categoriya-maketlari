from sqlalchemy.orm import Session,joinedload
from database import engine
from sqlalchemy import select
from database import Category,Product


def read_categories():
    with Session(engine) as sess:
        stmt=select(Category).options(joinedload(Category.products))
        categoties=sess.scalars(stmt).unique().all()
        return categoties

def read_category(category_id):
    with Session(engine) as sess:
        stmt=select(Category).where(Category.id==category_id).options(joinedload(Category.products))
        category=sess.scalar(stmt)
        return category
        
def create_category(category_name):
    with Session(engine) as sess:
        category=Category(name=category_name)
        
        sess.add(category)
        sess.commit()
        sess.refresh(category)
        return category

def update_category(category_id:int,name):
    with Session(engine) as sess:
      category=sess.get(Category,category_id)
      category.name=name
      
      sess.commit()
      sess.refresh(category)
      return category
      
def delete_category(category_id:int):
    with Session(engine) as sess:
      category=sess.get(Category,category_id)
      sess.delete(category)

      sess.commit()
      sess.refresh(category)




def create_product(name:str,category_id:int):
    with Session(engine) as sess:
        product=Product(
            name=name,
            category_id=category_id
            )

        sess.add(product)
        sess.commit()
        sess.refresh(product)
        return product   

def read_products():
    with Session(engine) as sess:
     stmt=select(Product).options(joinedload(Product.category))
     products=sess.scalars(stmt).unique().all()
     return products

def read_product(product_id):
    with Session(engine) as sess:
        stmt=select(Product).where(Product.id==product_id).options(joinedload(Product.category))
        product=sess.scalar(stmt)
        return product
    
def update_product_name(product_id,name):
    with Session(engine) as sess:
        product=sess.get(Product,product_id)
        product.name=name

        sess.commit()
        sess.refresh(product)
        return product

def update_product_category(product_id,category_id):
    with Session(engine) as sess:
        product=sess.get(Product,product_id)
        product.category_id=category_id

        sess.commit()
        sess.refresh(product)
        return product

def delete_product(product_id):
    with Session(engine) as sess:
        product=sess.get(Product,product_id)
        sess.delete(product)

        sess.commit()
        sess.refresh(product)