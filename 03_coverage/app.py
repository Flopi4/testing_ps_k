"""Клас Figure для завдань з покриття коду."""


class Figure:
    FIGURES = ("квадрат", "прямокутник", "трикутник")

    def __init__(self, figure_type, length):
        assert figure_type in self.FIGURES, f"Невідомий тип фігури: {figure_type}"
        assert (
            isinstance(length, (int, float))
            and not isinstance(length, bool)
            and length > 0
        ), "Довжина має бути додатним числом"
        self.type = figure_type
        self.length = length

    def get_figure_type(self):
        return self.type

    def get_figure_length(self):
        return self.length

    def get_angles(self):
        """Кути фігури (трикутник вважаємо рівностороннім)."""
        if self.type == "квадрат":
            return [90, 90, 90, 90]
        if self.type == "прямокутник":
            return [90, 90, 90, 90]
        return [60, 60, 60]


def main():
    figure = Figure("квадрат", 5)
    print(figure.get_figure_type(), figure.get_angles())


if __name__ == "__main__":  # pragma: no cover
    main()
