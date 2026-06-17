from sqlalchemy.orm import Session
from app.db import models


# ============ CREATE (Создание) ============

def create_category(db: Session, title: str):
    """Создание новой категории"""
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ''):
    """Создание новой книги"""
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# ============ READ (Чтение) ============

def get_category(db: Session, category_id: int):
    """Получение категории по ID"""
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_category_by_title(db: Session, title: str):
    """Получение категории по названию"""
    return db.query(models.Category).filter(models.Category.title == title).first()

def get_all_categories(db: Session):
    """Получение всех категорий"""
    return db.query(models.Category).all()

def get_book(db: Session, book_id: int):
    """Получение книги по ID"""
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books_by_category(db: Session, category_id: int):
    """Получение всех книг по категории"""
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()

def get_all_books(db: Session):
    """Получение всех книг"""
    return db.query(models.Book).all()


# ============ UPDATE (Обновление) ============

def update_category(db: Session, category_id: int, new_title: str):
    """Обновление названия категории"""
    category = get_category(db, category_id)
    if category:
        category.title = new_title
        db.commit()
        db.refresh(category)
    return category

def update_book(db: Session, book_id: int, **kwargs):
    """Обновление данных книги"""
    book = get_book(db, book_id)
    if book:
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book


# ============ DELETE (Удаление) ============

def delete_category(db: Session, category_id: int):
    """Удаление категории"""
    category = get_category(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category

def delete_book(db: Session, book_id: int):
    """Удаление книги"""
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book