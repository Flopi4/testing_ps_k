"""Демонстрація: тест без assert збільшує покриття, але нічого не перевіряє."""
from app import Figure


def test_get_angles_without_assert():
    for figure_type in Figure.FIGURES:
        Figure(figure_type, 1).get_angles()  # результат ніде не перевіряється
