"""
Задача 1 
Написать программу, которая последовательно вызывает три функции.
Функция 1 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело
на 3, функция 2 – подсчитывает для заданного отрезка чисел все числа, которые делятся
нацело на 4, Функция 3– подсчитывает для заданного отрезка чисел все числа, которые
делятся нацело на 5
"""
section=[]

while True:
    try:    
        beginning=int(input("введите начало отрезка:  "))
        break
    except ValueError:
        print("Введите число")
        continue
while True:
    try:        
        end=int(input("введите конец отрезка:  "))
        break
    except ValueError:
        print("Введите число")
        continue

if beginning<end:
    section=[i for i in range(beginning,end+1)] 
elif beginning>end:
    section=[i for i in range(end,beginning+1)]

print(section)

def division3(section):
    div=[]
    for i in section:
        if i%3==0:
            div.append(i)
    return div

def division4(section):
    div=[]
    for i in section:
        if i%4==0:
            div.append(i)
    return div

def division5(section):
    div=[]
    for i in section:
        if i%5==0:
            div.append(i)
    return div

print(division3(section))
print(division4(section))
print(division5(section))
