# Лабораторна робота №3
# Міні-магазин

products = [
    {"name": "Хліб", "price": 35.50, "quantity": 10},
    {"name": "Молоко", "price": 42.00, "quantity": 8},
    {"name": "Шоколад", "price": 55.75, "quantity": 15},
    {"name": "Сік", "price": 48.90, "quantity": 7},
    {"name": "Печиво", "price": 39.99, "quantity": 12}
]

cart = []

admin_login = "admin"
admin_password = "1234"


def show_catalog():
    print("\n--- КАТАЛОГ ТОВАРІВ ---")

    for i, product in enumerate(products, 1):
        print(
            f"{i}. {product['name']} - "
            f"{product['price']:.2f}грн. "
            f"Залишок: {product['quantity']}"
        )


def add_to_cart():
    show_catalog()

    number = int(input("\nВведіть номер товару: ")) - 1

    if 0 <= number < len(products):
        product = products[number]

        if product["quantity"] > 0:
            cart.append(product)
            product["quantity"] -= 1
            print(f"{product['name']} додано до кошика!")
        else:
            print("Товару немає в наявності.")
    else:
        print("Неправильний номер.")


def show_cart():
    print("\n--- КОШИК ---")

    if not cart:
        print("Кошик порожній.")
        return

    for i, product in enumerate(cart, 1):
        print(f"{i}. {product['name']} - {product['price']:.2f}грн.")

    total = sum(map(lambda product: product["price"], cart))

    print(f"Разом: {total:.2f}грн.")


def remove_from_cart():
    show_cart()

    if cart:
        number = int(input("\nВведіть номер товару для видалення: ")) - 1

        if 0 <= number < len(cart):
            product = cart.pop(number)
            product["quantity"] += 1
            print(f"{product['name']} видалено з кошика.")
        else:
            print("Неправильний номер.")


def buy_products():
    if not cart:
        print("\nКошик порожній.")
        return

    total = sum(map(lambda product: product["price"], cart))

    print(f"\nСума покупки: {total:.2f}грн.")
    answer = input("Підтвердити покупку? (так/ні): ")

    if answer.lower() == "так":
        cart.clear()
        print("Покупку успішно здійснено!")
    else:
        print("Покупку скасовано.")


def admin_panel():
    login = input("\nЛогін адміністратора: ")
    password = input("Пароль: ")

    if login == admin_login and password == admin_password:
        print("\n--- ПАНЕЛЬ АДМІНІСТРАТОРА ---")

        for product in products:
            print(
                f"{product['name']}: "
                f"{product['quantity']} шт. "
                f"по {product['price']:.2f}грн."
            )
    else:
        print("Неправильний логін або пароль.")


while True:
    print("\n===== МІНІ-МАГАЗИН =====")
    print("1. Переглянути каталог")
    print("2. Додати товар у кошик")
    print("3. Переглянути кошик")
    print("4. Видалити товар з кошика")
    print("5. Купити товари")
    print("6. Увійти як адміністратор")
    print("0. Вийти")

    choice = input("\nВаш вибір: ")

    if choice == "1":
        show_catalog()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        show_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        buy_products()

    elif choice == "6":
        admin_panel()

    elif choice == "0":
        print("До побачення!")
        break

    else:
        print("Невірний вибір.")