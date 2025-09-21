date, month = int(input()), input()

if (month == "Декабрь" and 22 <= date <= 31) or (month == "Январь" and 1 <= date <= 19):
    print("Козерог")

elif (month == "Январь" and 20 <= date <= 31) or (month == "Февраль" and 1 <= date <= 18):
    print("Водолей")

elif (month == "Февраль" and 19 <= date <= 29) or (month == "Март" and 1 <= date <= 20):
    print("Рыбы")

elif (month == "Март" and 21 <= date <= 31) or (month == "Апрель" and 1 <= date <= 19):
    print("Овен")

elif (month == "Апрель" and 20 <= date <= 30) or (month == "Май" and 1 <= date <= 20):
    print("Телец")

elif (month == "Май" and 21 <= date <= 31) or (month == "Июнь" and 1 <= date <= 20):
    print("Близнецы")

elif (month == "Июнь" and 21 <= date <= 30) or (month == "Июль" and 1 <= date <= 22):
    print("Рак")

elif (month == "Июль" and 23 <= date <= 31) or (month == "Август" and 1 <= date <= 22):
    print("Лев")

elif (month == "Август" and 23 <= date <= 31) or (month == "Сентябрь" and 1 <= date <= 22):
    print("Дева")

elif (month == "Сентябрь" and 23 <= date <= 30) or (month == "Октябрь" and 1 <= date <= 22):
    print("Весы")

elif (month == "Октябрь" and 23 <= date <= 31) or (month == "Ноябрь" and 1 <= date <= 21):
    print("Скорпион")

else:
    print("Стрелец")