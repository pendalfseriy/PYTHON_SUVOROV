"""
Сделать копию скрипта задания 1 Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
• состоит из 4 чисел (а не букв или других символов)
• каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес».
Сообщение «Неправильный IP-адрес» должно выводиться только один раз, даже если
несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
qq=[]
sch=0
ii=0
while True:
    f1=0
    ch=(input("введи IP-адреса в формате 10.0.1.1:  "))
    q=(ch.split('.'))
    try:
        qq=[int(i) for i in q]
        
        if len(qq)==4:
            for i in qq:
                if i not in range(0,256):
                    if sch==0: 
                        print("Неправильный IP-адрес")
                    f1=1 
                    sch=sch=+1
                    continue
                   
        elif len(qq)!=4:
            if sch==0:
                print("Неправильный IP-адрес")
            sch=sch=+1
            continue
        if f1==1:
            continue
        break

    except ValueError:
        if sch==0:
            print("Неправильный IP-адрес")
        sch=sch=+1
        continue

# print(qq)
if qq[0] in range(1,223): 
    print("«unicast»")
elif qq[0] in range(224,239): 
    print("«multicast»")
elif qq.count(255)==len(qq): 
    print("«local broadcast»")
elif qq.count(0)==len(qq): 
    print("«unassigned»")
else:
    print("«unused»")
    print(sch)