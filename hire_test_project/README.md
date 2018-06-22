# Инструкция по установке

## Требования

Для корректной работы приложения требуются:

- Python 3.6.3
- PostgreSQL 10.4
- Celery 4.2.0
- Redis 4.0.10

## Установка приложения

#### PostgreSQL
Создать юзера sondrin. Для этого можно например зайти в консоль psql под суперюзером и выполнить:
```
create user sondrin with superuser createdb replication password '123';
```

#### Установка приложения

Склонировать репозиторий:

```
git clone https://github.com/serg2192/OpenMedia.git
git checkout master
```

Создать виртуальное окружение:

```
cd open_media
virtualenv ./venv
```

Установить все зависимости:
```
pip install -r hire_test_project/requirements/requirements/txt
```


## Запуск приложения

```
python manage.py runserver
```

