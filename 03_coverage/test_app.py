import pytest

from app import Figure, main


def test_getters():
    figure = Figure("квадрат", 5)
    assert figure.get_figure_type() == "квадрат"
    assert figure.get_figure_length() == 5


@pytest.mark.parametrize(
    "figure_type, expected",
    [
        ("квадрат", [90, 90, 90, 90]),
        ("прямокутник", [90, 90, 90, 90]),
        ("трикутник", [60, 60, 60]),
    ],
)
def test_get_angles(figure_type, expected):
    assert Figure(figure_type, 3).get_angles() == expected


@pytest.mark.parametrize("bad_type", ["коло", "", None])
def test_invalid_type(bad_type):
    with pytest.raises(AssertionError):
        Figure(bad_type, 3)


@pytest.mark.parametrize("bad_length", [0, -1, "5", None, True])
def test_invalid_length(bad_length):
    with pytest.raises(AssertionError):
        Figure("квадрат", bad_length)


def test_main_output(capsys):
    main()
    out = capsys.readouterr().out
    assert "квадрат" in out
    assert "[90, 90, 90, 90]" in out
