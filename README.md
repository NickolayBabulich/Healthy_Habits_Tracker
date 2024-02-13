# Atomic Habits - Трекер привычек (курсовой проект по Django REST framework/DRF)

### О проекте:

Трекер привычек - данный проект реализует бэкэнд-часть SPA веб-приложения. На основе описанных API эндпоинтов пользователь регистрируется, авторизуется под своим профилем и создает привычки, напоминание о которых отправляется в телеграм бота.
<br>

В данном сервисе реализован следующий функционал:

- Регистрация и авторизация пользователя
- Создание, изменение, удаление привычки
- Просмотр своих привычек
- Просмотр привычек со статусом публичные
- Рассылка привычек в телеграм за 10 минут до необходимости осуществить действие

## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/-OOP-FF5733?style=flat)](https://en.wikipedia.org/wiki/Object-oriented_programming) [![DRF](https://img.shields.io/badge/-DRF-FF5733?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![API](https://img.shields.io/badge/-API-4CAF50?style=flat)](https://en.wikipedia.org/wiki/Application_programming_interface)
[![Celery](https://img.shields.io/badge/-Celery-37814A?style=flat&logo=celery&logoColor=white)](http://www.celeryproject.org/)
[![PyTest](https://img.shields.io/badge/-PyTest-0A9EDC?style=flat&logo=python&logoColor=white)](https://docs.pytest.org/)
[![Swagger](https://img.shields.io/badge/-Swagger-85EA2D?style=flat&logo=swagger&logoColor=white)](https://swagger.io/)
[![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
 [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

### Настройка сервиса:
Для запуска приложения в Docker необходимо выполнить следующие команды:
- docker-compose build
- docker-compose up

- Установлены Python версии не ниже 3.11, база данных PostgreSQL, Redis
- В телеграме создан бот для рассылок
- В директории проекта создано виртуальное окружение:
    - ```python -m venv venv```
- Установлены зависимости:
    - ```pip install -r requirements.txt```
- Создана пустая БД в PostgreSQL
- Заполнен файл .env.sample вашими настройками и после переименован в .env
- Созданы и применены миграции:
    - ```python manage.py makemigrations```
    - ```python manage.py migrate```
- Запущен сервер redis
- Запущен Celery:
    - ```celery -A config worker -l INFO```
    - ```celery -A config beat -l INFO```
- Запущен локальный сервер:
    - ```python manage.py runserver```

### Дополнительные настройки:

- Суперпользователь создается командой:
    - ```python manage.py csu``` и имеет следующие настройки:
        - логин: admin@app.com
        - пароль: 1
- Возможно предустановить пользователей для тестов командой:
    - ```python manage.py create_users``` создается 3 пользователя с данными:
        - логин: user0@app.com, user1@app.com, user2@app.com
        - пароль: 1

### Начало работы:

- Для работы рекомендуется использовать Postman или аналогичные программы для тестирования API
- Необходимые данные и сами эндпоинты реализованные в программе можно посмотреть по ссылке http://127.0.0.1:8000/swagger/
- Для начала работы пользователю необходимо создать пользователя и авторизоваться
- После авторизации возможно создавать привычки
- Напоминание в телеграм отправляется за 10 минут до срабатывания привычки

### Логика работы системы:

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше 2 минут. Исходя из этого получаем первую модель — Привычка.

- Исключен одновременный выбор связанной привычки и указания вознаграждения
- Время выполнения должно быть не больше 120 секунд
- В связанные привычки могут попадать только привычки с признаком приятной привычки
- У приятной привычки не может быть вознаграждения или связанной привычки
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней
