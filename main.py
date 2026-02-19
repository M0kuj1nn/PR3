"""Точка входа в программу. Запускает обработку файла с командами."""
from parser import CommandProcessor

def main():
    cp = CommandProcessor()
    cp.execute_file("artifact.txt")

if __name__ == "__main__":
    main()
