import random
while True:
    attempts = 0
    computer = random.randint(1, 100)
    difficulty = input("Выберите уровень сложности: \n1. Лёгкий (10 попыток) \n2. Средний (7 попыток) \n3. Сложный (5 попыток) \nВведите 1, 2 или 3: ")
    if difficulty == "2":
        max_attempts = 7
    elif difficulty == "3":
        max_attempts = 5
    else:
        max_attempts = 10
    while True:
        try:
            number = int(input("Компьютер загадал число от 1 до 100. Попробуйте угадать его: "))
        except ValueError:
            print("Нужно ввести число!")
            continue
        attempts += 1
        if number > computer:
            print("Меньше!")
        elif number < computer:
            print("Больше!")
        else:
            question = input(f"Вы угадали! \nПопыток: {attempts} \nХотите сыграть ещё раз? (да/нет) ").lower().strip()
            if question == "нет":
                print("Спасибо за игру!")
                break
            elif question == "да":
                break
        if attempts >= max_attempts:
            print(f"Вы исчерпали все попытки. Загаданное число было: {computer}")
            question = input("Хотите сыграть ещё раз? (да/нет) ").lower().strip()
            if question == "нет":
                print("Спасибо за игру!")
                break
            else:
                break
    if question == "нет":
        break