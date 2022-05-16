revenue = int(input("введите выручку: "))
costs = int(input("введите издержки: "))
if revenue > costs:
    print(f"прибыль фирмы {revenue-costs}")
    print(f"рентабельность выручки составила {(revenue-costs)/revenue}")
    size = int(input("введите численность сотрудников компании: "))
    print(f"прибыль на каждого человека в компании равна {(revenue-costs)/size}")
elif revenue < costs:
    print(f"убыток фирмы {(costs - revenue)}")
else:
    print("работа фирмы не принесла прибыли")
