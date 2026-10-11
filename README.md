# Mini PIM API

Мини-API для управления товарными данными (pet-проект, вдохновлён NotPIM).

## Что умеет

- CRUD для товаров через REST API.
- Импорт товаров из JSON-фида с валидацией.
- Админка Django для ручного управления.
- Кастомная валидация: цена > 0, SKU в верхнем регистре.

## Стек

- Python 3.12
- Django 6.1.2
- Django REST Framework 3.18.3
- SQLite (для простоты)

## Установка и запуск

```bash
# Клонировать
git clone https://github.com/x3au4ukx/notpim_pet.git
cd notpim_pet

# Виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Зависимости
pip install -r requirements.txt

# Миграции
python manage.py migrate

# Суперпользователь (для админки)
python manage.py createsuperuser

# Запуск
python manage.py runserver