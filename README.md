Задание:
Разработка API для книжной библиотеки

Применены технологии:
FastApi, SqlAlchemy, Docker, Graphen

Подготовка:

> docker-compose up --build

Работа с приложением:

1. FastApi + SqlAlchemy
   http://127.0.0.1:8080/docs

2. FAstApi + SqlAlchemy + Graphen
   http://127.0.0.1:8080/grapgql

Тест:
Не смог разобраться почему не импортируется
модуль graphen при выполнениии команды в командной строке pytest,
хотя тесты работали какое-то время.

Ошибка:
import graphene
ModuleNotFoundError: No module named 'graphene'
