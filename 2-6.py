try:
    contribution=int(input("Введите сумму вклада в банк: "))
    percent=int(input("Введите годовой процент: "))
    calculation=(contribution*(1+(percent/100))**5)
    calculations=round (calculation, 2)
except ValueError:
    print("Ошибка. Введите целочисленные значения")
result=print(f"Вклад в конце срока: {calculations}")
