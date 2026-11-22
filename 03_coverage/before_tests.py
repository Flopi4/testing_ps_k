"""Початковий набір тестів (для порівняння "до"). Запускається вручну."""
import pytest

from app import Figure


def test_triangle_angles():
    assert Figure("трикутник", 3).get_angles() == [60, 60, 60]


def test_getters():
    figure = Figure("квадрат", 5)
    assert figure.get_figure_type() == "квадрат"
    assert figure.get_figure_length() == 5


def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)
