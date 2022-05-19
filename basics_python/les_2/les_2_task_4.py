text = input("введите текст: ")
for ind, el in enumerate(text.split(' ')):
    print(ind, el[:10])
