# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Class:
    def __init__(self, class_room, teacher):
        self.class_room = class_room
        self.teacher = list(teacher)


class Person:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname

    def full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname


class Student(Person):
    def __init__(self, name, patronymic, surname, class_room, mather, father):
        Person.__init__(self, name, patronymic, surname)
        self._class_room = {'class_num': int(class_room.split()[0]), 'class_char': class_room.split()[1]}
        self.mather = mather
        self.father = father

    def full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def class_room(self):
        return "{}{}".format(self._class_room['class_num'], self._class_room['class_char'])

    def show_parents(self):
        print(f"Родители:\nМать:{self.mather}\nОтец:{self.father}")

    def show_class(self):
        print(f"Класс: {self._class_room}")


class Parents(Person):
    def __init__(self, name, patronymic, surname):
        Person.__init__(self, name, patronymic, surname)


class Teacher(Person):
    def __init__(self, name, patronymic, surname, dis):
        Person.__init__(self, name, patronymic, surname)
        self.dis = dis

    def full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname


teacher = [Teacher("Петр", "Семенович", "Кукушкин", "Математика"),
           Teacher("Федор", "Михайлович", "Иванов", "Русский язык")]
classes = [Class("5A", [teacher[0], teacher[1]]),
           Class("6Г", [teacher[1]]),
           Class("10Б", [teacher[0], teacher[1]])]
parents = [Person("Семен", "Семенович", "Кукин"),
           Person("Денис", "Витальевич", "Букин"),
           Person("Дмитрий", "Александрович", "Иванов")]

for f in classes:
    print(f.class_room)

for f in classes:
    print()
