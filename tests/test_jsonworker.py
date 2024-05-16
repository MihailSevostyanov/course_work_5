import pathlib
from config import ROOT_DIR

TEST_FILE_PATH1 = pathlib.Path.joinpath(ROOT_DIR, 'data', 'test.json')


def test_load_vacancies(get_jsonworker_object, list_dict_vacancies_1):
    assert get_jsonworker_object.load_vacancies() == list_dict_vacancies_1


def test_write_vacancy(get_jsonworker_object, list_object_vacancies,
                       list_dict_vacancies_1):
    get_jsonworker_object.write_vacancies(list_object_vacancies)
    assert get_jsonworker_object.load_vacancies() == list_dict_vacancies_1


def test_del_vacancy_full(get_jsonworker_object, list_dict_vacancies_1,
                          list_dict_vacancies_2):
    get_jsonworker_object.del_vacancy_full(list_dict_vacancies_1[0])
    assert get_jsonworker_object.load_vacancies() == []


def test_add_vacancy(get_jsonworker_object, list_object_vacancies,
                     list_dict_vacancies_1):
    get_jsonworker_object.add_vacancies(list_object_vacancies)
    get_jsonworker_object.add_vacancies(list_object_vacancies)
    assert get_jsonworker_object.load_vacancies() == [list_dict_vacancies_1[0],
                                                      list_dict_vacancies_1[0]]


def test_del_vacancy_one(get_jsonworker_object, list_dict_vacancies_1):
    get_jsonworker_object.del_vacancies_one(list_dict_vacancies_1[0])
    # строка возвращающая файл в исходное состояние
    assert get_jsonworker_object.load_vacancies() == list_dict_vacancies_1


