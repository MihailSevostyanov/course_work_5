class Company:

    def __init__(self, employer_id, accredited, name,
                 description, url, vacancies_url, area, industries):
        self.employer_id = employer_id
        self.accredited = accredited
        self.name = name
        self.description = description
        self.url = url
        self.vacancies_url = vacancies_url
        self.area = area
        self.industries = industries


    @classmethod
    def get_list_with_objects(cls, companies):
        returned_list = []
        for company in companies:
            employer_id = company['id']
            accredited = company['accredited_it_employer']
            name = company['name']
            description = company['description']
            url = company['alternate_url']
            vacancies_url = company['vacancies_url']
            area = company['area']['name']
            industries = ' // '.join(
                [industry['name'] for industry in company['industries']])
            company_obj = cls(employer_id, accredited, name,
                              description, url, vacancies_url, area, industries)
            returned_list.append(company_obj)
        return returned_list


    def to_list(self):
        return [self.employer_id, self.accredited, self.name, self.description,
                self.url, self.vacancies_url, self.area, self.industries]


    def __str__(self):
        return (
            f'==============================================================='
            f'\nКомпания - {self.name}'
            f'\nРазвивается в следующих направлениях - {self.industries}'
            f'\nСсылка на просмотр информации о данной компании'
            f'(в том числе списка вакансий) - {self.url}')