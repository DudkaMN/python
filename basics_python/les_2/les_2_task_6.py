products = []
n = 1
while True:
    prod = input('введите + для добавления товара или End для завершения составления списка: ')
    if prod == "+":
        prod_dict = {'название': input('введите название товара: '), 'цена': input('введите цену товара: '), 'количество': input('введите количество товара: ') ,'ед.': input('введите единицу измерения: ')}
        prod_tuple = (n, dict(prod_dict))
        n += 1
        products.append(prod_tuple)
    else:
        break
for e in products:
    print(e)
name = set()
price = set()
qua = set()
uni = set()
analytics = {'название': name, 'цена': price, 'количество': qua, 'ед.': uni}
for j in analytics.keys():
    for el in products:
        for i in el:
            if type(i) == dict:
                for k in i.keys():
                    if k == j:
                        analytics.get(j).add(i.get(k))
for keys, values in analytics.items():
    print(keys, values)
