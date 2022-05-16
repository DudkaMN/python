time = int(input("введите время в секундах: "))
s = time % 60
m = (time // 60) % 60
h = time // 3600
print (f"{h:02d}:{m:02d}:{s:02d}")
