#поменять местами самый большой и самый маленький элемент списка 
import random 
spisok=[random.randint(18,21) for i in range(1,10)] 
print(spisok) 
a=spisok.index(20) 
spisok[a]=200 
spisok_1=spisok[:]
print(spisok)
max=spisok.index(max(spisok)) 
min=spisok.index(min(spisok)) 
#print("MAX index",max,"=",MAX,"MIN index",min,"=",MIN) 
print(spisok_1) 
#print(max)`` 
spisok_1[max]=spisok[min] 
spisok_1[min]=spisok[max] 
print(spisok_1)