from abc import ABC, abstractmethod
import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами


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



hh_site = Hh_site()
hh = hh_site.get_vacancies()


class Superjob_site(Api_sites):
    """Класс подключается к API и получает вакансии с  superjob.ru"""
    @abstractmethod
    def get_vacancies(self):
        pass


class Job_processing:
    """Класс поддерживает методы сравнения вакансий между собой по зарплате и валидирует данные, которыми инициализируются его атрибуты."""
    def __init__(self, name,  salary, url, information):
        self.name = name
        self.url = url
        self.salary = salary
        self.information = information

    def __str__(self):
        return str(self.salary)

    def __lt__(self, other):
        return self.salary < other.salary


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

            jsObj1 = json.loads(hh)

            nextFileName1 = 'hh.json'

            f = open(nextFileName1, mode='w', encoding='utf8')
            f.write(json.dumps(jsObj1, ensure_ascii=False, indent=2))
            f.close()

            # Проверка на последнюю страницу, если вакансий меньше 2000
            if (jsObj1['pages'] - page) <= 1:
                break

            # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
            time.sleep(0.25)
        f = open('hh.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        # Текст файла переводим в справочник
        jsonObj = json.loads(jsonText)
        areas = []
        cities = jsonObj['items']

        for k in cities:
            try:
                areas.append([k['name'],
                              str(k["salary"]["from"]),
                              k["alternate_url"],
                              k["snippet"]["requirement"]])
            except TypeError:
                areas.append([k['name'],
                              "Данных нет",
                              k["alternate_url"],
                              k["snippet"]["requirement"]])
            else:
                areas.append([k['name'],
                              str(k["salary"]["from"]),
                              k["alternate_url"],
                              k["snippet"]["requirement"]])

        result = sorted(areas, reverse=True, key=lambda x: x[1])
        for i in result:
            print(i)

x = Work_files_hh()
x.add_file()


class Work_files_superjob(Work_files):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях с  superjob.ru"""
    @abstractmethod
    def add_file(self):
        pass








