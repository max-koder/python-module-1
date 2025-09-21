weight, height = int(input()), float(input())

bmi = weight / (height * height)

if bmi <= 18.5:
    print("Недостаточный вес")
elif 18.5 < bmi <= 24.9:
    print("Нормальный вес")
elif 24.9 < bmi <= 29.9:
    print("Избыточный вес")
else:
    print("Ожирение")