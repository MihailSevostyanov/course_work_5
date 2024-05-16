import os
from config import ROOT_DIR
from src.company import Company
from src.dbmanager import DBManager
from src.headhunterapi import HeadHunterAPI
from src.jsonworker import JSONWorker
from src.vacancy import Vacancy


def get_filtered_vacancies(vacancies_list, words_for_filter):
    """
    :param vacancies_list: принимаемый лист для фильтрации по словам
    :param words_for_filter: список слов, принимаемый для фильтрации списка
    :return: отфильтрованный список
    """
    filtered_list = []
    for vacancy in vacancies_list:
        for word in words_for_filter:
            if word in vacancy.responsibility or word in vacancy.requirement:
                filtered_list.append(vacancy)
                break
    return filtered_list


def get_vacancies_by_salary(vacancies, min_salary):
    """
    :param vacancies: список вакансий из которого вернутся лишь те зарплаты, чьё
    значение выше поступившего аргумента min_salary
    :param min_salary: значение зарплаты служащее фильтром для списка вакансий
    :return: список вакансий с зарплатами выше указанной
    """
    only_salary_vacancies = []
    for vacancy in vacancies:
        if vacancy >= min_salary:
            only_salary_vacancies.append(vacancy)
    return only_salary_vacancies


def get_sorted_vacancies(vacancies):
    """Возвращает списко вакансий, отсортированный по минимальной заработной
    плате"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies, stop):
    """Возвращает срез от списка vacancies"""
    return vacancies[:stop]


def print_vacancies(vacancies):
    """Печатает каждую вакансию из поданного списка"""
    for vacancy in vacancies:
        print(vacancy)


def add_data_to_db():
    user_input = input('Желаете наполнить базу данных информацией о вакансиях'
                       ' и компаниях? yes/no')
    if user_input == 'yes':
        company_ids = input("Введите id компаний среди вакансий которой будет "
                            "осуществляться поиск(через пробел) "
                            "или можете оставить поле пустым для использования "
                            "фиксированного списка компаний")
        if company_ids.strip() == '':
            company_ids = ['3127', '3776', '1122462', '2180', '87021',
                           '1740', '80', '4181', '15478', '78638']
        else:
            company_ids = company_ids.split(' ')
        hh_api = HeadHunterAPI()
        hh_vacancies = []
        for company_id in company_ids:
            hh_vacancies = hh_api.load_vacancies(employer_id=company_id)
        hh_companies = hh_api.load_companies(company_ids)
        vacancies_list = Vacancy.get_list_with_objects(hh_vacancies)
        companies_list = Company.get_list_with_objects(hh_companies)
        dbmanager = DBManager()
        dbmanager.load_to_db(vacancies_list, companies_list)
        print('Таблицы были заполнены')


def load_vacancies():
    while True:
        user_input = input('В этом блоке вы можете выгружать вакансии для\n'
                           'последующего выполнения манипуляций\n'
                           'с полученной информацией\n'
                           'Кнопки управления:\n'
                           '1 - выгрузить вакансии из файла\n'
                           '2 - выгрузить вакансии из базы данных\n'
                           '3 - выгрузить вакансии с HeadHunterAPI\n').strip()
        if user_input not in ['1', '2', '3']:
            print('Попробуйте ввести команду снова')
            continue
        elif user_input == '1':
            file_name_1 = input("Введите название файла(без расширения - на "
                                "данный момент программа работает автоматически"
                                " с файлами формата json")
            file_path_1 = os.path.join(ROOT_DIR, 'data',
                                       file_name_1 + '.json')
            if os.path.exists(file_path_1):
                jsonworker = JSONWorker(file_path_1)
                json_vacancies = jsonworker.load_vacancies()
                vacancies_list = Vacancy.get_objects_list_from_objects_dict(
                    json_vacancies)
                print(f'Выгрузка завершена, список с вакансиями создан\n'
                      f'Вакансий в списке: {len(vacancies_list)}\n')
                break
            else:
                print(f'Выгрузка не была произведена, не найден файл '
                      f'по следующему пути - {file_path_1}')
        elif user_input == '2':
            work_with_db()

        elif user_input == '3':
            search_query = input("Введите ваш поисковый запрос")
            hh_api = HeadHunterAPI()
            hh_vacancies = hh_api.load_vacancies(keyword=search_query)
            vacancies_list = Vacancy.get_list_with_objects(hh_vacancies)
            print(f'Запрос выполнен, список с вакансиями создан\n'
                  f'Вакансий в списке: {len(vacancies_list)}\n')
        try:
            return vacancies_list
        except NameError:
            print('Что-то пошло не так - список вакансий не был создан')


def user_interaction(vacancies):
    """Функция осуществляющая связь с пользователем и являющаяся неким подобием
         панели управления программой, вызывается в случае если пользователь решил
         работать с вакансиями, выгружаемыми из файла"""
    user_input = 0
    vacancies_list = vacancies[:]
    while user_input != 'назад':
        if user_input in ['стоп', 'stop']:
            break
        print('В этом блоке вы можете выполнять манипуляции с ранее'
              ' полученной информацией\n'
              'Кнопки управления:\n'
              '1 - отфильтровать вакансии по ключевым словам\n'
              '2 - оставить вакансии с З/П, выше N\n'
              '3 - сортировать вакансии по убыванию минимальной З/П\n'
              '4 - оставить N вакансий от начала списка\n'
              '5 - распечатать информацию о всех вакансиях в текущем списке\n')
        while user_input != 'назад':
            user_input = input(
                "Что желаете сделать? Для возврата введите 'назад'\n")
            if user_input in ['стоп', 'stop']:
                break
            if user_input == '1':
                filter_words = input(
                    "Введите ключевые слова для фильтрации "
                    "вакансий через пробел: ").split(" ")
                vacancies_list = get_filtered_vacancies(vacancies_list,
                                                        filter_words)
                print(f'Вакансии отфильтрованы по ключевым словам,\n'
                      f'вакансий в списке: {len(vacancies_list)}')
            elif user_input == '2':
                min_salary = int(
                    input('Введите нижний порог заработной платы: '))
                vacancies_list = get_vacancies_by_salary(vacancies_list,
                                                         min_salary)
                print(f'В списке остались только вакансии с зарплатой\n'
                      f'выше указанной, вакансий в списке: {len(vacancies_list)}')
            elif user_input == '3':
                vacancies_list = get_sorted_vacancies(vacancies_list)
                print(f'Вакансии отсортированы, '
                      f'вакансий в списке: {len(vacancies_list)}')
            elif user_input == '4':
                top_n = int(input(
                    f'Введите количество вакансий для вывода в топ N: '))
                vacancies_list = get_top_vacancies(vacancies_list,
                                                   top_n)
                print(
                    f'Срез выполнен, вакансий в списке: {len(vacancies_list)}')
            elif user_input == '5':
                print_vacancies(vacancies_list)
    return vacancies_list


def save_data(vacancies):
    user_input = 0
    while user_input != 'назад':
        print('В этом блоке вы можете выполнять манипуляции с ранее'
              ' полученной информацией\n'
              'Кнопки управления:\n'
              '1 - сохранить вакансии в файл с расширением json\n'
              '2 - сохранить вакансии в файл с расширением csv\n'
              '3 - сохранить вакансии в файл с расишрением txt\n'
              '4 - сохранить вакансии в БД(новую или старую)\n')
        user_input = input()
        if user_input in ['стоп', 'stop']:
            break
        if user_input == '1':
            file_name_2 = input('Введите название файла для сохранения данных,'
                                ' без указания расширения')
            file_path_2 = os.path.join(ROOT_DIR, 'data', file_name_2 + '.json')
            jsonworker = JSONWorker(file_path_2)
            if os.path.exists(file_path_2):
                confirm = input('Такой файл уже есть, '
                                'желаете вести работу в нем? д/н').lower().strip()
                if confirm == 'д':
                    confirm = input(
                        'Желаете перезаписать или дописать файл? п/д')
                    if confirm == 'д':
                        jsonworker.add_vacancies(vacancies)
                        print('Вакансии добавлены в файл')
                    elif confirm == 'п':
                        jsonworker.write_vacancies(vacancies)
                        print('Вакансии сохранены в файл с перезаписью')
            else:
                jsonworker.write_vacancies(vacancies)
                print(f'Вакансии сохранены в файл по адресу {file_path_2}')
        elif user_input == '2':
            print('В данный момент указанный функционал находится в разработке')
            continue
        elif user_input == '3':
            print('В данный момент указанный функционал находится в разработке')
            continue
        elif user_input == '4':
            print('В данный момент указанный функционал находится в разработке')
            continue
        else:
            print('Попробуйте ввести вновь')


def work_with_db():
    db = DBManager()
    while True:
        user_input = input("Желаете продолжить работу с БД? Если нет введите "
                           "'стоп'")
        if user_input == 'стоп':
            break
        user_input_db = input('В этом блоке вы можете выгружать вакансии '
                              'из базы данных для\n'
                              'последующего выполнения манипуляций '
                              'с полученной информацией\n'
                              'Кнопки управления:\n'
                              '1 - получить список всех компаний и количество '
                              'вакансий у каждой компании.\n'
                              '2 - получить список всех вакансий с указанием '
                              'названия компании, названия вакансии,'
                              ' зарплаты и ссылки на вакансию.\n'
                              '3 - получить среднюю зарплату по вакансиям.\n'
                              '4 - получить список всех вакансий, у которых '
                              'зарплата выше средней по всем вакансиям.\n'
                              '5 - получить список всех вакансий, '
                              'в названии которых содержатся искомое слово.\n')
        if user_input_db not in ['1', '2', '3', '4', '5']:
            print('Попробуйте ввести команду снова\n')
            continue
        elif user_input_db == '1':
            for_unpack = db.get_companies_and_vacancies_count()
            for company in for_unpack:
                print(f'Название компании-работодателя: {company[0]}\n'
                      f'Количество вакансий у данного работодателя'
                      f'(обнаруженных в БД): {company[1]}')
        elif user_input_db == '2':
            for_unpack = db.get_all_vacancies()
            for vacancy in for_unpack:
                print(f'Название вакансии: {vacancy[1]}\n'
                      f'Название компании-работодателя: {vacancy[0]}\n'
                      f'Заработная плата от {vacancy[2]} до {vacancy[3]}'
                      f', указана в {vacancy[4]}'
                      f'(если что-то в этой строке отсутствует или '
                      f'равно нулю, значит эта информация не была '
                      f'указана в описании вакансии)\n'
                      f'Ссылка на вакансию: {vacancy[5]}')
        elif user_input_db == '3':
            average_salary = db.get_avg_salary()
            print(f'Средняя заработная плата по '
                  f'всей БД: {average_salary}')
        elif user_input_db == '4':
            for_unpack = db.get_vacancies_with_higher_salary()
            for vacancy in for_unpack:
                print(f'Название вакансии: {vacancy[1]}\n'
                      f'Название компании-работодателя: {vacancy[0]}\n'
                      f'Заработная плата от {vacancy[2]} до {vacancy[3]}'
                      f', указана в {vacancy[4]}'
                      f'(если что-то в этой строке отсутствует или '
                      f'равно нулю, значит эта информация не была '
                      f'указана в описании вакансии)\n'
                      f'Ссылка на вакансию: {vacancy[5]}')
        elif user_input_db == '5':
            user_keyword = input('Введите искомое слово:')
            for_unpack = db.get_vacancies_with_keyword(user_keyword)
            for vacancy in for_unpack:
                print(f'Название вакансии: {vacancy[1]}\n'
                      f'Название компании-работодателя: {vacancy[0]}\n'
                      f'Заработная плата от {vacancy[2]} до {vacancy[3]}'
                      f', указана в {vacancy[4]}'
                      f'(если что-то в этой строке отсутствует или '
                      f'равно нулю, значит эта информация не была '
                      f'указана в описании вакансии)\n'
                      f'Ссылка на вакансию: {vacancy[5]}')
        else:
            print('Попробуйте ввести вновь')
    print('К сожалению в данный момент программа не поддерживает совершение'
          ' дальнейших манипуляций с информацией получаемой из БД')
    return []
