import pytest

from app import Figure


# --- fixtures ---
@pytest.fixture
def square():
    return Figure("квадрат", 5)


@pytest.fixture
def figure_10():
    """Фігура з довжиною 10."""
    return Figure("квадрат", 10)


@pytest.fixture(scope="module")
def allowed_figures():
    """Одна й та сама fixture на весь модуль."""
    return Figure.FIGURES


# --- основи (з маркером unit) ---
@pytest.mark.unit
def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"


@pytest.mark.unit
def test_square_length(square):
    assert square.get_figure_length() == 5


def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


# --- параметризація ---
@pytest.mark.parametrize("figure", Figure.FIGURES)
def test_allowed_figure(figure):
    assert Figure(figure, 1).type == figure


# --- fixture з довжиною 10 ---
def test_figure_10_length(figure_10):
    assert figure_10.get_figure_length() == 10


def test_figure_10_type(figure_10):
    assert figure_10.get_figure_type() == "квадрат"


# --- fixture зі scope="module" у двох тестах ---
def test_allowed_figures_count(allowed_figures):
    assert len(allowed_figures) == 3


def test_allowed_figures_content(allowed_figures):
    assert "квадрат" in allowed_figures


# --- неправильні типи та довжини ---
@pytest.mark.parametrize("bad_type", ["коло", "", "Квадрат", None, 5])
def test_invalid_type(bad_type):
    with pytest.raises(AssertionError):
        Figure(bad_type, 3)


@pytest.mark.parametrize("bad_length", [0, -1, -0.5, "5", None, True])
def test_invalid_length_values(bad_length):
    with pytest.raises(AssertionError):
        Figure("квадрат", bad_length)
