from abc import ABC, abstractmethod
class Api_sites:
    """абстрактный класс для работы с API сайтов с вакансиями."""
    @abstractmethod
    def get_vacancies(self):
        pass

class Hh_site(Api_sites):
    """Класс подключается к API и получает вакансии с hh.ru."""
    @abstractmethod
    def get_vacancies(self):
        pass

class Superjob_site(Api_sites):
    """Класс подключается к API и получает вакансии с  superjob.ru"""
    @abstractmethod
    def get_vacancies(self):
        pass


class Job_processing():
    """Класс поддерживает методы сравнения вакансий между собой по зарплате и валидирует данные, которыми инициализируются его атрибуты."""
    pass


class Work_files:
    """абстрактный класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях."""
    @abstractmethod
    def add_file(self):
        pass

class Work_files_hh(Api_sites):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях с hh.ru."""
    @abstractmethod
    def add_file(self):
        pass

class Work_files_superjob(Api_sites):
    """класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях с  superjob.ru"""
    @abstractmethod
    def add_file(self):
        pass