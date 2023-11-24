#сортируется: сначала четные потом нечетные
list_1=[21,22,23,24,25,26,27,28]
print(list_1)
a=len(list_1)
print(a)
L=len(list_1)
i=0
while i<L:
    if list_1[i]%2==0:
        list_1.append(list_1[i])
#list_1.remove(list_1[i])
    i+=1
print(list_1)
i=0
while i<L:
    if list_1[i]%2!=0:
        list_1.append(list_1[i])
#list_1.remove(list_1[i])
    i+=1
print(list_1)
A=len(list_1)
print(A)
i=0
print(list_1[a:A])