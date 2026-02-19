"""Модуль для хранения и управления коллекцией артефактов."""
class Repository:
    """Класс-контейнер для хранения и управления артефактами."""
    def __init__(self):
        """Инициализирует пустой репозиторий."""
        self.items = []

    def add(self, item):
        """Добавляет артефакт в репозиторий."""
        self.items.append(item)

    def remove_by_condition(self, attr, value):
        """Удаляет артефакты, которые соответствуют условию attr~value."""
        self.items = [
            i for i in self.items
            if not i.matches_condition(attr, value)
        ]

    def print_all(self):
        """Выводит все артефакты из репозитория."""
        for item in self.items:
            print(item)
