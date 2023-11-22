# Напишите программу, которая у пользователя запрашивает три числа 
# определяющие стороны треугольника. Определить тип треугольника: 
# равнобедренный, равносторонний, прямоугольный, обычный 
T1='треугольник равнобедренный' 
T2='треугольник равносторонний' 
T3='треугольник прямоугольный' 
T4='треугольник обычный' 
while True: 
    try: 
        A=int(input('Введите A сторону ')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if A<0: 
        print("Отрицательная длина, введите положительное число") 
        continue 
    else: 
        break 
while True: 
    try: 
        B=int(input('Введите B сторону')) 
    except ValueError: 
        print("Отрицательная длина") 
        continue 
    if B<0: 
        print("Отрицательная длина, введите положительное число") 
        continue 
    else: 
        break 
while True: 
    try: 
        C=int(input('Введите C сторону')) 
    except ValueError: 
        print("Вы ввели не число") 
        continue 
    if C<0: 
        print("Отрицательная длина, введите положительное число") 
        continue 
    else: 
        break 
if (B<A) and (C<A): 
    GIP=A 
    if B==C: 
        print(T1) 
    elif B!=C: 
        if A*A==(B*B+C*C): 
            print(T3) 
        elif A*A!=(B*B+C*C):
            print(T4) 
elif(A<B) and (C<B): 
    GIP=B 
    if A==C: 
        print(T1) 
    elif A!=C: 
        if B*B==(A*A+C*C): 
            print(T3) 
        elif B*B!=(A*A+C*C): 
            print(T4) 
elif(A<C) and (B<C): 
    GIP=C 
    if A==B: 
        print(T1) 
    elif A!=C: 
        if C*C==(A*A+B*B): 
            print(T3) 
        elif C*C!=(A*A+B*B): 
            print(T4) 
elif (A==B and (C<A and C<B)) or (A==C and (B<A and B<C)) or (B==C and (A<B and A<C)):
    print(T1)
elif ((A==B and C<A) or (A==C and B<A) or (B==C and A<B))and((A*A==(B*B+C*C))or(B*B==(A*A+C*C))or(C*C==(A*A+B*B))):
    print(T1,' и ',T3)
elif A==B==C: 
    print(T2)