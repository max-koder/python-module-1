user, password = input(), input()
if user != "user123":
    print("Пользователь не найден.")
elif user == "user123" and password != "pass123":
    print("Неверный пароль.")
else:
    print("Вход выполнен успешно!")