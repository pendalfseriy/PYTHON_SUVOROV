# Задача 3 Напишите функцию reverse(in_file, out_file), которая читает
# строки из файла in_file и создает файл out_file, куда сохраняет прочитанные
# строки в обратном порядке.

text='''Вечерело
Жужжали мухи
Светил фонарик 
Кипела вода в чайнике 
Венера зажглась на небе 
Деревья шумели 
Тучи разошлись
Листва зеленела'''

in_file='in_file.txt'
out_file='out_file.txt'

f=open(in_file,'w+',encoding='utf-8')
f.write(text)
f.close()

def reverse(in_file, out_file):
    f=open(in_file,'r',encoding='utf-8')
    list1=f.readlines()
    # print(list1) #исходное содержание
    list1[-1]=list1[-1]+'\n'
    list1.reverse()
    list1[-1]=list1[-1].rstrip()
    # print(list1) #в обратном порядке
    f.close()


    f=open(out_file,'w+',encoding='utf-8')
    f.writelines(list1)
    f.close()

    f=open(out_file,'r',encoding='utf-8')
    print(*f)
    f.close()

reverse(in_file, out_file)