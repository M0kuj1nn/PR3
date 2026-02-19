#класс в котором мы будем хранить данные
class Repository:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove_by_condition(self, attr, value):
        self.items = [
            i for i in self.items
            if not i.matches_condition(attr, value)
        ]

    def print_all(self):
        for item in self.items:
            print(item)
