score = 0
import random
while True:
    computer = random.choice(["камень", "ножницы", "бумагу"])
    choice = input("Камень, ножницы или бумага? ").lower().strip()
    print(f"Я выбрал {computer}!")
    if choice == computer:
        question = input("Ничья. Хотите сыграть ещё раз? (да/нет) ").lower().strip()
    elif (choice == "камень" and computer == "ножницы") or (choice == "ножницы" and computer == "бумагу") or (choice == "бумага" and computer == "камень"):
        question = input("Вы выиграли. Хотите сыграть ещё раз? (да/нет) ").lower().strip()
        score += 1
    else:
        question = input("Вы проиграли. Хотите сыграть ещё раз? (да/нет) ").lower().strip()
        score -= 1
    if question == "нет":
                if score < 0:
                    lose = input(f"Ваш счёт ужасающий: {score}. Вы уверены что хотите закончить игру? (да/нет) ").lower().strip()
                    if lose == "нет":
                        continue
                    else:
                        print(f"Вы проиграли со счётом: {score}.")
                elif score == 0:
                    print(f"Между нами ничья. Счёт: {score}.")
                else:
                    print(f"Вы выиграли со счётом: +{score}.")
                break