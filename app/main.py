import sys
import os

# Добавляем корневую папку в путь
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal
from app.db.crud import get_all_categories, get_all_books


def main():
    """Вывод данных из БД"""
    
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("ДАННЫЕ ИЗ БАЗЫ ДАННЫХ octagon_db")
        print("=" * 70)
        
        # Получаем и выводим категории
        categories = get_all_categories(db)
        print(f"\n📚 КАТЕГОРИИ ({len(categories)} шт.):")
        print("-" * 70)
        for cat in categories:
            print(f"  • ID: {cat.id:2d} | Название: {cat.title}")
        
        # Получаем и выводим книги
        books = get_all_books(db)
        print(f"\n📖 КНИГИ ({len(books)} шт.):")
        print("-" * 70)
        
        for book in books:
            category_name = book.category.title if book.category else "Без категории"
            print(f"  • ID: {book.id:2d}")
            print(f"    Название: {book.title}")
            print(f"    Описание: {book.description[:50] + '...' if book.description and len(book.description) > 50 else book.description}")
            print(f"    Цена: {book.price:8.2f} руб.")
            print(f"    Категория: {category_name}")
            print()
        
        print("=" * 70)
        print(f"✅ Всего: {len(categories)} категорий, {len(books)} книг")
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()