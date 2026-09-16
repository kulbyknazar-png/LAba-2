# Лабораторна робота №2
# Міні програма "Оцінки студентів"

users = {
    "Nazar": {
        "password": "1234",
        "grades": [10, 8, 12, 7, 4, 11]
    },
    "Ivan": {
        "password": "1111",
        "grades": [6, 9, 5, 3, 8, 10]
    },
    "Oleg": {
        "password": "2222",
        "grades": [12, 11, 10, 9, 8, 7]
    },
    "Andrii": {
        "password": "3333",
        "grades": [4, 3, 2, 8, 6, 10]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:

    grades = users[login]["grades"]

    print("\nВхід успішний!")
    print("Ваші оцінки:", grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if grade >= 5 and grade <= 12:
            satisfactory += 1
        elif grade >= 1 and grade <= 4:
            unsatisfactory += 1

    print("Кількість оцінок від 5 до 12:", satisfactory)
    print("Кількість оцінок від 1 до 4:", unsatisfactory)

else:
    print("\nНеправильний логін або пароль!")