# Условный оператор
# 1.Напишите программу, которая запрашивает у пользователя три числа 
# в диапазоне 1-1000. 
# Компьютер генерирует два случайных числа 
# в диапазоне 1-100, которые определяют отрезок. 
# Определить какие  числа указанные пользователям попали в отрезок.
import random

Diap_1_100=[]
Diap_srez=[]
numbers=[]
Err='Вне границ диапазона'
i=1
while i<101: #
   Diap_1_100.append(i)
   i+=1
#print(Diap_1_100)  
A=random.randint(1,100)
B=random.randint(1,100)
print(A)
print(B)
if A<B:
    Diap_srez=Diap_1_100[Diap_1_100.index(A):Diap_1_100.index(B+1)] # Заполнение среза если A больше B
elif A>B:
    Diap_srez=Diap_1_100[Diap_1_100.index(B):Diap_1_100.index(A+1)] # Заполнение среза если B больше A
print(Diap_srez)
while True:
    try:
        a1=int(input("Введите 1 число [1,1000] "))
        numbers.append(a1)
    except ValueError:
        print("Вы ввели не число") 
        continue
    if (a1<1): 
        print(Err) 
        continue
    elif (1000<a1):
        print(Err) 
        continue 
    else:
        break    
while True:
    try:
        a2=int(input("Введите 2 число [1,1000]"))
        numbers.append(a2)
    except ValueError:
        print("Вы ввели не число") 
        continue
    if (a2<1): 
        print(Err) 
        continue
    elif (1000<a2):
        print(Err)  
        continue
    else:
        break    
while True:
    try:
        a3=int(input("Введите 3 число [1,1000]"))
        numbers.append(a3)
    except ValueError:
        print("Вы ввели не число") 
        continue
    if (a3<1) : 
        print(Err)  
        continue
    elif (1000<a3): 
        print(Err)  
        continue
    else:
        break    
result=[]
print(numbers)
for i in numbers:
    if i in Diap_srez:
        result.append(i)
print("В отрезок попали: ",result)