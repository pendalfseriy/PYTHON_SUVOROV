# Задача 1 Создайте файл nums.txt, содержащий несколько чисел,
# записанных через пробел. Напишите программу, которая подсчитывает и
# выводит на экран общую сумму чисел, хранящихся в этом файле.
string = '1 2 2 323 2 3'
f = open('nums.txt', 'w+')
f.write(string)
f.close()
f=open('nums.txt','r+')
q=f.read().split(" ")
q=[int(i) for i in q]
print(sum(q))
f.close()
