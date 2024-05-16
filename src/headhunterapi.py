import requests
from src.parser import Parser


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = ''
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {}
        self.vacancies = []
        self.companies = []

    def load_vacancies(self, keyword: str = '', employer_id=''):
        """
        :param employer_id: возможно передавать идентификационный номер
        для поиска вакансий у конкретного работодателя
        :param keyword: слово для поиска по вакансиям на ХХ.ру
        :return: список вакансий пришедший с АПИ ХХ.р
        """
        self.url = 'https://api.hh.ru/vacancies'
        self.params['page'] = 0
        self.params['per_page'] = 100
        self.params['text'] = keyword
        if employer_id != '':
            self.params['employer_id'] = employer_id
        print('Происходит парсинг вакансий\n')
        while self.params.get('page') != 10:
            response = requests.get(self.url, headers=self.headers,
                                    params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

    def load_companies(self, company_ids: list):
        """
        :param company_ids: список айди вакансий для их поиска на ХХ.ру
        :return: список с информацией о компаниях пришедший с АПИ ХХ.р
        """
        for company_id in company_ids:
            self.url = 'https://api.hh.ru/employers/' + company_id
            response = requests.get(self.url, headers=self.headers,
                                    params=self.params)
            self.companies.append(response.json())
        return self.companies
