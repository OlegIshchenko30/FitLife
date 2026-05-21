# Проект FitLife - MVP версия 1.0

# 0. Константы

MILLILITERS_IN_LITER = 1000
DAILY_WATER_NEEDED_PER_KG_IN_MILLILITERS = 30

DAILY_WATER_NEEDED_PER_KG_IN_LITERS = (
    DAILY_WATER_NEEDED_PER_KG_IN_MILLILITERS / MILLILITERS_IN_LITER
)

# 1. Знакомство

# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input(
    "Приветствую тебя в проекте FitLife! "
    "Для начала напиши как тебя зовут."
)

# TODO: Спроси возраст и сохрани в переменную user_age
# (не забудь преобразовать в число)
user_age = int(input(
    "Сколько тебе лет?"
))

# 2. Сбор данных

# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
user_weight = float(input(
    "Какой твой вес в кг? (Например 70)"
))

# TODO: Запроси рост (в метрах, например 1.75)
#  и сохрани в user_height (тип float)
user_height = float(input(
    "Какой твой рост в метрах? (Например 1.75)"
))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)

# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)


def calculate_bmi(user_weight, user_height):
    """Return the body mass index formula rounded to one decimal."""
    bmi = user_weight / user_height**2
    return round(bmi, 1)


bmi = calculate_bmi(user_weight, user_height)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed


def calculate_daily_water_needed_in_liters(user_weight):
    """Return daily water recommendation."""
    water_needed = (user_weight * DAILY_WATER_NEEDED_PER_KG_IN_LITERS)
    return round(water_needed, 2)


water_needed = calculate_daily_water_needed_in_liters(user_weight)

# 4. Вывод красивого результата

# TODO: Используй f-строку, чтобы вывести приветствие,
#  например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
result_message = (
    f"{user_name}, можете ознакомиться с результатами!\n\n"
    f"- Ваш возраст: {user_age} года\n"
    f"- Индекс Массы Тела (ИМТ): {bmi}\n"
    f"- Рекомендуемая дневная норма воды: {water_needed} литра.\n\n"
    "Расчет окончен. Будьте здоровы!"
)

print(result_message)
print()