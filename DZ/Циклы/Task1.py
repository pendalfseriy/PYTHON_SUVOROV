"""
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1. Ввод данных
осуществляется в виде строки. В зависимости от типа адреса (описаны ниже), вывести на
• «unicast» - если первый байт в диапазоне 1-223
• «multicast» - если первый байт в диапазоне 224-239
• «local broadcast» - если IP-адрес равен 255.255.255.255
• «unassigned» - если IP-адрес равен 0.0.0.0
• «unused» - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
qq=[]
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
                    print(f"{i} вне диапазона значений октета")
                    f1=1 
                    continue
                   
        elif len(qq)!=4:
            print("не 4 октета")
            continue
        if f1==1:
            continue
        break

    except ValueError:
        print("Допустимы только целые числа")
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





# • «unicast» - если первый байт в диапазоне 1-223
# • «multicast» - если первый байт в диапазоне 224-239
# • «local broadcast» - если IP-адрес равен 255.255.255.255
# • «unassigned» - если IP-адрес равен 0.0.0.0
# • «unused» - во всех остальных случаях