# Даны два списка целых чисел одинаковый длины. Например [5,4,3] и [2,1,3].
# Сформировать третий список полученный путем нахождения разницы меду списками,
# например [5-2, 4-1,3-3] итоговый список [3,3,0]. Формирование третьего списка
# осуществляется с использованием функции


a=[5,4,3]
b=[2,1,3]

def check(list1,list2):
    if len(list1)==len(list2):
        LEN=len(list1)
        Rez=equally(list1,list2,LEN)
        return Rez
    elif (len(list1)<len(list2) and list1!=None):
        print("Error разные длины списков")
    elif (len(list1)>len(list2) and list2!=None):
        print("Error разные длины списков")
    elif len(list1)==0 and len(list2)!=0:
        LEN=len(list2)
        list1=nul(list1,LEN)
        print(list2)
        Rez=equally(list1,list2,LEN)
        return Rez
    elif len(list1)!=0 and len(list2)==0:
        LEN=len(list1)
        list2=nul(list2,LEN)
        Rez=equally(list1,list2,LEN)
        return Rez
    elif len(list2)==0 and len(list1)==0:
        Rez=[]
        return Rez

def equally(list1,list2,LEN):
    list3=[]
    i=0
    while i<LEN:
        c_=list1[i]-list2[i]
        list3.append(c_)
        i+=1
    return list3

def nul(list,LEN):
    list.clear()
    i=0
    while i<LEN:
        list.append(0)
        i+=1
    return list

print(check(a,b))