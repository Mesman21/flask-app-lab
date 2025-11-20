from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, ForeignKey, Boolean


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"


class Product(db.Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)

    # Нове поле (Частина 4)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id'), nullable=True)
    category: Mapped["Category"] = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name}>"