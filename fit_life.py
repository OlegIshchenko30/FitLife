# Проект FitLife - MVP версия 1.0


MILLILITERS_IN_LITER = 1000
DAILY_WATER_NEEDED_PER_KG_IN_MILLILITERS = 30

DAILY_WATER_NEEDED_PER_KG_IN_LITERS = (
    DAILY_WATER_NEEDED_PER_KG_IN_MILLILITERS / MILLILITERS_IN_LITER
)


def collect_user_name():
    """Collect user's name"""
    return input(
        "Приветствую вас в проекте FitLife! "
        "Для начала напишите как вас зовут."
    )


def collect_user_age():
    """Collect user's age."""
    while True:
        user_age = input(
            "Сколько вам лет?"
        )

        try:
            user_age = int(user_age)
        except ValueError:
            print(
                "Произошла ошибка.\n"
                "Убедитесь что вводите целое число.\n"
                "Например: 25",
            )
            continue

        if user_age <= 0:
            print(
                "Ваш возраст должен быть больше чем 0.",
            )
            continue

        break

    return user_age


def collect_user_weight():
    """Collect user's weight."""
    while True:
        user_weight = input(
            "Какой ваш вес в кг?\n"
            "Например: 70"
        )

        try:
            user_weight = float(user_weight)
        except ValueError:
            print(
                "Произошла ошибка.\n"
                "Убедитесь что ввели либо целое число, "
                "либо дробное через точку.\n"
                "Например: 70 или 70.5.",
            )
            continue

        if user_weight <= 0:
            print(
                "Убедитесь что вводите вес больше 0 кг.",
            )
            continue

        break

    return user_weight


def collect_user_height():
    """Collect user's height."""
    while True:
        user_height = input(
            "Какой ваш рост в метрах?\n"
            "Например: 1.75"
        )

        try:
            user_height = float(user_height)
        except ValueError:
            print(
                "Произошла ошибка.\n"
                "Убедитесь что ввели дробное число через точку.\n"
                "Например: 1.75.",
            )
            continue

        if user_height <= 0:
            print(
                "Убедитесь что вводите рост выше 0 метров.",
            )
            continue

        break

    return user_height


def calculate_bmi(user_weight, user_height):
    """Return the body mass index formula rounded to one decimal."""
    bmi = user_weight / user_height**2
    return round(bmi, 1)


def calculate_daily_water_needed_in_liters(user_weight):
    """Return daily water recommendation."""
    water_needed = (user_weight * DAILY_WATER_NEEDED_PER_KG_IN_LITERS)
    return round(water_needed, 2)


def main():
    """Main scenario"""
    user_name = collect_user_name()
    user_age = collect_user_age()
    user_weight = collect_user_weight()
    user_height = collect_user_height()

    bmi = calculate_bmi(user_weight, user_height)
    water_needed = calculate_daily_water_needed_in_liters(user_weight)

    result_message = (
        f"{user_name}, можете ознакомиться с результатами!\n\n"
        f"- Ваш возраст: {user_age} года\n"
        f"- Индекс Массы Тела (ИМТ): {bmi}\n"
        f"- Рекомендуемая дневная норма воды: {water_needed} литра.\n\n"
        "Расчет окончен. Будьте здоровы!"
    )

    print(f"{result_message}")


if __name__ == "__main__":
    main()
