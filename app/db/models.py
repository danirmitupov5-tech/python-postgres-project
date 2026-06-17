from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base


class Category(Base):
    """Модель для таблицы categories"""
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True, index=True)

    # Связь с книгами (один ко многим)
    books = relationship("Book", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, title='{self.title}')>"


class Book(Base):
    """Модель для таблицы books"""
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    url = Column(String, nullable=True, default='')
    
    # Внешний ключ на таблицу categories
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    # Связь с категорией
    category = relationship("Category", back_populates="books")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', price={self.price})>"