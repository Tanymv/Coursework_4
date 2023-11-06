from abc import abstractmethod
import requests  # Для запросов по API
import json  # Для обработки полученных результатов
import time  # Для задержки между запросами


class Api_sites:
    """абстрактный класс для работы с API сайтов с вакансиями."""

    @abstractmethod
    def get_vacancies(self):
        pass


class Hh_site(Api_sites):
    """Класс подключается к API и получает вакансии с hh.ru."""

    @property
    def get_vacancies(self):
        params = {
            'text': 'python',
        }
        req = requests.get('https://api.hh.ru/vacancies', params=params)
        data = req.content.decode()
        req.close()
        url = 'https://api.hh.ru/vacancies'
        try:
            r = requests.get(url, timeout=1)
            r.raise_for_status()
        except requests.exceptions.RequestException as errex:
            print("Exception request")
        return data


hh_site = Hh_site()
hh = hh_site.get_vacancies


class Superjob_site(Api_sites):
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
        req.close()
        url = 'https://api.hh.ru/vacancies'
        try:
            r = requests.get(url, timeout=1)
            r.raise_for_status()
        except requests.exceptions.RequestException as errex:
            print("Exception request")
        return data


superjob_site = Superjob_site()
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


class Work_files:
    """абстрактный класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления
    информации о вакансиях."""

    @abstractmethod
    def add_file(self):
        pass


class Work_files_hh(Work_files):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям с hh.ru."""

    def add_file(self):
        for page in range(0, 20):

            js_obj1 = json.loads(hh)

            next_file_name1 = 'hh.json'

            f = open(next_file_name1, mode='w', encoding='utf8')
            f.write(json.dumps(js_obj1, ensure_ascii=False, indent=2))
            f.close()

            if (js_obj1['pages'] - page) <= 1:
                break

            time.sleep(0.25)

        f = open('hh.json', encoding='utf8')
        jsonText = f.read()
        f.close()

        json_obj = json.loads(jsonText)
        areas = []
        obj = json_obj['items']

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


class Work_files_superjob(Work_files):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям с  superjob.ru"""

    def add_file(self):
        for page in range(0, 20):

            js_obj2 = json.loads(super_)

            next_file_name2 = 'super.json'

            f = open(next_file_name2, mode='w', encoding='utf8')
            f.write(json.dumps(js_obj2, ensure_ascii=False, indent=2))
            f.close()

            if (js_obj2['pages'] - page) <= 1:
                break

            time.sleep(0.25)
        f = open('super.json', encoding='utf8')
        jsonText = f.read()
        f.close()

        json_obj = json.loads(jsonText)
        areas = []
        obj = json_obj['items']

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


class Clearing_files:
    """
    Класс очищает json файлы.
    """

    def __init__(self, filename):
        self.filename = filename

    def clear(self):
        with open(self.filename, "w") as file:
            file.truncate()


clearing_files1 = Clearing_files("hh.json")
clearing_files2 = Clearing_files("super.json")
clearing_files1.clear()
clearing_files2.clear()


def user_interaction():
    input("Введите слово для запроса: ")
    conclusion = int(input("Введите 1 - HeadHunter, 2 - SuperJob, 3 - Вместе: "))
    if conclusion == 1:
        work_files_hh = Work_files_hh()
        work_files_hh.add_file()
    elif conclusion == 2:
        work_files_superjob = Work_files_superjob()
        work_files_superjob.add_file()
    elif conclusion == 3:
        work_files_hh = Work_files_hh()
        work_files_hh.add_file()
        work_files_superjob = Work_files_superjob()
        work_files_superjob.add_file()
    else:
        print("Вы ввели не то")


if __name__ == "__main__":
    user_interaction()
