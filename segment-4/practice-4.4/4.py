year = float(input())

if year < 0:
    print("Введен неверный возраст")
elif year > 2:
    print(round (21.0 + (year - 2) * 4, 1))
else:
    print(round(year * 10.5, 1))