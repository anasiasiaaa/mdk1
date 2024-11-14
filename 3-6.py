number = input("Введите пятизначное число: ")
if len(number) == 5 and int(number)>0:
    a, b, c, d, e = number
    print(f"{a} 0 {c} 0 {e}")
else:
    print("Ошибка ввода. Введите положительное пятизначное число.")
