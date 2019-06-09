__author__ = 'Бежук Валерий Эдуардович'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    fib = []
    sumFib = 0
    firstSum = n
    secondSum = 0

    while (sumFib < m):
        sumFib = firstSum + secondSum
        firstSum = secondSum
        secondSum = sumFib
        if sumFib > m:
            break

        fib.append(sumFib)

    return fib

print(fibonacci(1,20)) #добавил проверку. Надеюсь, я правильно понял условие.

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()



def sort_to_max(origin_list):
    sortList = []
    sortOriginList = list(origin_list)
    while len(sortList) != len(origin_list):
        m = min(sortOriginList)
        sortList.append(min(sortOriginList))
        sortOriginList.remove(m)
    return sortList



sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

my_list = ['да','нет','да','да','не знаю','может быть ','ничего','да борода',
           'никогда','нет','никак нет','да','да','да джигурда']

def my_filter(fun , l):

    fil_list = []
    for i in l:
        if fun(i) == True:
            fil_list.append(i)

    return fil_list


print(my_filter(lambda x: x == 'да', my_list))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1, A2, A3, A4 = (5, 5), (2, 4), (6, 3), (9, 4)

def parallelogram(a, b, c, d):
    if a[0] - d[0] == b[0] - c[0] and a[1] - d[1] == b[1] - c[1]:
        print("Стороны попарно параллельны, а значит и равны. Данные точки являются вершинами параллелограмма")
    else:
        print("Стороны не равны и не параллельны. Данные точки не являются вершинами параллелограмма")


parallelogram (A1, A2, A3, A4)

