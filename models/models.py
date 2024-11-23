from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional
from datetime import datetime


class UserModel(BaseModel):
    id: int  # Целочисленный идентификатор
    name: str  # Строковое имя
    email: EmailStr  # Проверка правильности email
    is_active: bool  # Логическое значение
    signup_date: datetime  # Дата и время регистрации
    tags: List[str]  # Список строк
    age: Optional[int]  # Необязательный целочисленный возраст
    website: Optional[HttpUrl]  # Необязательный URL
    metadata: dict  # Словарь с произвольными данными
    score: float  # Число с плавающей точкой


# Создаем экземпляр модели
example_obj_pydantic = UserModel(
    id=1,
    name="John Doe",
    email="johndoe@example.com",
    is_active=True,
    signup_date=datetime.now(),
    tags=["python", "developer"],
    age=30,
    website="https://example.com",
    metadata={"role": "admin", "department": "IT"},
    score=4.7,
)
