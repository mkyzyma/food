## 1. Создайте виртуальное окружение

Например:

`pyenv virtualenv 3.10.7 food`

`pyenv activate food`

## 2. Установка зависимостей

`pip install poetry`

`poetry install`

## 3. Запуск тестов

`pytest`

## 4. Запуск сервера

### На тестовой базе SQLite:

`uvicorn api.app:app --reload`

### На postgres через docker-compose:

`docker-compose up`

или в фоновом режиме

`docker-compose up -d`

## 4. Swagger

http://localhost:8000/docs

**Примечания**

> Не реализован нормальный сидинг начальных данных. Чтобы не пришлось их добавлять через swagger можно делать так: сначала запустить `pytest`, а потом `uvicorn api.app:app --reload`. При этом будет использоваться тестовая база, с некоторым набором данных.

> Не реализована обработка ошибок, кроме того что предоставляет pydantic
