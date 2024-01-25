# Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое
# число. Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается три раза,
# число 3 - два раза, числа 2 и 4 - по одному разу.
def spisok(size):    
    import random
    ii=[]
    print("Введите разброс:   ")
    a=int(input("Начало:    "))
    b=int(input("Конец:    "))
    if a<b:
        i=0
        while i<=size:
            ii.append(random.randint(a,b))
            print(ii)
            i=+1
    elif a>b:
        i=0
        while i<=size:
            ii.append(random.randint(b,a))
            print(ii)
            i=+1
spisok(5)