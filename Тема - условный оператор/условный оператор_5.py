#Напишите программу, которая у пользователя запрашивает одно число. 
#Находит делители данного числа от 2 до 10 и выводит на экран найденные делители 
while True: 
    A=[2,3,4,5,6,7,8,9,10] 
    B=[] 
    while True: 
        try: 
            a=int(input("Введи число ")) 
            print(type(a)) 
        except ValueError: 
            print("Вы ввели не число") 
            continue 
        break 
    print("введено ",a) 
    i=0 
    while i<len(A): 
        if a%A[i]==0: 
            B.append(A[i]) 
        i+=1 
    print("Число ",a,"делится на",B) 
    continue