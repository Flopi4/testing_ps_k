"""Клас Figure для завдань з pytest."""


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
