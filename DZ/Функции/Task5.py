# Сдвиг также должен быть кольцевым, то есть элемент, вышедший за пределы списка, 
# должен появляться с другого его конца.
# sdv=int(input("Введите сдвиг:   "))
sp=[1,2,3,4,5,5]
beginning=sp[:]
print(sp)

def Input_Shift(): 
    while True:
        try:
            print("")
            sdv=int(input("(положительное число - сдвиг вправо)\n(отрицательное число - сдвиг влево)\nВведите сдвиг:   "))
            return sdv
        except ValueError:
            print("число должно быть типа int")
            continue

def reverse(list):
    list.reverse()
    print("Инвертирование:  ",list)
    return list

def shift(list,sdv):
    i=0
    while i<sdv:
        list.append(list[0])
        list.remove(list[0])
        print(list,"-->") #проверка сдвига
        i+=1
    return list 
  
def sdvig(list,sd):
    if sd>0:
        reverse(list)
        shift(list,sd)
        reverse(list)
        return list
    elif sd<0:
        shift(list,-1*sd)

sdv=Input_Shift()       
Rez=sdvig(sp,sdv)
print(f"Результат: \n{beginning}\n{Rez}")