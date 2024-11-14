import random #добавление модуля рандом, для рандомизации ходов

winning_moves = { #задача правил (камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень)
    'камень': 'ножницы',
    'ножницы': 'бумага',
    'бумага': 'камень'
}

user_wins = 0 #подсчет (статистика) выигранных матчей игроком
computer_wins = 0 #статистика выигранных матчей компьютером
user_moves_count = {'камень': 0, 'ножницы': 0, 'бумага': 0} #какие элементы выбирали чаще всего

try:
    n = int(input("Введите количество игр: "))#задача количества игр, чтобы определить, когда выводить статистику
except ValueError:
    print("Введите числовое целое значение количества игр")

for _ in range(n): #генерация последовательности ходов
    user_move = input("Введите ваш ход (камень, ножницы, бумага): ").lower() #ввод хода и проверка,
    #чтобы введенный ход совпадал с доступными
    
    if user_move not in winning_moves: #вывод ошибки при вводе не того хода
        print("Неверный ввод! Попробуйте снова.")
        continue
    
    user_moves_count[user_move] += 1 #подсчет ходов пользователя

    computer_move = random.choice(list(winning_moves.keys()))#случайный ход компьютера
    print(f"Компьютер выбрал: {computer_move}")
    
    if user_move == computer_move: #определение результатов игры 
        print("Ничья!")
    elif winning_moves[user_move] == computer_move:
        print("Вы выиграли!")
        user_wins += 1
    else:
        print("Компьютер выиграл!")
        computer_wins += 1

print("\nСтатистика:") #вывод статистики игры
print("Количество выигрышей пользователя:", user_wins)
print("Количество выигрышей компьютера:", computer_wins)
print("Ходы пользователя:")
for move, count in user_moves_count.items():
    print(f"{move}: {count}")

if user_moves_count['камень'] > user_moves_count['ножницы'] and user_moves_count['камень'] > user_moves_count['бумага']:
#анализ ходов игрока для того, чтобы компьютер не всегда выдавал по рандому. если пользователь чаще выбирает камень,
#то компьютер выберет бумагу
    computer_choice = 'бумага'
elif user_moves_count['ножницы'] > user_moves_count['камень'] and user_moves_count['ножницы'] > user_moves_count['бумага']:
    computer_choice = 'камень'
elif user_moves_count['бумага'] > user_moves_count['камень'] and user_moves_count['бумага'] > user_moves_count['ножницы']:
    computer_choice = 'ножницы'
else:
    computer_choice = random.choice(list(winning_moves.keys())) #если равные, случайный выбор

