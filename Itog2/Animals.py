import re
from datetime import datetime


class Animals:
    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

    def get_name(self):
        return self.__name

    def set_name(self, new):
        self.__name = new

    name = property(get_name, set_name)

    def get_birthday(self):
        return self.__birthday

    def set_birthday(self, new):
        self.__birthday = new

    birthday = property(get_birthday, set_birthday)

    def __str__(self):
        return f'{self.name}  {self.birthday}'


class Pets(Animals):
    category = 'Pets'

    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.__commands = []

    def add_commands(self, *com):
        for cmd in com:
            self.__commands.append(cmd)

    def get_commands(self):
        return ', '.join(self.__commands)

    def set_commands(self, new):
        self.__commands = new

    commands = property(get_commands, set_commands)

    def __str__(self):
        return f'{self.category} {self.name}  {self.birthday}: {self.commands}'


class PackAnimals(Animals):
    category = 'PackAnimals'

    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.__commands = []

    def add_commands(self, *chars):
        for char in chars:
            self.__commands.append(char)

    def get_commands(self):
        return ', '.join(self.__commands)

    def set_commands(self, new):
        self.__commands = new

    commands = property(get_commands, set_commands)

    def __str__(self):
        return f'{self.category} {self.name}  {self.birthday}: {self.commands}'


class Dog(Pets):
    types = 'Dog'


class Cat(Pets):
    types = 'Cat'


class Hamster(Pets):
    types = 'Hamster'


class Horse(PackAnimals):
    types = 'Horse'


class Donkey(PackAnimals):
    types = 'Donkey'


class Camel(PackAnimals):
    types = 'Camel'



reestr = []


def add_animal():
    animal = input('''
    dog - d
    cat - c
    hamster - h
    horse - hr
    donkey - dk
    camel - cm
    > ''').lower()
    name, date = input("Введите имя и дату рождения через пробел (дд.мм.гггг): ").split()


    try:
        datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        print("Неверный формат даты. Пожалуйста, используйте дд.мм.гггг")
        return

    match animal:
        case 'd':
            reestr.append(Dog(name, date))
        case 'c':
            reestr.append(Cat(name, date))
        case 'h':
            reestr.append(Hamster(name, date))
        case 'hr':
            reestr.append(Horse(name, date))
        case 'dk':
            reestr.append(Donkey(name, date))
        case 'cm':
            reestr.append(Camel(name, date))
        case _:
            print("Неверный выбор животного. Попробуйте снова.")
            return

    print('Животное успешно добавлено')


def select_command():
    num = int(input("Введите номер животного: "))
    if 0 <= num < len(reestr):
        print('Команды:', reestr[num].commands)
    else:
        print("Неверный номер животного.")



def list_b():
    while True:
        try:
            d1, d2 = input("Введите первую и вторую дату через пробел (дд.мм.гггг): ").split()
            dt1 = datetime.strptime(d1, '%d.%m.%Y')
            dt2 = datetime.strptime(d2, '%d.%m.%Y')
            if dt1 > dt2:
                raise ValueError("Первая дата не должна быть позже второй даты.")
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите даты в корректном формате.")

    l = []

    for entry in reestr:
        try:
            dt = datetime.strptime(entry.birthday, '%d.%m.%Y')
            if dt1 <= dt <= dt2:
                l.append(entry)
        except ValueError:
            print(f"Некорректная дата рождения в записи: {entry.birthday}. Пропускаем.")

    if l:
        print("Записи в заданном диапазоне дат:")
        for i in l:
            print(i)
    else:
        print("Нет записей в заданном диапазоне дат.")


if __name__ == '__main__':
    cat = Cat('Барсик', '05.01.2020')
    cat.add_commands('спать', 'кушать')
    print(cat)

    camel = Camel('Джамал', '10.02.2018')
    camel.add_commands('бежать', 'есть')
    print(camel)

    hamster = Hamster('Харли', '15.03.2021')
    hamster.add_commands('бегать', 'есть')
    print(hamster)

    reestr.extend([cat, camel, hamster])
    while True:
        menu = '''
        Добавить животное - a
        Список команд животного - c
        Добавить команды животному - ac
        Обучить команде животное - n
        Вывести список по дате рождения - b
        Счетчик животных - cnt
        Выход - exit
         > '''
        com = input(menu).lower()
        match com:
            case 'a':
                add_animal()
            case 'ac':
                index = int(input("Введите номер животного: "))
                if 0 <= index < len(reestr):
                    reestr[index].add_commands(input("Введите команду: "))
                else:
                    print("Неверный номер животного.")
            case 'c':
                select_command()
            case 'n':
                index = int(input("Введите номер животного: "))
                if 0 <= index < len(reestr):
                    command = input("Введите название команды: ")
                    reestr[index].add_commands(command)
                else:
                    print("Неверный номер животного.")
            case 'b':
                list_b()
            case 'cnt':
                print(f'Количество животных: {len(reestr)}')
            case 'exit':
                break