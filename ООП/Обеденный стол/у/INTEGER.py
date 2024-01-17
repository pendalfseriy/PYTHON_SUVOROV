# Задание 2 Написать класс – списки целых чисел. Учитывая следующие
# рекомендации:
# - создайте метод init(), внутри которого будут определен один параметр: размер
# списка. Начальные значения свойства берутся из входных параметров метода.
# ·
# создайте метод InputData позволяющий задать данные списка пользователем
# ·
# создайте метод InputDataRandom заполняющий список с помощью датчика
# случайных чисел
# ·
# создайте метод print() – вывод на экран содержимого списка
# ·
# создайте метод FindValue - который возвращает список индексов для
# искомого элемента
# ·
# создайте метод DelValue - который удаляет из списка искомый элемент.
# ·
# создайте метод FindMax- который возвращает максимальное значение из
# списка.
import random
 
class LIST_INTEGERS():
    def __init__(self):# Задаем размер списка
        
        while True:
            try:
                self.size =int(input("задайте размер списка    "))
                # print(self.size)
                # print(type(self.size))
                if type(self.size)==int:
                    break
            except ValueError:
                print("Введите целое число")
                continue

    def InputData(self):#Формироетя набор данных
        spisok=[]    
        while True:
            try:
                s=int(input("Введите набор данных  "))
                if s in spisok:
                    print("элемент уже есть")
                    continue
                spisok.append(s)
                print(f"Пополнен набор элементов:   {spisok}")
                continue
            except ValueError:
                print("Набор элементов для формирования списка")
                break
        print(spisok)
        return spisok
    
    def InputDataRandom(self,spisok,size):#Заполнение списка набором данных
        form=random.choices(spisok,k=size)
        # print(form)
        return form
    
    def Print(self,Print1):#Вывод сформированного списка
        print(f"Сформирован список: {Print1}")
    
    def FindValue(self,IND):#Вывод индексов
        b=[]
        for i in IND:
            b.append(IND.index(i))
        print(f"Индексы списка:     {b}")
        return b
    
    def DelValue(self,EL):#Удаление заданного элемента
        while True:
            try:
                Rez=int(input(f"какой элемент удалить?  {EL}"))
                IND=EL.index(Rez)
                print(f"Удален элемент: {Rez} (первый элемент по индексу {IND})")
                EL.remove(Rez)
                print(EL)
                return EL
                
            except ValueError:
                    print("ВВедите элемент из текущего списка")
                    continue  
      
    def FindMax(self,Znach):#Вывод максимума
        Max=max(Znach)
        print(f"{Max} максимальный элемент")
        return Max
    
LIST=LIST_INTEGERS()

# print(LIST.size,)
# print(i,"22")
a=LIST.InputData()
# print(a)
# print(type(a))
b=LIST.InputDataRandom(a,LIST.size)
# print(b)
c=LIST.Print(b)
d=LIST.FindValue(b)
# print(d)
e=LIST.DelValue(b)
# print(e)
F=LIST.FindMax(e)
