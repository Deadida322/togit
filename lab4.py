import csv
import os


class Number:
    __number = {}

    def __setattr__(self, key, value):
        self.__number[key] = int(value)

    def __getitem__(self, key):
        return self.__number[key]

    def set_number(self, key, value):
        self.__setattr__(key, value)

    def get_number(self, key):
        return self.__getitem__(key)


class Name:
    __name = {}

    def __setattr__(self, key, value):
        self.__name[key] = value

    def __getitem__(self, key):
        return self.__name[key]

    def set_name(self, key, value):
        self.__setattr__(key, value)

    def get_name(self, key):
        return self.__getitem__(key)


class Email:
    __email = {}

    def __setattr__(self, key, value):
        self.__email[key] = value

    def __getitem__(self, key):
        return self.__email[key]

    def set_email(self, key, value):
        self.__setattr__(key, value)

    def get_email(self, key):
        return self.__getitem__(key)


class Group:
    __group = {}

    def __setattr__(self, key, value):
        self.__group[key] = value

    def __getitem__(self, key):
        return self.__group[key]

    def set_group(self, key, value):
        self.__setattr__(key, value)

    def get_group(self, key):
        return self.__getitem__(key)


class SuperClass:
    number = Number()
    name = Name()
    email = Email()
    group = Group()

    def read_csv(self):
        with open("arr.csv", 'r') as arr:
            r = csv.DictReader(arr, delimiter=";")
            for i, row in enumerate(r):
                for j, item in enumerate(row):
                    if j == 0:
                        self.number.set_number(i, row["number"])
                    elif j == 1:
                        self.name.set_name(i, row["name"])
                    elif j == 2:
                        self.email.set_email(i, row["email"])
                    elif j == 3:
                        self.group.set_group(i, row["group"])

    def write_csv(self):
        with open("arr.csv", "w") as csv:
            w = csv.DictWriter(csv, delimiter=";", fieldnames=["number", "name", "email", "group"], lineterminator="\r")
            w.writeheader()
            i = 0
            while True:
                try:
                    w.writerow({
                        "number": self.number.get_number(i),
                        "name": self.name.get_name(i),
                        "email": self.email.get_email(i),
                        "group": self.group.get_group(i)
                    })
                    i += 1
                except KeyError:
                    break

    def rewrite_values(self, name, key, value):
        if name == "number":
            self.number.set_number(int(key), value)
        elif name == "name":
            self.name.set_name(key, value)
        elif name == "email":
            self.email.set_email(key, value)
        elif name == "group":
            self.group.set_group(key, value)
        else:
            raise Exception("Поле не обнаружено")
        self.write_csv()

    def sort_dict(self, arg):
        arr = []
        i = 0
        while True:
            try:
                arr.append({
                    "number": self.number.get_number(i),
                    "name": self.name.get_name(i),
                    "email": self.email.get_email(i),
                    "group": self.group.get_group(i)
                })
                i += 1
            except KeyError:
                break
        arr.sort(key=lambda item: item[arg])
        for i in range(len(arr)):
            print(arr[i])
            self.number.set_number(i, arr[i]["number"])
            self.name.set_name(i, arr[i]["name"])
            self.email.set_email(i, arr[i]["email"])
            self.group.set_group(i, arr[i]["group"])
        self.write_csv()

    def print_csv(self):
        i = 0
        while True:
            try:
                print({"number": self.number.get_number(i),
                       "name": self.name.get_name(i),
                       "email": self.email.get_email(i),
                       "group": self.group.get_group(i)})
                i += 1
            except KeyError:
                break

    def select_csv(self):
        i = 0
        while True:
            try:
                if self.number.get_number(i) > 2:
                    print({"number": self.number.get_number(i),
                           "name": self.name.get_name(i),
                           "email": self.email.get_email(i),
                           "group": self.group.get_group(i)})
                i += 1
            except KeyError:
                break

    @staticmethod
    def print_menu():
        obj = iter([ "1 - Изменить определённое поле", "2 - Вывести с id > 2", "3 - сортировать по ключу", "4 - подсчитать количество файлов"])
        while True:
            try:
                print(next(obj))
            except StopIteration:
                break

    @staticmethod
    def do_generator():
        for i in (i for i in range(10)):
            print(i, end=" ")
        print()

    @staticmethod
    def count_files(path):
        """
        Подсчёт количества файлов в директории
        :param path путь к папке
        """
        try:
            count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
            print(count)
        except:
            print("Неверный путь")
            return 0


def main():
    m = SuperClass()
    m.read_csv()
    m.print_menu()
    var = input()
    print('Изначальный список ')
    m.print_csv()
    if var == "1":
        m.rewrite_values(input("Поле: "), input("Ключ: "), input("Значение: "))
        m.print_csv()
    elif var == "2":
        print('Элементы больше 2 следующие')
        m.select_csv()
    elif var == "3":
        k = input("Ключ: ")
        m.sort_dict(k)
    elif var == "4":
        path = input('Введите путь')
        m.count_files(path)



main()
