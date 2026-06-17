import sys
import os

# Добавляем корневую папку в путь (чтобы работали импорты)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal, create_tables
from app.db.crud import create_category, create_book


def init_database():
    """Инициализация базы данных"""
    
    print("=" * 60)
    print("НАЧАЛО ИНИЦИАЛИЗАЦИИ БАЗЫ ДАННЫХ")
    print("=" * 60)
    
    # Создаем таблицы
    print("\n📋 Создание таблиц...")
    create_tables()
    print("✅ Таблицы созданы!")
    
    db = SessionLocal()
    
    try:
        # ===== Добавляем категории =====
        print("\n📚 Добавление категорий...")
        
        categories = ['Программирование', 'Художественная литература']
        category_ids = {}
        
        for cat_title in categories:
            # Проверяем, есть ли уже такая категория
            existing = db.query(models.Category).filter(models.Category.title == cat_title).first()
            if existing:
                print(f"  ⚠️ Категория '{cat_title}' уже существует (ID: {existing.id})")
                category_ids[cat_title] = existing.id
            else:
                category = create_category(db, cat_title)
                category_ids[cat_title] = category.id
                print(f"  ✅ Добавлена категория: '{cat_title}' (ID: {category.id})")
        
        # ===== Добавляем книги =====
        print("\n📖 Добавление книг...")
        
        books_data = [
            # Книги по программированию
            {
                'title': 'Python: основы и применение',
                'description': 'Полное руководство по Python',
                'price': 1500.50,
                'category_title': 'Программирование'
            },
            {
                'title': 'SQL для аналитиков',
                'description': 'Практическое руководство по SQL',
                'price': 1200.00,
                'category_title': 'Программирование'
            },
            {
                'title': 'Алгоритмы и структуры данных',
                'description': 'Фундаментальные алгоритмы',
                'price': 1800.75,
                'category_title': 'Программирование'
            },
            {
                'title': 'Веб-разработка на Flask',
                'description': 'Создание веб-приложений',
                'price': 1350.00,
                'category_title': 'Программирование'
            },
            # Художественная литература
            {
                'title': 'Война и мир',
                'description': 'Роман Льва Толстого',
                'price': 900.00,
                'category_title': 'Художественная литература'
            },
            {
                'title': 'Преступление и наказание',
                'description': 'Роман Фёдора Достоевского',
                'price': 850.50,
                'category_title': 'Художественная литература'
            },
            {
                'title': 'Мастер и Маргарита',
                'description': 'Роман Михаила Булгакова',
                'price': 950.00,
                'category_title': 'Художественная литература'
            }
        ]
        
        for book_data in books_data:
            category_id = category_ids.get(book_data['category_title'])
            if category_id:
                book = create_book(
                    db,
                    title=book_data['title'],
                    description=book_data['description'],
                    price=book_data['price'],
                    category_id=category_id,
                    url=''
                )
                print(f"  ✅ Добавлена книга: '{book.title}' (цена: {book.price} руб.)")
        
        db.commit()
        
        print("\n" + "=" * 60)
        print("✅ ИНИЦИАЛИЗАЦИЯ БАЗЫ ДАННЫХ УСПЕШНО ЗАВЕРШЕНА!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    # Добавляем импорт models для создания таблиц
    from app.db import models
    init_database()