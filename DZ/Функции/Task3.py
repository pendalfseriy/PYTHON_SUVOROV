# Напишите программу по следующему описанию.
# В основной ветке программы вызывается функция cylinder(), которая вычисляет
# площадь цилиндра.
# В теле cylinder определена функция circle, вычисляющая площадь круга по формуле
# В теле cylinder у пользователя спрашивается, хочет ли он получить только площадь
# боковой поверхности цилиндра, которая вычисляется по формуле 2πrh, или полную
# площадь цилиндра.
# В последнем случае к площади боковой поверхности цилиндра должен добавляться
# удвоенный результат вычислений функции circle().

import math

def cylinder():
    r=int(input("Введите радиус основания:  "))
    h=int(input("Введите высоту:  "))
    Scircle=circle(r)
    print(f"Площадь круга:  {Scircle}")
    print(("1:  вычислить площадь боковой поверхности цилиндра"))
    print(("2:  вычислить полную площадь цилиндра"))
    var=int(input("Введите 1 или 2: "))
    
    Bok=cylinder_bok(r,h)
    if var==1:
        print(Bok)
        return Bok
    elif var==2:
        Sall=float(Scircle*2+Bok) 
        print(Sall)
        return Sall
 
def cylinder_bok(r,h):
    Sbok=float(2*math.pi*r*h)
    return Sbok
 
def circle(r):
    Scircle=float(math.pi*r*r)
    return Scircle

cylinder()
