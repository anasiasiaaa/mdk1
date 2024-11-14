#2.	Вычислите значение выражения (x+1)2+3(x+1) при x=1.7.

import math #подключение модуля с математикой в код
def math_expression(): #сзоздание функции, которая ничего не возвращает
    x = 1.7 #задача параметров x
    first_expression = (x+1) #первое действие
    second_expression = (2+3) #второе действие
    third_expression = (x+1) #третье действие
    expression = (first_expression * second_expression * third_expression)
    #умножение всех скобок
    print (expression) #вывод результата

