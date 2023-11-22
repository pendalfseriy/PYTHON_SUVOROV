# Напишите программу, которая у пользователя запрашивает две точки 
# (верхний левый гол, нижний правый угол) на координатной плоскости, 
# например (2,3), (3,5). По этим двум точкам строится прямоугольник. 
# Подсчитать периметр прямоугольника, площадь прямоугольника. 
# Далее программа запрашивает еще две точки 
# (верхний левый гол, нижний правый угол) на координатной плоскости, 
# например (1,1), (4,4) второго прямоугольника. 
# Определить прямоугольники пересекаются хотя бы по одной стороне или нет. 
x1_rectangle1=int(input('x1 = ')) 
y1_rectangle1=int(input('y1 = ')) 
P1=[x1_rectangle1,y1_rectangle1] #Координата 1 точки 1 прямоугольника 
print("Точка 1 у 1 прямоугольника: ",P1) 
x2_rectangle1=int(input('x2 = ')) 
y2_rectangle1=int(input('y2 = ')) 
P2=[x2_rectangle1,y2_rectangle1] #Координата 2 точки 1 прямоугольника 
print("Точка 2 у 1 прямоугольника: ",P2) #Условия для работы счетчика в циклк while (i+=1) в циклах для нахождения точек у сторон 1 прямоугольника: 
if x1_rectangle1>x2_rectangle1: 
    length=x1_rectangle1-x2_rectangle1 
elif x1_rectangle1<x2_rectangle1: 
    length=x2_rectangle1-x1_rectangle1 
if y1_rectangle1>y2_rectangle1: 
    width=y1_rectangle1-y2_rectangle1 
elif y1_rectangle1<y2_rectangle1: 
    width=y2_rectangle1-y1_rectangle1 
S=length*width # Нахождение периметра 1 прямоугольника 
P=(length+width)*2# Нахождение площади 1 прямоугольника 
print("Длина= ", length," Ширина= ",width," Периметр=",P," Площадь= ",S) 
D1=[]#список точек по 1 стороне 1 прямоугольника 
D2=[]#список точек по 2 стороне 1 прямоугольника 
Diap_P1=[] 
if y1_rectangle1<y2_rectangle1:# Две длины/готово 
    i=y1_rectangle1 
    while i<=y2_rectangle1: 
        Dl1=[x1_rectangle1,i] 
        Dl2=[x2_rectangle1,i] 
        D1.append(Dl1) 
        D2.append(Dl2) 
        i+=1 # print(D1)#debug множество точек по 1 длине # 
#print(D2) #debug множество точек по 2 длине 
elif y2_rectangle1<y1_rectangle1: 
    i=y2_rectangle1 
    while i<=y1_rectangle1: 
        Dl1=[x1_rectangle1,i] 
        Dl2=[x2_rectangle1,i] 
        D1.append(Dl1) 
        D2.append(Dl2) 
        i+=1 
# print(D1)#debug множество точек по 1 длине 
# print(D2) #debug множество точек по 2 длине 
Points1=[] 
Shir1=[]#список точек по 3 стороне 1 прямоугольника 
Shir2=[]#список точек по 4 стороне 1 прямоугольника 
if x1_rectangle1<x2_rectangle1:# Две ширины /готово 
    i=x1_rectangle1 
    while i<=x2_rectangle1: 
        Sh1=[i,y1_rectangle1] 
        Sh2=[i,y2_rectangle1] 
        Shir1.append(Sh1) 
        Shir2.append(Sh2) 
        i+=1 # print(Shir1)#debug множество точек по 3 длине 
# print(Shir2) #debug множество точек по 4 длине 
elif x2_rectangle1<x1_rectangle1: 
    i=x2_rectangle1 
    while i<=x1_rectangle1: 
        Sh1=[i,y1_rectangle1] 
        Sh2=[i,y2_rectangle1] 
        Shir1.append(Sh1) 
        Shir2.append(Sh2) 
        i+=1 
# print(Shir1)#debug множество точек по 3 длине 
# print(Shir2) #debug множество точек по 4 длине 
Diap_P=[] 
Diap_Massive=[Shir1,Shir2,D1,D2] 
for i in Diap_Massive: 
    Diap_P.extend(i) 
# print(Diap_P) 
for i in Diap_P: 
    if i not in Diap_P1: 
        Diap_P1.append(i) 
# print(Diap_P1) #множество точек 
#_________ 
x1_rectangle2=int(input('x1 = ')) 
y1_rectangle2=int(input('y1 = ')) 
P1=[x1_rectangle2,y1_rectangle2] #Координата 1 точки 1 прямоугольника 
print("Точка 1 у 2 прямоугольника: ",P1) 
x2_rectangle2=int(input('x2 = '))  
y2_rectangle2=int(input('y2 = ')) 
P2=[x2_rectangle2,y2_rectangle2] #Координата 2 точки 1 прямоугольника 
print("Точка 2 у 2 прямоугольника: ",P2) 
#Условия для работы счетчика в циклк while (i+=1) в циклах для нахождения точек у сторон 1 прямоугольника: 
if x1_rectangle2>x2_rectangle2: 
    length=x1_rectangle2-x2_rectangle2 
elif x1_rectangle2<x2_rectangle2: 
    length=x2_rectangle2-x1_rectangle2 
if y1_rectangle2>y2_rectangle2: 
    width=y1_rectangle2-y2_rectangle2 
elif y1_rectangle2<y2_rectangle2: 
    width=y2_rectangle2-y1_rectangle2 
D1=[]#список точек по 1 стороне 1 прямоугольника 
D2=[]#список точек по 2 стороне 1 прямоугольника 
Diap_P2=[] 
if y1_rectangle2<y2_rectangle2:# Две длины/готово 
    i=y1_rectangle2 
    while i<=y2_rectangle2: 
        Dl1=[x1_rectangle2,i] 
        Dl2=[x2_rectangle2,i] 
        D1.append(Dl1) 
        D2.append(Dl2) 
        i+=1 # print(D1)#debug множество точек по 1 длине 
# print(D2) #debug множество точек по 2 длине 
elif y2_rectangle2<y1_rectangle2: 
    i=y2_rectangle2 
    while i<=y1_rectangle2:
        Dl1=[x1_rectangle2,i] 
        Dl2=[x2_rectangle2,i] 
        D1.append(Dl1) 
        D2.append(Dl2) 
        i+=1 # print(D1)#debug множество точек по 1 длине 
# print(D2) #debug множество точек по 2 длине 
Points1=[] 
Shir1=[]#список точек по 3 стороне 1 прямоугольника 
Shir2=[]#список точек по 4 стороне 1 прямоугольника 
if x1_rectangle2<x2_rectangle2:# Две ширины /готово 
    i=x1_rectangle2 
    while i<=x2_rectangle2: 
        Sh1=[i,y1_rectangle2] 
        Sh2=[i,y2_rectangle2] 
        Shir1.append(Sh1) 
        Shir2.append(Sh2) 
        i+=1 
# print(Shir1)#debug множество точек по 3 длине 
# print(Shir2) #debug множество точек по 4 длине 
elif x2_rectangle2<x1_rectangle2: 
    i=x2_rectangle2 
    while i<=x1_rectangle2: 
        Sh1=[i,y1_rectangle2] 
        Sh2=[i,y2_rectangle2] 
        Shir1.append(Sh1) 
        Shir2.append(Sh2) 
        i+=1 
# print(Shir1)#debug множество точек по 3 длине # 
#print(Shir2) #debug множество точек по 4 длине 
Diap_P=[] 
Diap_Massive=[Shir1,Shir2,D1,D2] 
for i in Diap_Massive: 
    Diap_P.extend(i) 
# print(Diap_P)#debug множество точек по периметру с повторениями 
for i in Diap_P: 
    if i not in Diap_P2: 
        Diap_P2.append(i) 
# print(Diap_P2) #debug множество точек по периметру без повторений 
Per=[] 
LENP1=len(Diap_P1) 
LENP2=len(Diap_P2) 
# i=0 
# while i < LENP1: 
# if i in Diap_P2: 
# Per.append(Diap_P1[i]) 
for i in Diap_P1: 
    if i in Diap_P2: 
        Per.append(i) 
print("пересекается в ",Per)