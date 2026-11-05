"""Функції та клас для завдань "Загальне тестування та юніт-тести"."""

VOWELS = "аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU"


# --- Перевірка даних (assert / raise ValueError) ---
def check_positive(number):
    """Перевірка введеного числа через assert."""
    assert number > 0, "Число має бути більшим за нуль!"
    return number


def create_name(name):
    if not name:
        raise ValueError("Ім'я не може бути порожнім")
    return name


def parse_positive_int(text):
    """Власна перевірка введення: рядок -> додатне ціле, інакше ValueError."""
    try:
        number = int(text)
    except (TypeError, ValueError):
        raise ValueError("Потрібно ввести ціле число")
    if number <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return number


# --- Тестування функцій ---
def count_symbols(text: str) -> int:
    return len(text)


def divide(a, b):
    return a / b


def count_vowels(text: str) -> int:
    """Кількість голосних літер (українські та латинські)."""
    return sum(1 for ch in text if ch in VOWELS)


# --- Клас Figure ---
class Figure:
    SIDES = {"квадрат": 4, "прямокутник": 4, "трикутник": 3}

    def __init__(self, figure_type, length):
        if figure_type not in self.SIDES:
            raise ValueError(f"Невідомий тип фігури: {figure_type}")
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Довжина має бути додатним числом")
        self._type = figure_type
        self._length = length

    def get_figure_type(self):
        return self._type

    def get_figure_length(self):
        return self._length

    def get_angles(self):
        """Кути фігури (трикутник вважаємо рівностороннім)."""
        if self._type == "трикутник":
            return [60, 60, 60]
        return [90, 90, 90, 90]


# --- Функція з input() ---
def ask_number():
    return parse_positive_int(input("Введіть число: "))
