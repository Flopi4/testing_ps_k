import unittest

from app import Figure


class TestFigure(unittest.TestCase):
    def test_getters(self):
        figure = Figure("квадрат", 5)
        self.assertEqual(figure.get_figure_type(), "квадрат")
        self.assertEqual(figure.get_figure_length(), 5)

    def test_angles_square(self):
        self.assertEqual(Figure("квадрат", 3).get_angles(), [90, 90, 90, 90])

    def test_angles_rectangle(self):
        self.assertEqual(Figure("прямокутник", 3).get_angles(), [90, 90, 90, 90])

    def test_angles_triangle(self):
        self.assertEqual(Figure("трикутник", 3).get_angles(), [60, 60, 60])

    def test_invalid_type(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 3)

    def test_invalid_length(self):
        for bad in [0, -1, "5", None, True]:
            with self.subTest(bad=bad):
                with self.assertRaises(AssertionError):
                    Figure("квадрат", bad)


if __name__ == "__main__":
    unittest.main()
