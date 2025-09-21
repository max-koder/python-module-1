year = int(input())

if year % 4 == 0:
    print("Високосный год")
elif year % 100 == 0 and year % 400 != 0:
    print("Обычный год")
else:
    print("Обычный год")
