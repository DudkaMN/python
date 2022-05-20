my_list = list(input('введите список через ,:').split(', '))
ind = 0
while ind <= len(my_list):
    if ind % 2 == 0:
        el = my_list.pop(ind)
        my_list.insert(ind + 1, el)
    ind += 1
print(my_list)
