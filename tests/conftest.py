import pathlib
from io import StringIO

import pytest

from config import ROOT_DIR
from src.jsonworker import JSONWorker
from src.vacancy import Vacancy

TEST_FILE_PATH = pathlib.Path.joinpath(ROOT_DIR, 'data', 'test.json')


@pytest.fixture
def get_jsonworker_object():
    return JSONWorker(TEST_FILE_PATH)


@pytest.fixture
def list_dict_vacancies_1():
    return [{"name": "Senior Python разработчик",
             "salary_from": 30000000,
             "salary_to": None,
             "employer": "PIT STOP MOTORS",
             "currency": "узбек. сум",
             "experience": "От 1 года до 3 лет",
             "schedule": "Полный день",
             "employment": "Полная занятость",
             "requirement": "Опыт работы с "
                            "<highlighttext>Python</highlighttext> не менее "
                            "5 лет. Глубокие знания стандартной библиотеки "
                            "<highlighttext>Python</highlighttext> и разработки"
                            " вебприложений. Опыт работы с фреймворками...",
             "responsibility": "Разработка и поддержка веб-приложений на "
                               "<highlighttext>Python</highlighttext>. "
                               "Участие в проектировании архитектуры проектов. "
                               "Оптимизация производительности и "
                               "масштабируемости приложений. "
                               "Работа в тесном...",
             "professional_roles": "Руководитель группы разработки",
             "url": "https://hh.ru/vacancy/96378209"}]


@pytest.fixture
def list_dict_vacancies_2():
    return [{"name": "Junior DevOps engineer",
             "salary_from": 6000000,
             "salary_to": None,
             "employer": "PROXIMAOPS",
             "currency": "узбек. сум",
             "experience": "От 1 года до 3 лет",
             "schedule": "Полный день",
             "employment": "Полная занятость",
             "requirement": "Знание git, CI \\ CD, Jenkins (написание скриптов "
                            "сборок, дебаг, мониторинг). - Знание bash, "
                            "<highlighttext>python</highlighttext> "
                            "для написания скриптов и сценариев "
                            "развертывания. - ",
             "responsibility": "Зона ответственности: - Обслуживание, "
                               "мониторинг и поддержка инфраструктуры."
                               " - Совершенствование существующей "
                               "инфраструктуры в целях повышения ее "
                               "отказоустойчивости и масштабируемости. - "
                               "Своевременное реагирование и...",
             "professional_roles": "Другое",
             "url": "https://hh.ru/vacancy/94442670"
             }
            ]


@pytest.fixture
def list_object_vacancies(list_dict_vacancies_1):
    return Vacancy.get_objects_list_from_objects_dict(list_dict_vacancies_1)


@pytest.fixture
def big_list_object_vacancies(big_list_dict_vacancies):
    return Vacancy.get_objects_list_from_objects_dict(big_list_dict_vacancies)


@pytest.fixture
def big_list_dict_vacancies():
    return [{"name": "Senior Python разработчик",
             "salary_from": 30000000,
             "salary_to": None,
             "employer": "PIT STOP MOTORS",
             "currency": "узбек. сум",
             "experience": "От 1 года до 3 лет",
             "schedule": "Полный день",
             "employment": "Полная занятость",
             "requirement": "Опыт работы с <highlighttext>Python</highlighttext> не менее 5 лет. Глубокие знания стандартной библиотеки <highlighttext>Python</highlighttext> и разработки вебприложений. Опыт работы с фреймворками...",
             "responsibility": "Разработка и поддержка веб-приложений на <highlighttext>Python</highlighttext>. Участие в проектировании архитектуры проектов. Оптимизация производительности и масштабируемости приложений. Работа в тесном...",
             "professional_roles": "Руководитель группы разработки",
             "url": "https://hh.ru/vacancy/96378209"
             },
            {
                "name": "Java-разработчик",
                "salary_from": 15000000,
                "salary_to": 25000000,
                "employer": "PRO DATA",
                "currency": "узбек. сум",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы не менее 3-5 лет с Java 11, Spring Boot, Spring Data JPA, Hibernate, SOLID. Грамотная работа с...",
                "responsibility": "Разработка и оптимизация продукта «Панель облачной платформы», а также прочего, необходимого компании, функционала. Оперативная доработка и устранение неисправностей в коде. ",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95867928"
            },
            {
                "name": "Маркетолог-аналитик",
                "salary_from": 12000000,
                "salary_to": 20000000,
                "employer": "CHOCOCREAM.UZ",
                "currency": "узбек. сум",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "...аналитики продаж и маркетинга. Умение работать с базами данных ( Power BI), знание языков программирования для аналитики массивных данных ( SQL, <highlighttext>Python</highlighttext>).",
                "responsibility": "Подготовка аналитических отчетов на основе исследуемых данных. Анализ всей линейки продуктов компании и их продаж. Анализ конкурентной среды и определение...",
                "professional_roles": "Аналитик",
                "url": "https://hh.ru/vacancy/96053676"
            },
            {
                "name": "Старший Python разработчик",
                "salary_from": 10000000,
                "salary_to": 15000000,
                "employer": "Rochwin",
                "currency": "узбек. сум",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Коммерческий опыт работы разработки Django на МИКРО СЕРВИСАХ не менее 5 лет обязательно; (кандидаты без опыта не рассматриваются). ",
                "responsibility": "Разработка Back-end на <highlighttext>Python</highlighttext> (Django, FastApi) . Написание документации на Swagger. Поддержка существующего проекта (Microservice). Миграция базы данных с монолита...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95898832"
            },
            {
                "name": "Junior DevOps engineer",
                "salary_from": 6000000,
                "salary_to": None,
                "employer": "PROXIMAOPS",
                "currency": "узбек. сум",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знание git, CI \\ CD, Jenkins (написание скриптов сборок, дебаг, мониторинг). - Знание bash, <highlighttext>python</highlighttext> для написания скриптов и сценариев развертывания. - ",
                "responsibility": "Зона ответственности: - Обслуживание, мониторинг и поддержка инфраструктуры. - Совершенствование существующей инфраструктуры в целях повышения ее отказоустойчивости и масштабируемости. - Своевременное реагирование и...",
                "professional_roles": "Другое",
                "url": "https://hh.ru/vacancy/94442670"
            },
            {
                "name": "Инженер-программист",
                "salary_from": 5000000,
                "salary_to": None,
                "employer": "O'zelektroapparat-Electroshield (Узэлектроаппарат-Электрощит)",
                "currency": "узбек. сум",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "знание и умение применять на практике языки VBS, <highlighttext>Python</highlighttext>, С++ (Опционально языки С). - умение работать с АРI. - знание SQL. - ",
                "responsibility": "поддержка САПР EЗ.Series. - работа с базами данных САПР (заполнение, актуализация, адаптация схемных рсшений, ЗD моделей). - работа в EЗ.Series, AutoCad, Kompas. - ",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/96179141"
            },
            {
                "name": "IT project manager",
                "salary_from": 1200000,
                "salary_to": None,
                "employer": "New Energy Vehicles Kazakhstan",
                "currency": "тенге",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Разработка backend приложения будет выполняться с применением С#, Java, <highlighttext>Python</highlighttext>. Мы ожидаем что вы имеете подтвержденный опыт разработки минимум на...",
                "responsibility": "Возможность принять участие в построении технологического будущего Казахстана.",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95097491"
            },
            {
                "name": "QA Engineer",
                "salary_from": 1000000,
                "salary_to": None,
                "employer": "ForteBank",
                "currency": "тенге",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы с <highlighttext>python</highlighttext> и pytest. Понимание принципов HTTP/REST, опыт тестирования API. Приветствуется знание языков и протоколов: XML, JSON...",
                "responsibility": "Искать, документировать и сопровождать ошибки в баг-трекере. Вручную проверять разработанный функционал, где автоматизация нерациональна. Базы данных - Oracle. Testing - <highlighttext>Python</highlighttext>...",
                "professional_roles": "Тестировщик",
                "url": "https://hh.ru/vacancy/94481728"
            },
            {
                "name": "Machine Learning Engineer (специалист по машинному обучению)",
                "salary_from": 950000,
                "salary_to": 1200000,
                "employer": "Kolesa (АО Колеса)",
                "currency": "тенге",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знание основ Deep Learning в сфере CV и NLP (работа с разнородными данными: изображения, текст, табулярные данные). Владение <highlighttext>Python</highlighttext> (опыт...",
                "responsibility": "Разрабатывать ML модели для широкого круга задач. Участвовать в разработке сервиса на основе ML на всех этапах: от сбора данных...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/96182192"
            },
            {
                "name": "Senior C++",
                "salary_from": 700000,
                "salary_to": 1000000,
                "employer": "Sibdev",
                "currency": "руб.",
                "experience": "Более 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Опыт работы в качестве Senior. Уверенное знание C/C++ (5+ лет). Понимание принципов работы ядра Linux (memory management; network...",
                "responsibility": "Разработка и поддержка программного обеспечения на языке C/C++ под управлением ОС Linux. Отслеживание и устранение ошибок в коде. ",
                "professional_roles": "Руководитель группы разработки",
                "url": "https://hh.ru/vacancy/94491094"
            },
            {
                "name": "Маркетинговый аналитик",
                "salary_from": 600000,
                "salary_to": 950000,
                "employer": "Kolesa (АО Колеса)",
                "currency": "тенге",
                "experience": "Нет опыта",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Хороший SQL. Базовый <highlighttext>Python</highlighttext>. Опыт с Google-Аналитика /Firebase / Яндекс-Метрика / Яндекс-App метрика или с Базовый другими системами app...",
                "responsibility": "Помогать оптимизировать наш маркетинг. Заниматься оптимизацией и повышением эффективности компаний. Строить и улучшать воронки. Анализировать показатели сайтов и приложений для...",
                "professional_roles": "Аналитик",
                "url": "https://hh.ru/vacancy/94973394"
            },
            {
                "name": "Web QA Engineer",
                "salary_from": 550000,
                "salary_to": 1300000,
                "employer": "Kolesa (АО Колеса)",
                "currency": "тенге",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знание основных консольных команд Linux. Опыт программирования: PHP/JavaScript/Go/<highlighttext>Python</highlighttext>/Java. Опыт работы с NoSQL БД. Опыт работы в...",
                "responsibility": "Выполнять ручное и автоматизированное тестирование бизнес-логики, бэкэнда, фронтенда и интеграций. Разрабатывать и поддерживать в актуальном состоянии тест-планы, тест...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/96146369"
            },
            {
                "name": "Middle Backend разработчик",
                "salary_from": 500000,
                "salary_to": 600000,
                "employer": "Arcana Inc.",
                "currency": "тенге",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знание <highlighttext>Python</highlighttext> (минимум 2 год коммерческого опыта). - FastAPI, Django (1 год опыта). - Опыт создания REST API проектов. - Знание ООП, SOLID. - ",
                "responsibility": "Разрабатывать REST API на FastAPI, Django для различных проектов. - Писать тесты. - Делать code review другим разработчикам. - Участвовать в планировании проектов. - ",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95984435"
            },
            {
                "name": "Python Разработчик (Backend)",
                "salary_from": 500000,
                "salary_to": 700000,
                "employer": "Troubleshooting Technology",
                "currency": "тенге",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы от 2 лет на позиции <highlighttext>Python</highlighttext> разработчика. 2. Глубокое знание <highlighttext>Python</highlighttext> и его экосистемы. 3. Опыт работы с...",
                "responsibility": "1. Разработка и поддержка backend части веб и мобильных приложений. 2. Работа с микросервисной архитектурой. 3. Участие в проектировании и...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/94735611"
            },
            {
                "name": "Full Stack Developer",
                "salary_from": 500000,
                "salary_to": 600000,
                "employer": "ICEBERG-Service",
                "currency": "тенге",
                "experience": "Более 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знания технологий: JavaScript, React, Next.js, Css-modules, Webpack, Nest.js, Node.js,Postgres, SQL Redis, Mongo. Ответственно подходить к поставленным задачам. Пунктуальность.",
                "responsibility": "Разрабатывать модули и приложение для интернет магазина. Поддержка текущих модулей. Управлять SQL Базой (создавать и управлять таблицами). Прописывать парсера для...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95977651"
            },
            {
                "name": "Программист-робототехник",
                "salary_from": 450000,
                "salary_to": None,
                "employer": "Myrtle",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знание языков программирования C/C++, <highlighttext>Python</highlighttext>. Опыт написания программного обеспечения для STM32 (обязательны примеры успешно реализованных проектов). ",
                "responsibility": "Разработка алгоритмов программного обеспечения систем управления БПЛА (Беспилотных летательных аппаратов). Разработка и реализация логики работы систем управления БПЛА. ",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95119001"
            },
            {
                "name": "Python Developer",
                "salary_from": 450000,
                "salary_to": None,
                "employer": "Myrtle",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы с БД (PostgreSQL, MongoDB) и используемыми в <highlighttext>Python</highlighttext> ORM-фреймворками. Опыт работы в операционных системах семейства Linux и...",
                "responsibility": "Разработка backend-сервисов. Участие в проектировании архитектуры разрабатываемых решений. Организация обмена данными между сервисами. Оптимизация производительности приложений. Оптимизация и улучшение...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95119047"
            },
            {
                "name": "Computer vision engineer",
                "salary_from": 450000,
                "salary_to": None,
                "employer": "Myrtle",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт программирования на C++ и/или <highlighttext>Python</highlighttext> от 3-х лет. Опыт работы с OpenCV. Опыт работы с распознаванием изображений...",
                "responsibility": "Разработка ПО с применением нейронных сетей и компьютерного зрения для автономных БПЛА.",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95118931"
            },
            {
                "name": "Backend-разработчик (Senior)",
                "salary_from": 450000,
                "salary_to": None,
                "employer": "Вайтлист",
                "currency": "руб.",
                "experience": "Более 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Опыт коммерческой разработки на <highlighttext>Python</highlighttext> от 5 лет. Знание популярных <highlighttext>Python</highlighttext> web фрейворков: Django, FastAPI, Flask. Опыт проектирования микросервисной архитектуры. ",
                "responsibility": "Возможность влиять на развитие, видение продукта и на стратегию в целом.",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/96381610"
            },
            {
                "name": "Аналитик-Данных",
                "salary_from": 400000,
                "salary_to": 800000,
                "employer": "TapTatti Retail",
                "currency": "тенге",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы от 1 года в области анализа данных. Знание <highlighttext>Python</highlighttext> и SQL. Уверенная работа с Excel/Sheets. ",
                "responsibility": "Опыт работы с инструментами анализа данных, такими как <highlighttext>Python</highlighttext>. Продвинутые навыки пользователя Excel, Google Sheets. Разработка отчетностей в Power BI. ",
                "professional_roles": "BI-аналитик, аналитик данных",
                "url": "https://hh.ru/vacancy/94498271"
            },
            {
                "name": "Руководитель аналитического центра",
                "salary_from": 400000,
                "salary_to": None,
                "employer": "СИНЕРГИЯ",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы с аналитическими инструментами (<highlighttext>Python</highlighttext>, Excel, SQL, Tableau, PowerBI). Опыт работы с большими объёмами данных (BigData) и ETL-процессы. ",
                "responsibility": "Мы поддерживаем нестандартное мышление. Передовые идеи и инновации. Энергию предпринимательского духа. Мы вдохновляемся научными разработками и созданием уникальных продуктов в...",
                "professional_roles": "Руководитель отдела аналитики",
                "url": "https://hh.ru/vacancy/95363108"
            },
            {
                "name": "Senior Data Engineer",
                "salary_from": 400000,
                "salary_to": None,
                "employer": "Лаборатория Маркетинга",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знание статистики и математический бекграунд. Навыки владения инструментами: Hadoop, Spark, <highlighttext>Python</highlighttext>, SQL. Оценка и знание сложностей и оценок алгоритмов. ",
                "responsibility": "Формировать прогрессирующую систему анализа данных на продукте и масштабировать кросс-продуктовую аналитику. Улучшать систему качественного, количественного анализа данных. ",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95996741"
            },
            {
                "name": "Дата инженер",
                "salary_from": 400000,
                "salary_to": None,
                "employer": "L’etoile Digital",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Владение языками программирования (SQL на уровне не ниже Middle, <highlighttext>Python</highlighttext>, либо другом скриптовом языке программирования). Опыт работы с планировщиками задач...",
                "responsibility": "Участвовать в проектировании, создании, развертывании и управлении общей архитектуры платформы данных. Выстраивать процессы взаимодействия DWH и других компонент экосистемы данных...",
                "professional_roles": "Аналитик",
                "url": "https://hh.ru/vacancy/94340434"
            },
            {
                "name": "ML / gen AI разработчик (Python)",
                "salary_from": 400000,
                "salary_to": 450000,
                "employer": "NOCODIA",
                "currency": "тенге",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Частичная занятость",
                "requirement": "Опыт коммерческой разработки в области генеративного AI (OpenAI и/или другое) не менее 6 мес, на <highlighttext>Python</highlighttext> не менее года. ",
                "responsibility": "Разработка чат-ботов, модулей интеграции (API), разработка инструментов с использованием LLM, ML.",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/93064388"
            },
            {
                "name": "QA Lead / Руководитель команды тестирования",
                "salary_from": 370000,
                "salary_to": None,
                "employer": "Зорина Екатерина Владиславовна",
                "currency": "руб.",
                "experience": "Более 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Работы не менее чем с одним скриптовым языком (<highlighttext>Python</highlighttext>/ TCL/Bash/Perl) или другими языками программирования для написания тестов. ",
                "responsibility": "Лидирование создания и развития процесса тестирования в компании, охватывающего все направления автоматизации (web приложения, интеграционные взаимодействия, SQL, 1C и...",
                "professional_roles": "Тестировщик",
                "url": "https://hh.ru/vacancy/95923961"
            },
            {
                "name": "Lead Python developer",
                "salary_from": 370000,
                "salary_to": 740000,
                "employer": "Heaad",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Глубокое понимание структур данных, алгоритмов и объектно-ориентированного. Программирования на <highlighttext>Python</highlighttext>. Коммерческий опыт асинхронного программирования. Опыт работы в алгоритмическом фонде. ",
                "responsibility": "Проектирование, разработка и поддержка торговых систем, инструментов инфраструктуры. Плотное взаимодействие с трейдерами и инженерами DevOps. Работа над созданием асинхронного, сетевого...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95922593"
            },
            {
                "name": "QA Automation Engineer/Автотестировщик",
                "salary_from": 350000,
                "salary_to": None,
                "employer": "Финтех-Гид",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Знание SQL, Postgres (на уровне простых запросов). - Опыт написания тестов с использованием Playwright. - Опыт тестирования back-end приложений. - ",
                "responsibility": "Автоматизация E2E UI-тестов. - Развитие и сопровождение инструментов мониторинга и отчетности автотестирования. - Помощь DevOps инженерам в выстраивании процессов...",
                "professional_roles": "Тестировщик",
                "url": "https://hh.ru/vacancy/95451204"
            },
            {
                "name": "Technical Project Manager",
                "salary_from": 350000,
                "salary_to": 470000,
                "employer": "БизнесМатика",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Базовое знание хотя бы одного из языков программирования (например, <highlighttext>Python</highlighttext>, Golang или Java). Опыт работы с распределенными командами и разработчиками...",
                "responsibility": "Детализация и уточнений требований. Предпроектная оценка работ. Детализация и уточнения ожидаемого результата (образ результата, ожидаемое качество и т.д.). ",
                "professional_roles": "Руководитель проектов",
                "url": "https://hh.ru/vacancy/94908516"
            },
            {
                "name": "Devops engineer (Remote\\удаленно)",
                "salary_from": 350000,
                "salary_to": 450000,
                "employer": "Агентство 21 век, КЦ",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Ждем от кандидатов опыт с: - Сетевые навыки и безопасность. - Навыки программирования и скриптинга (<highlighttext>Python</highlighttext>, Bash). - Опыт работы с базами данных...",
                "responsibility": "Автоматизировать процесс поставки программного обеспечения. - Автоматизировать процессы разработки. - Поддерживать информационную безопасность компании. - Управлять инфраструктурой и доступами. - Взаимодействие с разработчиками для...",
                "professional_roles": "DevOps-инженер",
                "url": "https://hh.ru/vacancy/95728035"
            },
            {
                "name": "Ведущий бизнес-аналитик",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "Сантехника-Онлайн",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Желание развиваться в данном направлении. Умение принимать самостоятельные решения. Будет плюсом: Знание языка программирования (<highlighttext>Python</highlighttext>). Опыт работы с Web данными.",
                "responsibility": "Сбор, обработка и сегментирование больших объёмов данных, их анализ и представление выводов. Взаимодействие с другими отделами компании для выявления потребностей...",
                "professional_roles": "Бизнес-аналитик",
                "url": "https://hh.ru/vacancy/94823967"
            },
            {
                "name": "Сетевой инженер",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "КомпТек",
                "currency": "руб.",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Знание тенденций современных сетевых технологий, н-р: устройств на основе Open vSwitch, SDN, VXLAN, eVPN. PERL|<highlighttext>Python</highlighttext>/bash на уровне...",
                "responsibility": "Разработка, конфигурирование и описание работы сетевых тестовых схем коммутаторов и маршрутизаторов. Диагностика неисправностей/работы (Troubleshooting) сетевого оборудования и сетей. ",
                "professional_roles": "Сетевой инженер",
                "url": "https://hh.ru/vacancy/95615916"
            },
            {
                "name": "Head of BI",
                "salary_from": 300000,
                "salary_to": 500000,
                "employer": "IT-hunters",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "...данных, ориентированных на работу с Big Data. Приветствуется опыт разработки на SQL и <highlighttext>Python</highlighttext>, на уровне достаточного для ревью кода.",
                "responsibility": "Выстраивание работы подразделения, формирование стратегии развития направлений. Активное взаимодействие с руководителем компании, командой и внутренними бизнес-заказчиками. Управление всеми (организационными...",
                "professional_roles": "Руководитель проектов",
                "url": "https://hh.ru/vacancy/95997382"
            },
            {
                "name": "Руководитель отдела аналитики",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "Киприно, Производственный холдинг",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Желателен опыт работы с <highlighttext>Python</highlighttext> / R. - Знание основ категорийного менеджмента в продуктовом ритейле. - Сильные логические, аналитические навыки. - Опыт самостоятельной реализации...",
                "responsibility": "Руководство аналитическим отделом. - Анализ мониторинга сетевого/оптового канала (конкуренты, ценовая политика, промо стратегия). - Составление выводов по ценовой и ассортиментной политике...",
                "professional_roles": "Руководитель отдела аналитики",
                "url": "https://hh.ru/vacancy/95883669"
            },
            {
                "name": "Главный разработчик отчетности / BI-разработчик",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "Долсо",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы с Power BI и другими BI-платформами не менее 3 лет. Глубокие знания SQL. Навыки программирования для автоматизации...",
                "responsibility": "Построение визуальной отчетности (дашбордов) в MS Power BI. Проектирование, реализация и оптимизация моделей данных для обеспечения высокой производительности и доступности...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95437006"
            },
            {
                "name": "Senior Python developer/Python разработчик (Django, FastAPI) в TravelTech",
                "salary_from": 300000,
                "salary_to": 400000,
                "employer": "Лао Оливарес Кристина Вячеславовна",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Совокупный стаж коммерческой разработки на <highlighttext>Python</highlighttext> от 4-5 лет. -Знания Django, FastAPI. -Проектирование сервисов и API. -Владение pytest. -",
                "responsibility": "Market &AdTech - развитие инструментов для привлечения в сервис аудитории со всего мира. Условия: Оформление по договору ИП. -Проектирование и разработка...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95975517"
            },
            {
                "name": "Backend Python (Remote)",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "Simpol Lab",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "5+ лет опыта backend разработки. Отличное знание и понимание FastApi. Опыт работы с высоконагруженными распределенными системами. Знание инструментов и...",
                "responsibility": "Разработка новых функциональных возможностей. - Доработка существующего функционала продукта. - Разработка и подключение API как внутренних, так и внешних сервисов. - ",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/94456033"
            },
            {
                "name": "QA Lead",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "Кадровое агентство BWG",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Актуальный опыт работы в QA. Опыт управления командой от 2-х лет. Опыт программирования на любом языке – не обязательно коммерческий...",
                "responsibility": "Автоматизация сценариев тестирования. Разработка стратегии тестирования, составление тест-планов и чек-листов. Ведение тестовой документации. Взаимодействие с командой разработки и...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/94825519"
            },
            {
                "name": "РУКОВОДИТЕЛЬ ОТДЕЛА РАЗРАБОТКИ ВЕБ-СЕРВИСОВ",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "ФГБУ ГИВЦ Минкультуры России",
                "currency": "руб.",
                "experience": "Более 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы не менее 5 лет разработчиком в сфере разработки бизнес-приложений. Отличное знание процесса разработки, умение его организовывать и...",
                "responsibility": "Участие в планировании проектов и определении требований к программному обеспечению. Управление проектированием, разработкой, тестированием и поддержкой программного обеспечения. ",
                "professional_roles": "Руководитель группы разработки",
                "url": "https://hh.ru/vacancy/95912321"
            },
            {
                "name": "Инженер по автоматизации тестирования беспилотных технологий (QA/SDET)",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "SberAutoTech",
                "currency": "руб.",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Понимание принципов работы Docker. Базовые навыки разработки на <highlighttext>Python</highlighttext>, использования Pytest. Опыт взаимодействия с Allure report. Опыт работы с системами...",
                "responsibility": "Автоматизация тестирования беспилотных технологий и систем. Описание тестовой модели, заведение дефектов и репортов по результатам тестирования. Участие в развитии процесса...",
                "professional_roles": "Тестировщик",
                "url": "https://hh.ru/vacancy/89541561"
            },
            {
                "name": "Системный администратор серверов и локальной сети",
                "salary_from": 300000,
                "salary_to": 1500000,
                "employer": "ТК Прогресс",
                "currency": "тенге",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Проводить анализ сервера, что работает, что - не работает. 2. Базовые знания <highlighttext>Python</highlighttext>, Bash. 3. Базовые знания SQL, умение делать простые...",
                "responsibility": "Администратор серверов и локальных сетей.",
                "professional_roles": "Системный администратор",
                "url": "https://hh.ru/vacancy/95358102"
            },
            {
                "name": "Senior Product Analyst",
                "salary_from": 300000,
                "salary_to": 350000,
                "employer": "Пикабу",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Опыт работы в качестве продуктового аналитика от 3 лет.  Понимание и опыт работы с метриками продукта с рекламной монетизацией.  ",
                "responsibility": "Тесное взаимодействие с командами продукта, выявление значимых идей и потребностей, помощь в их реализации. - <highlighttext>Python</highlighttext> (библиотеки для анализа данных, мат. ",
                "professional_roles": "Аналитик",
                "url": "https://hh.ru/vacancy/95727374"
            },
            {
                "name": "Специалист по автоматизированному тестированию\\Automation QA Engineer (Python)",
                "salary_from": 300000,
                "salary_to": 320000,
                "employer": "АйТиКвик",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "...написания UI тестов <highlighttext>python</highlighttext> + selenium web driver. Опыт написания автотестов на Appium <highlighttext>Python</highlighttext>. Знание bash, <highlighttext>python</highlighttext>. Опыт тестирования REST...",
                "responsibility": "Написание и поддержка автотестов web и мобильных приложений с использованием <highlighttext>python</highlighttext>, selenium web driver и appium. Регистрация результатов тестирования в...",
                "professional_roles": "Тестировщик",
                "url": "https://hh.ru/vacancy/91786034"
            },
            {
                "name": "Ведущий бизнес-аналитик",
                "salary_from": 300000,
                "salary_to": None,
                "employer": "Сантехника-Онлайн",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Желание развиваться в данном направлении. Умение принимать самостоятельные решения. Будет плюсом: Знание языка программирования (<highlighttext>Python</highlighttext>). Опыт работы с Web данными.",
                "responsibility": "Сбор, обработка и сегментирование больших объёмов данных, их анализ и представление выводов. Взаимодействие с другими отделами компании для выявления потребностей...",
                "professional_roles": "Бизнес-аналитик",
                "url": "https://hh.ru/vacancy/94823966"
            },
            {
                "name": "Эксперт департамента геоинформационных систем",
                "salary_from": 300000,
                "salary_to": 500000,
                "employer": "Информационно-аналитический центр нефти газа, АО",
                "currency": "тенге",
                "experience": "От 3 до 6 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "...или MS SQL Server). Знание программирования (<highlighttext>Python</highlighttext>). Наличие практического опыта автоматизации геоинформационных задач (<highlighttext>Python</highlighttext>, библиотеки: arcpy, numpy, pandas, requests, json...",
                "responsibility": "Сопровождение процессов сбора, оценки, верификации, анализа получаемой геопространственной информации. Подготовка геопространственных данных (обработка, загрузка, миграция, пересчет координат, создание, приведение к...",
                "professional_roles": "Другое",
                "url": "https://hh.ru/vacancy/94569097"
            },
            {
                "name": "Senior Python Developer",
                "salary_from": 300000,
                "salary_to": 400000,
                "employer": "АСД Технолоджиз",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Опыт работы с PyQT. От кандидата мы ожидаем опыта коммерческой разработки на <highlighttext>Python</highlighttext> от 5 лет и владения технологиями выше.",
                "responsibility": "Разработка системы управления виртуализацией и системы VDI.",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/96127759"
            },
            {
                "name": "Python разработчик",
                "salary_from": 280000,
                "salary_to": 500000,
                "employer": "БизнесМатика",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Знание языка <highlighttext>Python</highlighttext>: Продвинутое знание <highlighttext>Python</highlighttext> 3.x. Опыт работы с anci для создания масштабируемых и высокопроизводительных приложений. ",
                "responsibility": "Анализ и реверс-инжиниринг текущего решения. Проектирование, разработка и внедрение эффективного и надежного кода. Поддерживать и оптимизировать существующие системы для...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95307857"
            },
            {
                "name": "Инженер-аналитик (Отдел Главного Механика)",
                "salary_from": 275000,
                "salary_to": None,
                "employer": "Быстринская горная компания",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Вахтовый метод",
                "employment": "Полная занятость",
                "requirement": "Умение работать с аналитическими инструментами (например, Excel, SQL, <highlighttext>Python</highlighttext>). Знание ПК, основных программ Microsoft Office, таких как MS Access, Word...",
                "responsibility": "Работа в Службе Главного Механика на строительстве золотоизвлекающей фабрики. - Сбор, анализ и интерпретация данных для выявления трендов и паттернов. - ",
                "professional_roles": "Аналитик",
                "url": "https://hh.ru/vacancy/96173612"
            },
            {
                "name": "Специалист по ГИС картографии (Иран)",
                "salary_from": 260000,
                "salary_to": 280000,
                "employer": "Росгеология",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Вахтовый метод",
                "employment": "Полная занятость",
                "requirement": "...от 28 октября 2021 г.  802/20). Является преимуществом знание: СУБД Рostgresql, MS sql, Oracle, <highlighttext>Python</highlighttext>, Corel Draw, GIMP, AutoCad.",
                "responsibility": "Работа в программе ArcGIS: создание тематических карт в ArcGIS, ведение баз пространственных геоданных, работа с пространственными данными из разных источников...",
                "professional_roles": "Геолог",
                "url": "https://hh.ru/vacancy/92756552"
            },
            {
                "name": "Junior Blockchain Developer",
                "salary_from": 250000,
                "salary_to": None,
                "employer": "SHiFT AM",
                "currency": "руб.",
                "experience": "От 1 года до 3 лет",
                "schedule": "Полный день",
                "employment": "Полная занятость",
                "requirement": "Cтэк: <highlighttext>python</highlighttext> / typescript / solidity / redis / PostgreSQL / mogo db / hardhat / fatsapi / asyncio / hardhat. Понимание технологических рисков DeFi, желателен опыт аудита и...",
                "responsibility": "Развивать dApp shift.tech как в ончейн части, так и на стороне backend. Участвовать в разработке наших финансовых продуктов: смарт-контракты...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95695925"
            },
            {
                "name": "Middle Python Developer",
                "salary_from": 250000,
                "salary_to": 350000,
                "employer": "Apeek",
                "currency": "руб.",
                "experience": "От 3 до 6 лет",
                "schedule": "Удаленная работа",
                "employment": "Полная занятость",
                "requirement": "Опыт от 5 лет в разработке. Хорошее знание <highlighttext>Python</highlighttext>, Django, Flask, Asyncio, Celery, Selenium. Умении проектировать структуру SQL и NoSQL...",
                "responsibility": "Писать качественный код опираясь на бизнес-аналитику и макеты в Figma. Проектировать и разрабатывать RestAPI. Выполнять интеграцию с внешними сервисами...",
                "professional_roles": "Программист, разработчик",
                "url": "https://hh.ru/vacancy/95652406"
            }
            ]


@pytest.fixture
def for_work_with_api(monkeypatch):
    user_input = StringIO("2\n1\nPython\n2\nBackend SQL\n3\n150000\n4\n5\n5\n"
                          "6\n7\ntest_api_complete.json\nstop")
    monkeypatch.setattr('sys.stdin', user_input)


@pytest.fixture
def for_work_with_file(monkeypatch):
    user_input = StringIO("2\n1\ntesting\n1\ntesting.json\n2\nBackend SQL\n3\n"
                          "500000\n4\n5\n5\n6\n7\nн\n8\ntest_complete.json\n"
                          "stop")
    monkeypatch.setattr('sys.stdin', user_input)
