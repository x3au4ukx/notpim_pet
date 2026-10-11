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
```
##  Эндпоинты

| Метод | URL                        | Описание             |
|-------|----------------------------|----------------------|
| GET   | /api/products/             | Список товаров       |
|POST | /api/products/             | Создать товар        |
|GET	| /api/products/{id}/        | 	Детали товара       |
|PUT | /api/products/{id}/        | Полное обновление    |
|PATCH | /api/products/{id}/        | Частичное обновление |
|DELETE | /api/products/{id}/        | Удалить товар        |
|POST | /api/products/import_feed/ | Импорт из JSON-фида  |

## Пример: создание товара

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"sku": "SKU001", "name": "Товар", "price": "199.99"}'
```
Ответ:
```json
{
    "id": 1,
    "sku": "SKU001",
    "name": "Товар",
    "description": "",
    "price": "199.99",
    "category": "",
    "created_at": "2026-10-11T18:07:30.396700Z",
    "updated_at": "2026-10-11T18:07:30.396700Z"
}
```
## Пример: импорт фида

```bash
curl -X POST http://127.0.0.1:8000/api/products/import_feed/ \
  -H "Content-Type: application/json" \
  -d '[
    {"sku": "SKU001", "name": "Товар 1", "price": "100.00"},
    {"sku": "SKU002", "name": "Товар 2", "price": "200.00"}
  ]'
```
Ответ:
```json
{
    "total": 2,
    "created": 2,
    "failed": 0,
    "created_items": [
        {
            "id": 1,
            "sku": "SKU001",
            "name": "Товар 1",
            "description": "",
            "price": "100.00",
            "category": "",
            "created_at": "2026-10-11T18:05:55.802654Z",
            "updated_at": "2026-10-11T18:05:55.802654Z"
        },
        {
            "id": 2,
            "sku": "SKU002",
            "name": "Товар 2",
            "description": "",
            "price": "200.00",
            "category": "",
            "created_at": "2026-10-11T18:05:55.814617Z",
            "updated_at": "2026-10-11T18:05:55.814617Z"
        }
    ],
    "errors": []
}
```

## Автор

[Андрей Зайцев](https://github.com/x3au4ukx)