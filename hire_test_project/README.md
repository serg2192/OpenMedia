# Инструкция по установке

## Требования

Для корректной работы приложения требуются:

- Python 3.6.3
- PostgreSQL 10.4
- Celery 4.2.0
- Redis 4.0.10

## Установка приложения

Установка Python, PostgreSQL, Celery, Redis происходит по соответствующим мануалам.

#### PostgreSQL
Создать юзера sondrin. Для этого можно например зайти в консоль psql под суперюзером и выполнить:
```
create user sondrin with superuser createdb replication password '123';
```

Можно не давать права superuser, replication, но я дал.

#### Установка приложения

Склонировать репозиторий:

```
git clone https://github.com/serg2192/OpenMedia.git
git checkout master
```

Создать виртуальное окружение:

```
cd OpenMedia
virtualenv ./venv
source ./venv/bin/activate
```

Установить все зависимости:
```
pip install -r hire_test_project/requirements/requirements.txt
```

## Запуск приложения
#### Запуск Redis

Требуется запустить либо как демон, либо из другого терминала.

Я запускаю из другого терминала.
Если установлен через sudo, выполняем из Linux терминала:

```
redis-server
```

Если установлен без sudo, выполняем из Linux терминала:

```
<path_to_redis>/src/redis-server
```

#### Запуск Celery

Требуется запустить либо как демон, либо из другого терминала.

Я запускаю из другого терминала.

```
cd OpenMedia/hire_test_project
celery -A hire_test_project worker -l info
```

P.S.:
Обязательно активировать виртуальное окружение перед запуском Celery.

```
source <path_to_virtual_env>/bin/activate
```

## Запуск приложения

```
python manage.py runserver
```

## API

На данный момент у приложения есть следующие url:
- parse/tags как POST метод требует чтобы в теле запроса был передан урл страницы для парсинга.

    Пример запроса:
    ```
    curl -X POST localhost:8000/parse/tags -H "Content-Type: application/json" -d '{"url":"http://yandex.ru"}'
    ```
- parse/tags как GET метод. Принимает номер задачи из Celery в качестве аргумента в строке запроса

    Пример запроса:
    ```
    curl -X GET localhost:8000/parse/tags?task_id=7b43794b-695f-4018-acbf-e2dac2a8e0a2 -H "Content-Type: application/json"
    ```