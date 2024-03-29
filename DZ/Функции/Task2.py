""" 
Основная ветка программы, не считая заголовков функций, состоит из одной
строки кода. Это вызов функции test(). В ней запрашивается на ввод целое число. Если
оно положительное, то вызывается функция positive(), тело которой содержит команду
вывода на экран слова "Положительное". Если число отрицательное, то вызывается
функция negative(), ее тело содержит выражение вывода на экран слова "Отрицательное".
"""

def test():
    while True:
        try:
            size=int(input("Введите целое число:    "))
            break
        except ValueError:
            print("Введено не целое число")
            continue
    if size>0:
        positive(size)
    elif size<0:
        negative(size)
    else:
        return 
     
def positive(size1):
    print(f"число {size1} положительное")
    
def negative(size1):
    print(f"число {size1} отрицательное")
 
test()