from src.vacancy import Vacancy


def test_classmethods(list_dict_vacancies_1):
    assert Vacancy.get_objects_list_from_objects_dict(list_dict_vacancies_1)[0].name == list_dict_vacancies_1[0]['name']
