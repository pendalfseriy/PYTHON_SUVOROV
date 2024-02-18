# Задание 1 
"""
Написать класс – обеденный стол. Учитывая следующие рекомендации:
Написать класс – обеденный стол.
Учитывая следующие рекомендации:
- создайте метод __init__(), внутри которого будут определены следующие динамические
свойства: ширина, длина, высота, цвет, количество посадочных мест
Начальные значения свойств берутся из входных параметров метода.
• создайте метод Print() – вывод на экран параметры кухонный стол– ширина-высота,
длина, цвет, количество посадочных мест
• Создать меню завтрак, меню обед, меню ужин. Каждое меню включает название блюда и
количество
• создайте метод «Покормить» - входные данные это вид меню, например завтрак,
количество человек. Каждый человек выбирает блюдо из меню. Результат вывод всех
выбранных блюд
• создайте метод «Счет» - подсчет стоимости завтрак/обеда/ужина
"""


# Задание 1 
"""
Написать класс – обеденный стол. Учитывая следующие рекомендации:
Написать класс – обеденный стол.
Учитывая следующие рекомендации:
- создайте метод __init__(), внутри которого будут определены следующие динамические
свойства: ширина, длина, высота, цвет, количество посадочных мест
Начальные значения свойств берутся из входных параметров метода.
• создайте метод Print() – вывод на экран параметры кухонный стол– ширина-высота,
длина, цвет, количество посадочных мест
• Создать меню завтрак, меню обед, меню ужин. Каждое меню включает название блюда и
количество
• создайте метод «Покормить» - входные данные это вид меню, например завтрак,
количество человек. Каждый человек выбирает блюдо из меню. Результат вывод всех
выбранных блюд
• создайте метод «Счет» - подсчет стоимости завтрак/обеда/ужина
"""
import random

breakfast={"чай":25,"какао":30,"каша":50,"бутерброд":45,"запеканка":60}
lunch={"чай":25,"сок":30,"суп":60,"гарнир":50,"котлета":90}
dinner={"чай":25,"компот":30,"каша":50,"гарнир":45,"пирог":60}
Menu1=[breakfast,lunch,dinner]
Menu1_1=["breakfast","lunch","dinner"]

class DiningTable():
    def __init__(self):
        self.width=int(input("Введите длину стола   "))    
        self.lenght=int(input("Введите ширину стола "))
        self.height=int(input("Введите высотуу стола    "))
        self.color=input("введи цвет    ")
        self.NumbSeats=int(input("Введите количество посадочных мест    "))
        # return self.NumbSeats
    
    def Print(self):
        print(f"длина стола {self.width}")
        print(f"ширина стола {self.lenght}")
        print(f"высоту стола {self.height}")
        print(f"цвет стола {self.color}")
        print(f"колмчество мест {self.NumbSeats}")
        

    def Feed(self):
        []
        print("\nbreakfast - 0\nlunch - 1\ndinner - 2\n")
        Position_Menu=int(input("какое меню будет выбрано?( Введите 0, 1 или 2)"))
        Key=Menu1[Position_Menu] #Выбранное меню
        Key_1=Menu1_1[Position_Menu]
        # print(Menu1[1])
        self.Key=Key
        print(f"\nвыбор из меню {Key_1}:")
        for i in Key.keys():
            print(f"{i} - {Key[i]}р")
        Spisok_select_menu=list(Key.keys()) #Список ключей из выбранного меню
        # print(Spisok_select_menu)
        Rand_of_Menu=random.sample(Spisok_select_menu,3) #Рандомный выбор 3 позиций из выбранного меню
        
        # print(Rand_of_Menu)
        self.sp_zkazov=[]   
        sp_zkazov=self.sp_zkazov# список со всеми выбранными позициями из данного меню с повторениями
        print("\n")
        for i in range(0,self.NumbSeats):
            Rand_of_Menu=random.sample(Spisok_select_menu,3) #Рандомный выбор 3 позиций из выбранного меню
            print(f"посетитель {i+1} заказал {Rand_of_Menu}")
            for i in Rand_of_Menu:
                sp_zkazov.append(i) #Заполнение списка всеми выбранными позициями из данного меню 
        # print(sp_zkazov)       
        self.spisok_select_bez_povt=[] # список со всеми выбранными позициями из данного меню без повторений
        spisok_select_bez_povt=self.spisok_select_bez_povt # список со всеми выбранными позициями из данного меню без повторений
        
    def SUM(self):
        for i in self.sp_zkazov:
            if i not in self.spisok_select_bez_povt:
                self.spisok_select_bez_povt.append(i)
        # print(spisok_select_bez_povt)
        quantity_of_position={} # словарь с количеством выбранных позиций
        for i in self.spisok_select_bez_povt:
            quantity=self.sp_zkazov.count(i)
            position={i:quantity}
            quantity_of_position[i]=quantity
        SUM=[]
        print("\nЧек:")
        for i in self.spisok_select_bez_povt:
            print(f"{i} {self.Key[i]} x {quantity_of_position[i]}р = {self.Key[i]*quantity_of_position[i]}р")
            summ=self.Key[i]*quantity_of_position[i]
            SUM.append(summ)
        REZ=sum(SUM)
        print(f"Итого:  {REZ}")

a = DiningTable()
a.Print()
a.Feed()
a.SUM()
