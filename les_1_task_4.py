n = int(input('введите число: '))
max = n % 10
while n != 0:
    n = n // 10
    if max < n % 10:
        max = n % 10
print (max)
