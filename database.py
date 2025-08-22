from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    products: Mapped[List["Product"]] = relationship(back_populates="category") 

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="products") 

engine = create_engine("sqlite:///./goods.db", echo=False)
Base.metadata.create_all(engine)


















