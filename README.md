# Что делает и зачем нужен

Принимает следующий JSON:

```{
    "Name": "some name", # text
    "Data": "some data", # text
    "timestamp": "time" # unixtime format
}
```

И отдаёт либо все записи по этой дате, либо по определенной дате (см. NB!)

# crypton-second-test-task

## Startup guide

```pip3 install -r requirements.txt``` 
(Лучше используйте venv)

```python manage.py migrate```

```python manage.py runserver 127.0.0.1:8000```

В браузере:

```http://127.0.0.1:8000/api/```

ИЛИ:

```Для списка запросов обратитесь к файлу requestexamples.txt```

Так же можно создать суперюзера и посмотреть данные через админку

```python manage.py createsuperuser```
```http://127.0.0.1:8000/admin/```

NB!
Механизм получения записей по дате изменён и согласован
для этого необходимо передать на энтрипоинт (/api/) GET запрос 
с JSON'ом формата {'timestamp': <UNIX TIME> (int)}, будут получены
все записи начиная с этого времени по времени на сервере

## TODO

Сделать адекватную JSON валидацию
