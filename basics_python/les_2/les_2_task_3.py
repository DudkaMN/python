month = int(input('введите номер месяца 1-12: '))
# решение dict
season = {1: 'winter', 2: 'winter', 12: 'winter', 3 : 'spring', 4 : 'spring', 5 : 'spring', 6 : 'summer',7 : 'summer',8 : 'summer', 9 : 'autumn', 10 : 'autumn', 11 : 'autumn'}
print(season.get(month))
# решение list
season_list = ['winter','spring','summer','autumn']
if 3 <= month <= 5:
    print(season_list[1])
elif 6 <= month <= 8:
    print(season_list[2])
elif 9 <= month <= 11:
    print(season_list[3])
else:
    print(season_list[0])
