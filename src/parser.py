from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс Parser является родительским классом, от которого так же могут
    наследовваться другие парсеры"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
