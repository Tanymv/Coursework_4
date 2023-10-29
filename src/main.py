from abc import ABC, abstractmethod
import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
import os            # Для работы с файлами
# import pandas as pd
class Api_sites:
    """абстрактный класс для работы с API сайтов с вакансиями."""
    @abstractmethod
    def get_vacancies(self):
        pass

class Hh_site(Api_sites):
    """Класс подключается к API и получает вакансии с hh.ru."""
    @abstractmethod
    def get_vacancies(self):
        params = {
            'text': 'python',
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        return data



a = Hh_site()
asa = a.get_vacancies()


class Superjob_site(Api_sites):
    """Класс подключается к API и получает вакансии с  superjob.ru"""
    @abstractmethod
    def get_vacancies(self):
        pass


class Job_processing():
    """Класс поддерживает методы сравнения вакансий между собой по зарплате и валидирует данные, которыми инициализируются его атрибуты."""
    def __init__(self, name, url, salary, information):
        self.name = name
        self.url = url
        self.salary = salary
        self.information = information

    def __str__(self):
        return str(self.salary)

    def __lt__(self, other):
        return self.salary < other.salary


f = open('hh.json', encoding='utf8')
jsonText = f.read()
f.close()
    # Текст файла переводим в справочник
jsonObj = json.loads(jsonText)
areas = {"name": "",
        "salary": "",
        "url": "",
        "req": ""}
cities = jsonObj['items']


for k in cities:
    try:
        areas["name"] = k['name']
        areas["salary"] = str(k["salary"]["from"])
        areas["url"] = k["alternate_url"]
        areas["req"] = k["snippet"]["requirement"]
    except TypeError:
        areas["name"] = k['name']
        areas["salary"] = "Данных нет"
        areas["url"] = k["alternate_url"]
        areas["req"] = k["snippet"]["requirement"]
    else:
        areas["name"] = k['name']
        areas["salary"] = str(k["salary"]["from"])
        areas["url"] = k["alternate_url"]
        areas["req"] = k["snippet"]["requirement"]
for i in areas:
    print(i)

#
# a = Job_processing("Junior Python Developer (удаленно)", "https://hh.ru/vacancy/88776307", 40000, "Будет плюсом: Опыт работы с библиотеками для работы с ботами (tg).")
# b = Job_processing("Junior Python Developer (удаленно)", "https://hh.ru/vacancy/88776307", 50000, "Будет плюсом: Опыт работы с библиотеками для работы с ботами (tg).")
# my = [a,b]
# result = sorted(areas, reverse=True, key=lambda x: x[1])
# for i in result:
#     print(i)


class Work_files:
    """абстрактный класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях."""
    @abstractmethod
    def add_file(self):
        pass

class Work_files_hh(Work_files):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях с hh.ru."""
    @abstractmethod
    def add_file(self):
        for page in range(0, 20):

            # Преобразуем текст ответа запроса в справочник Python
            jsObj1 = json.loads(asa)

            # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
            # Определяем количество файлов в папке для сохранения документа с ответом запроса
            # Полученное значение используем для формирования имени документа
            nextFileName1 = 'hh.json'

            # Создаем новый документ, записываем в него ответ запроса, после закрываем
            f = open(nextFileName1, mode='w', encoding='utf8')
            f.write(json.dumps(jsObj1, ensure_ascii=False, indent=2))
            f.close()

            # Проверка на последнюю страницу, если вакансий меньше 2000
            if (jsObj1['pages'] - page) <= 1:
                break

            # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
            time.sleep(0.25)

        print('Старницы поиска собраны')
x = Work_files_hh()
x.add_file()

class Work_files_superjob(Work_files):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях с  superjob.ru"""
    @abstractmethod
    def add_file(self):
        pass