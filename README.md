# Scrapy Парсер PEP

## Описание
**Scrapy Парсер PEP** - асинхронный парсер, собирающий документы о PEP с сайта Python.

С каждой страницы PEP парсер собирает информацию и сохраняет в два файла:
* Список PEP (номер, название и статус);
* Все статусы и количество документов с этим статусом.

## Стек технологий

![](https://img.shields.io/badge/Python-3.9-black?style=flat&logo=python) 
![](https://img.shields.io/badge/Scrapy-2.5.1-black?style=flat&logo=scrapy) 

## Порядок действий для запуска парсера

***1. Клонировать репозиторий и перейти в папку c проектом***

```shell
git clone git@github.com:ItsFreez/Scrapy_Parser_PEP.git
```

```shell
cd Scrapy_Parser_PEP
```

***2. Cоздать и активировать виртуальное окружение***

*Для Windows*
```shell
python -m venv env
source venv/Scripts/Activate
```
*Для MacOS/Linux*
```shell
python3 -m venv env
source env/bin/activate
```

***3. Обновить менеджер pip и установить зависимости из файла requirements.txt***

```shell
python -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

***4. Запустить парсер***

```shell
scrapy crawl pep
```

### Автор проекта

[ItsFreez](https://github.com/ItsFreez)
