# Scrapy Parser PEP

## Описание
Асинхронный парсер, собирающий документы о PEP с сайта Python.
С каждой страницы PEP парсер собирает информацию и сохраняет в два файла:
* Список PEP (номер, название и статус);
* Все статусы и количество документов с этим статусом.

## Применяемые технологии

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-green)

### Порядок действий для запуска парсера

Клонировать репозиторий и перейти в папку c проектом:

```
git clone git@github.com:ItsFreez/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

*Для Windows*
```
python -m venv env
source venv/Scripts/Activate
```
*Для MacOS/Linux*
```
python3 -m venv env
source env/bin/activate
```

Обновить менеджер pip и установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запуск парсера
```
scrapy crawl pep
```

### Автор проекта

[ItsFreez](https://github.com/ItsFreez)
