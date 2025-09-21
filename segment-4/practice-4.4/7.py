import math
weight, country = float(input()), input()

if country == "Россия":
    print(500)
else:
    if weight == 1.0:
        print(1000)
    else:
        print(1000 + (math.ceil(weight) - 1) * 500)