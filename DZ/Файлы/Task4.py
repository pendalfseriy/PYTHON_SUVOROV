# Задача 4 В многострочном текстовом файле prices.txt каждая строка с
# помощью символа табуляции разделена на три колонки:
# 1 название товара,2. количество товара и3. цена за 1 шт.Выведите общую
# стоимость заказа с точностью до копеек.
Product_name=[
"скотч",
"ножницы",
"ручки",
"карандаши",
"ластики",
"стикеры",
"блокноты",
"файлы",
"скрепки",
"скобы"
]
quantity=[
4,
5,
3,
6,
3,
4,
5,
2,
4,
7
]
price=[
50.00,
59.99,
5.50,
4.50,
3.50,
34.99,
76.99,
44.99,
49.99,
50.00 
]
name='prices.txt'
def prices(name,Product_name,quantity,price):
    Check=check(len(Product_name),len(quantity),len(price))
    # print(Check)
    if Check==True:
        f=open(name,'w+',encoding='utf-8')
        for i in range(len(Product_name)):
            string_=[Product_name[i],str(quantity[i]),str(price[i])]
            # print(string_)
            string="   ".join(string_)+'\n'
            # print(string)
            f.writelines(string)
        f.close()
    elif Check!=True:
        print("не соответствие в столбцах")
    REZ_final=REZ(name)
    return(REZ_final)

def check(Pn,q,p):
    if Pn==q==p:
        Rez=True
    elif Pn!=q or Pn!=p:
        Rez=False
    return Rez
def REZ(name):
    f=open(name,'r',encoding='utf-8')
    string=f.read().splitlines()
    # print(list)
    f.close()
    Sum=[]
    for i in string:
        # print(i)
        list=i.split('  ')
        # print(list)
        multiply=int(list[1])*float(list[2])
        Sum.append(multiply)
    # print(Sum)
    REZ=sum(Sum)
    # print(REZ)
    REZ=str(format(REZ, '.2f'))
    # print(REZ)
    REZ=REZ.split('.')
    # print(REZ)
    REZ=' Руб. '.join(REZ)+" Коп."
    # print(REZ)
    return(REZ)

print(f"Общая стоимость заказа: {prices(name,Product_name,quantity,price)}")



