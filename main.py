from external_requests import get_ip
from external_colorama import color_text
from external_pyfiglet import make_banner
from external_rich import rich_message
from external_faker import create_person
from external_art import make_art
from external_termcolor import terminal_text
from external_emoji import add_emoji
from external_cowsay import cow_message
from external_qrcode import create_qr

from builtin_math import calculate_square_root
from builtin_random import random_number
from builtin_datetime import current_date
from builtin_os import current_folder
from builtin_statistics import calculate_average


def main():
    print(make_banner("LAB 4"))

    print("Мій IP:", get_ip())

    print(color_text("Це текст з Colorama"))

    rich_message("Це повідомлення Rich")

    print("Випадкове число:", random_number())

    print("Квадратний корінь:", calculate_square_root(25))

    print("Дата:", current_date())

    print("Папка:", current_folder())

    print("Середнє:", calculate_average([10, 20, 30, 40]))

    person = create_person()
    print("Ім'я:", person["name"])
    print("Email:", person["email"])

    print(make_art("Python"))

    print(terminal_text("Termcolor працює"))

    print(add_emoji("Python :rocket:"))

    print(cow_message("Привіт!"))

    print(create_qr("https://github.com"))


if __name__ == "__main__":
    main()