first = int(input("Введите первое целое число: ")) #создание первой переменной с численным значением
second = int(input("Введите второе целое число: "))#создание второй переменной с численным значением
third = int(input("Введите третье целое число: "))#создание третьей переменной с численным значением
fours = int(input("Введите четвертое целое число: "))#создание четвертой переменной с численным значением

a = []#создание переменной, которая будет сохранять данные о чётных числах
if first % 2 == 0:#проверка на чётность
    a.append(first)#если число чётное, занесение в переменную а
if second % 2 == 0:#в следующих переменных повторение этого же процесса
    a.append(second)#
if third % 2 == 0:#
    a.append(third)#
if fours % 2 == 0:#
    a.append(fours)#

if a:#если какое либо значение занесено в переменную а, то выполняется условие
    print("Наибольшее четное число:", max(a))#вывод максимального четного числа
else:#
    print("not found")#если четных чисел нет, то выводится данная надпись