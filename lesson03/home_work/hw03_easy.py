__author__ = 'Бежук Валерий Эдуардович'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):

    numberOne = number * 10**ndigits # ввел дополнительные переменные для того, чтобы было понятнее в режиме отладки.
    numberTwo = (number*10**ndigits)//1

    if numberOne - numberTwo > 0.5:
       numberOne = ((numberOne + 1) // 1) / 10**ndigits

    return numberOne

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

    strTicketNumber = str(ticket_number)
    firstSum = 0
    secondSum = 0

    if len(strTicketNumber) % 2 != 0:
        return False

    for i in range(len(strTicketNumber) % 2):   #если я всё правильно понял и сделал,
        firstSum += int(strTicketNumber[i])     #то теперь можно применить эту функцию не только к шестизначным номерам
        secondSum += int(strTicketNumber[-i - 1])

    return firstSum == secondSum

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(43617511)) #добавил еще одну проверку, чтобы удостовериться
