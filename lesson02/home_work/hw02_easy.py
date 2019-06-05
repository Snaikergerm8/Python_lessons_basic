__author__ = 'Бежук Валерий Эдуардович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

fruit = ["киви", "ананас", "персик", "банан", "яблоко"]
i = 1
for f in fruit:
    print('{}. {}'.format(i,f))
    i+=1

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = [1,2,3,5,6,8,2]
b = [4,2,12,23,1,8]
n = 0
for i in b:
    while len(a) > n:
        if i == a[n]:
            a.pop(n)
        n+=1
    n = 0
print(a)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [1,2,3,5,6,8,2]
b = []
for i in a:
    if i % 2 == 0:
        i /= 4
        b.append(i)
    else:
        i *= 2
        b.append(i)
print(b)
