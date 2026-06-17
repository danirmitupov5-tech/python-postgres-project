import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Читаем параметры подключения из .env
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'octagon_db')
DB_USER = os.getenv('DB_USER', 'octagon')
DB_PASSWORD = os.getenv('DB_PASSWORD', '12345')

# Формируем строку подключения
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаем engine - основной объект для подключения
engine = create_engine(DATABASE_URL, echo=True)
# echo=True - выводит все SQL запросы в терминал для отладки

# Создаем фабрику сессий (сессия = подключение к БД)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()

# Функция для получения сессии (используется как зависимость)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функция для создания таблиц в БД
def create_tables():
    Base.metadata.create_all(bind=engine)