a, b, c = int(input()), int(input()), int(input())

s = [a, b, c]
if max(s) <= 15:
    print("Коробка №1")
elif max(s) > 200:
    print("Упаковка для лыж")
elif max(s) > 15 and max(s) < 50:
    print("Коробка №2")
else:
    print("Коробка №3")