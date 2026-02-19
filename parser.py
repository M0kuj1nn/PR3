"""Модуль для парсинга команд из файла и их выполнения."""
from classes import Aphorism, Proverb
from repository import Repository


class CommandProcessor:
    """Класс для обработки команд из файла (ADD, REM, PRINT)."""
    def __init__(self):
        #создаем компазицию, когда CP будет внутри содержать Repo
        self.repo = Repository()


    def process_line(self, line: str):
        #чистим от пробелов
        line = line.strip()
        if not line:
            return

        #Проверяем начало строки на команду при помощи startswith
        #берем строку от 5 символа, чистим от пробелов и вызываем нужный метод.

        # ADD команда

        if line.startswith("ADD"):
            return self.process_add(line[4:].strip())

        # REM content~"text"

        if line.startswith("REM"):
            return self.process_rem(line[4:].strip())

        # PRINT - просто вызываем сразу метод вывода из репозитория

        if line == "PRINT":
            return self.repo.print_all()

    def parse_args(self, arg_string: str):
        #Разбираем на кортеж параметры вида key="value";key2="value2"
        result = {}
        parts = arg_string.split(";")
        for part in parts:
            if "=" in part:
                key, val = part.split("=", 1)
                #убираем пробелы и кавычки
                result[key.strip()] = val.strip().strip("\"")
        return result

    #смотрим на тип команды, создаем на ее основе объект класса.
    def process_add(self, data: str):
        #разбиваем строку APHORISM;content="Жизнь — это движение";author="Аристотель" на два, тип фразы отпраляем в type_name
        #аргументы цельной строкой отправляем в args
        type_name, args = data.split(";", 1)

        #делаем из аргементов кортеж
        args = self.parse_args(args)

        if type_name == "APHORISM":
            obj = Aphorism(content=args["content"], author=args["author"])
        elif type_name == "PROVERB":
            obj = Proverb(content=args["content"], country=args["country"])
        else:
            print("Недопустимое значение в файле:", type_name)
            return

        self.repo.add(obj)

    #делим строку на аттрибут и значение, очищаем от пробелов и кавычек значение, вызываем remove_by_condition
    def process_rem(self, data: str):
        # пример: content~"abc"
        attr, value = data.split("~")
        value = value.strip().strip("\"")
        self.repo.remove_by_condition(attr, value)

    def execute_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                self.process_line(line)
