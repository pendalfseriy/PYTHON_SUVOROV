#Задача_2
# Пользователь вводит две строки из трех символов, например "234", "456"
# НАйти все элементы списка которые попали в отрезок из суммы этих чисел
# "234" - 9
# "456" - 15
mes1="Введите число из трех символов: "
mes2="число не трехзначное"
mes3="Суммы у 1 и у 2 числа"
sum1=[]
sum2=[]

while True:
    try:
        print("1 строка")
        number1=int(input(mes1))
        number1=str(number1)
    except ValueError:
        print("Вы ввели не число")
        continue
    if 3<len(number1):
        print(mes2)
        continue
    elif len(number1)<3:
        print(mes2)
        continue
    break
#print(type(number1),number1)#Debug работы с исключениями
while True:
    try:
        print("2 строка")
        number2=int(input(mes1))
        number2=str(number2)
    except ValueError:
        print("Вы ввели не число")
        continue
    if 3<len(number2):
        print(mes2)
        continue
    elif len(number2)<3:
        print(mes2)
        continue
    break

for i in number1:
    sum1.append(int(i))
for i in number2:
    sum2.append(int(i))

SUM1=sum(sum1)
SUM2=sum(sum2)

print(mes3,": ",SUM1,SUM2)
if SUM2<SUM1:
    REZ=[i for i in range(SUM2,SUM1+1)]
    print(REZ)
elif SUM1<SUM2:
    REZ=[i for i in range(SUM1,SUM2+1)]
    print(REZ)
elif SUM1==SUM2:
    print(SUM1 or SUM2)
