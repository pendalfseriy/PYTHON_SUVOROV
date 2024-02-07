"""
Написать программу – игра - угадай, в которой с помощью функции random
генерируется случайное число от 1 до 50 Пользователю предлагается угадать данное
число, на основе подсказать – загаданное число больше или меньше числа пользователя.
Вывести число попыток отгадывания числа
"""
import random
print("Угадай число от 1 до 50")
chislo=random.randint(1,50)
print(chislo)
popitka=0
i=0
while i==0:
    try:
        print(popitka)
        q=int(input("введи число:   "))
    except ValueError:
        print("неверный формат")
        continue
    popitka+=1

    if q>chislo:
        print("Загаданное число меньше ")
    elif q<chislo:
        print("Загаданное число больше ")
    elif q==chislo:
        print("Вы угадали ")
        i+=1
    
# print(popitka)
print(f"Загадано число {q}/nКоличество попыток {popitka}")
