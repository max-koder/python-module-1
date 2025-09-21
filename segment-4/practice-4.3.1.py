a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print("Равносторонний")
elif (a == b and a != c and b != c) or (a == c and a != b and c != b) or (b == c and a != b and a != c):
    print("Равнобедренный")
else:
    print("Разносторонний")