from src.utils import user_interaction, load_vacancies, save_data, \
    add_data_to_db


def main():
    print("Доброго времени суток, вы запустили программу "
          "для упрощенного общения с вакансиями")
    user_input = ''
    while user_input != 'exit':
        add_data_to_db()
        vacancies = load_vacancies()
        filtered_vacancies = user_interaction(vacancies)
        save_data(filtered_vacancies)


if __name__ == "__main__":
    main()
