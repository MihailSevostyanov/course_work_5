class Vacancy:
    """Класс Vacancy, для работы с вакансиями (выгруженными из того или иного
    места)"""

    def __init__(self, vacancy_id, name, salary_from, salary_to, employer_id,
                 currency,
                 experience, schedule, employment, requirement, responsibility,
                 professional_roles, url):
        self.vacancy_id = vacancy_id
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer_id = employer_id
        self.currency = currency
        self.experience = experience
        self.schedule = schedule
        self.employment = employment
        self.requirement = requirement
        self.responsibility = responsibility
        self.professional_roles = professional_roles
        self.url = url

    @classmethod
    def get_list_with_objects(cls, list_with_vacancies):
        """Класс-метод для создания ЭК из словарей формата Response, получаемых
        с АПИ ХХ.ру"""
        returned_list = []
        for vacancy in list_with_vacancies:
            vacancy_id = vacancy['id']
            name = Vacancy.check_data_str(vacancy['name'])
            if not vacancy.get('salary'):
                salary_from = 0
                salary_to = 0
                currency = 0
            else:
                salary_from = Vacancy.check_data_int(
                    vacancy.get('salary').get('from'))
                salary_to = Vacancy.check_data_int(
                    vacancy.get('salary').get('to'))
                currency = Vacancy.convert_currency(Vacancy.check_data_str
                                                    (vacancy['salary'][
                                                         'currency']))
            employer_id = Vacancy.check_data_str(vacancy['employer']['id'])
            experience = Vacancy.check_data_str(vacancy['experience']['name'])
            schedule = Vacancy.check_data_str(vacancy['schedule']['name'])
            employment = Vacancy.check_data_str(vacancy['employment']['name'])
            requirement = Vacancy.check_data_str(
                vacancy['snippet']['requirement'])
            responsibility = Vacancy.check_data_str(
                vacancy['snippet']['responsibility'])
            professional_roles = ', '.join(
                [professional_role['name'] for professional_role in
                 vacancy['professional_roles']])
            url = vacancy['alternate_url']
            vacancy_object = cls(vacancy_id, name, salary_from, salary_to,
                                 employer_id,
                                 currency, experience, schedule, employment,
                                 requirement, responsibility,
                                 professional_roles, url)
            returned_list.append(vacancy_object)
        return returned_list

    @classmethod
    def get_objects_list_from_objects_dict(cls, list_with_vacancies):
        """Класс-метод для создания ЭК из словарей формата Vacancy.__dict__,
        получаемых при выгрузке вакансий из файла"""
        returned_list = []
        for vacancy in list_with_vacancies:
            name = vacancy['name']
            salary_from = vacancy['salary_from']
            salary_to = vacancy['salary_to']
            currency = vacancy['currency']
            employer = vacancy['employer']
            experience = vacancy['experience']
            schedule = vacancy['schedule']
            employment = vacancy['employment']
            requirement = vacancy['requirement']
            responsibility = vacancy['responsibility']
            professional_roles = vacancy['professional_roles']
            url = vacancy['url']
            vacancy_object = cls(name, salary_from, salary_to, employer,
                                 currency, experience, schedule, employment,
                                 requirement, responsibility,
                                 professional_roles, url)
            returned_list.append(vacancy_object)
        return returned_list

    @staticmethod
    def check_data_str(value):
        """Валидатор для стороковых значений"""
        if value:
            return value
        return 'информация не была найдена'

    @staticmethod
    def check_data_int(value):
        """Валидатор для целочисленных значений"""
        if value:
            return value
        return 0

    @staticmethod
    def convert_currency(currency):
        """Метод для конвертации валюты при выводе пользователю"""
        if currency:
            if currency == 'RUR':
                return 'руб.'
            elif currency == 'KZT':
                return 'тенге'
            elif currency == 'BYR':
                return 'белорус. руб.'
            elif currency == 'UZS':
                return 'узбек. сум'
            elif currency == 'EUR':
                return 'евро'
            elif currency == 'USD':
                return 'долларов'
        elif currency == 0:
            return 'валюта не была указана'
        else:
            return (f'неизвестный тип валюты '
                    f'с кодовым обозначением {currency}')

    def to_list(self):
        return [self.vacancy_id, self.name, self.salary_from, self.salary_to,
                self.employer_id, self.currency, self.experience, self.schedule,
                self.employment, self.requirement, self.responsibility,
                self.professional_roles, self.url]

    def get_salary(self):
        if not (self.salary_from or self.salary_to):
            return "Заработная плата: не указана"
        else:
            if not self.salary_from:
                return (f"Заработная плата: до "
                        f"{self.salary_to} {self.currency}")
            if not self.salary_to:
                return (f"Заработная плата: от {self.salary_from} "
                        f"{self.currency}")
            if self.salary_from == self.salary_to:
                return (f"Заработная плата: {self.salary_from} "
                        f"{self.currency}")
            return (f"Заработная плата: от {self.salary_from} до "
                    f"{self.salary_to} {self.currency}")

    def __eq__(self, other):  # – для равенства ==
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from == other.salary_from
        return self.salary_from == other

    def __ne__(self, other):  # – для неравенства !=
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from != other.salary_from
        return self.salary_from != other

    def __lt__(self, other):  # – для оператора меньше <
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from < other.salary_from
        return self.salary_from < other

    def __le__(self, other):  # – для оператора меньше или равно <=
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from <= other.salary_from
        return self.salary_from <= other

    def __gt__(self, other):  # – для оператора больше >
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from > other.salary_from
        return self.salary_from > other

    def __ge__(self, other):  # – для оператора больше или равно >=
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from >= other.salary_from
        return self.salary_from >= other

    def __str__(self):
        return (f'============================================================'
                f'\nВакансия: {self.name}\n'
                f'{self.get_salary()}\n'
                f'Наниматель: {self.employer_id}\n'
                f'Опыт работы: {self.experience}\n'
                f'График работы: {self.schedule}\n'
                f'Занятость: {self.employment}\n'
                f'Требования: {self.requirement.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                f'Обязанности: {self.responsibility.replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                f'Название должности: {self.professional_roles}\n'
                f'Ссылка на страницу вакансии: {self.url}\n'
                f'============================================================')
