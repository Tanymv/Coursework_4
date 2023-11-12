from abc import ABC, abstractmethod
import requests  # Для запросов по API
import json  # Для обработки полученных результатов
import time  # Для задержки между запросами


class FileSaver:
    @staticmethod
    def save_to_file(data, filename, mode):
        with open(filename, mode=mode, encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))


class ApiSites(ABC):
    """абстрактный класс для работы с API сайтов с вакансиями."""

    @abstractmethod
    def get_vacancies(self):
        pass


class HhSite(ApiSites):
    """Класс подключается к API и получает вакансии с hh.ru."""

    @property
    def get_vacancies(self):
        params = {
            'text': 'python',
        }
        req = requests.get('https://api.hh.ru/vacancies', params=params)
        data = req.content.decode()
        url = 'https://api.hh.ru/vacancies'
        try:
            r = requests.get(url, timeout=1)
            r.raise_for_status()
        except requests.exceptions.RequestException as errex:
            print("Exception request")
        return data


hh_site = HhSite()
hh = hh_site.get_vacancies


class SuperjobSite(ApiSites):
    """Класс подключается к API и получает вакансии с  superjob.ru"""

    def get_vacancies(self):
        params = {
            'text': 'python',
        }
        header = {
            'X-Api-App-Id': "v3.h.4548695.86e5263b88c14dcdf21278c56e244fe76c271480"
                            ".11211fc0eb5b45066dbaf0fe6cefa4a84f6e847a"
        }
        req = requests.get('https://api.hh.ru/vacancies', params=params, headers=header)
        data = req.content.decode()
        url = 'https://api.hh.ru/vacancies'
        try:
            r = requests.get(url, timeout=1)
            r.raise_for_status()
        except requests.exceptions.RequestException as errex:
            print("Exception request")
        return data


superjob_site = SuperjobSite()
super_ = superjob_site.get_vacancies()


class Vacancy:
    """Класс поддерживает методы сравнения вакансий между собой по зарплате и валидирует данные,
    которыми инициализируются его атрибуты."""

    def __init__(self, name, salary, url, information):
        self.name = name
        self.url = url
        self.salary = salary
        self.information = information

    def __str__(self):
        return str(self.salary)

    def __lt__(self, other):
        return self.salary < other.salary


class WorkFiles(ABC):
    """абстрактный класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления
    информации о вакансиях."""

    @abstractmethod
    def add_file(self):
        pass


class WorkFilesHh(WorkFiles):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям с hh.ru."""

    def add_file(self):
        file_saver = FileSaver()

        for page in range(0, 20):
            js_obj1 = json.loads(hh)
            next_file_name1 = 'hh.json'
            file_saver.save_to_file(js_obj1, next_file_name1, mode='a')
            areas = []
            obj = js_obj1['items']

            for k in obj:
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

            result = sorted(areas, reverse=True, key=lambda item: item[1])
            print("Вакансии с Hh.ru")

            for i in result:
                print(i)
            break
    def top(self):
        file_saver = FileSaver()

        for page in range(0, 20):
            js_obj1 = json.loads(hh)
            next_file_name1 = 'hh.json'
            file_saver.save_to_file(js_obj1, next_file_name1, mode='a')
            areas = []
            obj = js_obj1['items']

            for k in obj:
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

            result = sorted(areas, reverse=True, key=lambda item: item[1])
            result = result[-5:]
            print("Вакансии с Hh.ru")

            for i in result:
                print(i)
            break


class WorkFilesSuperjob(WorkFiles):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям с  superjob.ru"""

    def add_file(self):
        file_saver1 = FileSaver()

        for page in range(0, 20):
            js_obj2 = json.loads(hh)
            next_file_name2 = 'hh.json'
            file_saver1.save_to_file(js_obj2, next_file_name2, mode='a')

            areas = []
            obj = js_obj2['items']

            for k in obj:
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

            result = sorted(areas, reverse=True, key=lambda item: item[1])
            print("")
            print("Вакансии с Superjob.ru")

            for i in result:
                print(i)
            break
    def top(self):
        file_saver = FileSaver()

        for page in range(0, 20):
            js_obj2 = json.loads(hh)
            next_file_name2 = 'hh.json'
            file_saver.save_to_file(js_obj2, next_file_name2, mode='a')

            areas = []
            obj = js_obj2['items']

            for k in obj:
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

            result = sorted(areas, reverse=True, key=lambda item: item[1])
            print("")
            print("Вакансии с Superjob.ru")
            result = result[-5:]

            for i in result:
                print(i)
            break


class ClearingFiles:
    """
    Класс очищает json файлы.
    """

    def __init__(self, filename):
        self.filename = filename

    def clear(self):
        with open(self.filename, "w") as file:
            file.truncate()


clearing_files1 = ClearingFiles("hh.json")
clearing_files2 = ClearingFiles("super.json")
clearing_files1.clear()
clearing_files2.clear()


def user_interaction():
    input("Введите слово для запроса: ")
    conclusion = int(input("Введите 1 - HeadHunter, 2 - SuperJob, 3 - Вместе: "))
    if conclusion == 1:
        work_files_hh = WorkFilesHh()
        work_files_hh.add_file()
        user_input = int(input("Хотите вывести топ 5? 1 - да, 2 - нет. "))
        if user_input == 1:
            work_files_hh.top()
        elif user_input == 2:
            print("До встречи")
    elif conclusion == 2:
        work_files_superjob = WorkFilesSuperjob()
        work_files_superjob.add_file()
        user_input = int(input("Хотите вывести топ 5? 1 - да, 2 - нет. "))
        if user_input == 1:
            work_files_superjob.top()
        elif user_input == 2:
            print("До встречи")
    elif conclusion == 3:
        work_files_hh = WorkFilesHh()
        work_files_hh.add_file()
        work_files_superjob = WorkFilesSuperjob()
        work_files_superjob.add_file()
        user_input = int(input("Хотите вывести топ 5? 1 - да, 2 - нет. "))
        if user_input == 1:
            work_files_hh.top()
            work_files_superjob.top()
        elif user_input == 2:
            print("До встречи")
    else:
        print("Вы ввели не то")


if __name__ == "__main__":
    user_interaction()
