# Задача 4. Дан список целых чисел. 
# Посчитать, сколько раз в нем встречается каждое число. 
# Например, если дан список [1, 1, 3, 2, 1, 3, 4], 
# то в нем число 1 встречается три раза, число 3 - два раза, 
# числа 2 и 4 - по одному разу.
import random
def spisok(size):
    spisok_1=[]
    print("Введите разброс элементов:   ")
    a=int(input("Начинается с:  "))
    b=int(input("Заканчивается:  "))
    i=0
    while i < size:
        q=random.randint(a,b)
        spisok_1.append(q)
        # print(q,i,sp)
        i+=1
    print(f"В списке:  {spisok_1}")
    spisok_2=bezPOVT(spisok_1)
    schet(spisok_1,spisok_2)
    return spisok_1
    
 
def bezPOVT(sp):
    sp1=[]
    for i in sp:
        if i not in sp1:
            sp1.append(i)
    # print(sp1) #
    return sp1
 
def schet(sp,sp1):
    for i in sp1:
        sp.count(i)
        print(f"Число {i} встречается {sp.count(i)} раз")
 
spisok(7)