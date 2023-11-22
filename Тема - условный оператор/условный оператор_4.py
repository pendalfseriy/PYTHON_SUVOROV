# Напишите программу, которая определяет пройдет коробка 
# с размерами a*b*c в ящик с размерами x*y*z 
while True: 
    try: 
        a=int(input('Введите длину коробки a= ')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if a<0: 
        print("Вы отрицательное число") 
        continue 
    else: 
        break  
while True: 
    try: 
        b=int(input('Введите длину коробки b= ')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if a<0: 
        print("Вы отрицательное число") 
        continue 
    else: 
        break  
while True: 
    try: 
        c=int(input('Введите длину коробки c= ')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if c<0: 
        print("Вы отрицательное число") 
        continue 
    else: 
        break  
while True: 
    try: 
        x=int(input('Введите длину ящика x= ')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if x<0: 
        print("Вы отрицательное число") 
        continue 
    else: 
        break  
while True: 
    try: 
        y=int(input('Введите длину ящика y= ')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if y<0: 
        print("Вы отрицательное число") 
        continue 
    else: 
        break  
while True: 
    try: 
        z=int(input('Введите длину ящика z= ')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if z<0: 
        print("Вы отрицательное число") 
        continue 
    else: 
        break  
box1=[a,b,c] 
box2=[x,y,z] 
Str1="коробка с размерами " 
Str2="влезет в ящик с размерами " 
if ((a<=x) and (b<=y) and (c<=z)) or ((a<=x) and (c<=y) and (b<=z)) or ((b<=x) and (c<=y) and (a<=z)) or ((b<=x) and (a<=y) and (c<=z)) or ((c<=x) and (a<=y) and (b<=z))or ((c<=x) and (b<=y) and (a<=z)): 
    print(Str1,box1,Str2,box2) 
else: 
    print(Str1,box1,"не",Str2,box2)
