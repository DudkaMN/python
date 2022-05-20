def my_div(s_1, s_2):
    if s_2 == 0:
        print('второе число не должно быть равно 0')
    else:
        print(s_1 / s_2)


s_1 = int(input("введите первое число: "))
s_2 = int(input("введите второе число: "))
my_div(s_1, s_2)
