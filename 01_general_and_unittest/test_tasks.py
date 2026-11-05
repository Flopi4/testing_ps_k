import unittest
from unittest.mock import patch

from tasks import (Figure, ask_number, check_positive, count_symbols,
                   count_vowels, create_name, divide, parse_positive_int)


class TestChecks(unittest.TestCase):
    def test_check_positive_ok(self):
        self.assertEqual(check_positive(5), 5)

    def test_check_positive_fail(self):
        with self.assertRaises(AssertionError):
            check_positive(-1)

    def test_create_name(self):
        self.assertEqual(create_name("Іван"), "Іван")
        with self.assertRaises(ValueError):
            create_name("")

    def test_parse_positive_int(self):
        self.assertEqual(parse_positive_int("7"), 7)
        for bad in ["abc", "", "0", "-3"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parse_positive_int(bad)


class TestFunctions(unittest.TestCase):
    def test_count_symbols(self):
        self.assertEqual(count_symbols("abc"), 3)
        self.assertEqual(count_symbols(""), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_count_vowels_empty(self):
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_digits(self):
        self.assertEqual(count_vowels("12345"), 0)

    def test_count_vowels_ukrainian(self):
        self.assertEqual(count_vowels("Привіт"), 2)
        self.assertEqual(count_vowels("ЄЇІ"), 3)

    def test_count_vowels_latin_and_mixed(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("а1б2е3"), 2)


class TestFigure(unittest.TestCase):
    def setUp(self):  # виконується перед кожним тестом
        self.square = Figure("квадрат", 5)

    def test_properties(self):
        self.assertEqual(self.square.get_figure_type(), "квадрат")
        self.assertEqual(self.square.get_figure_length(), 5)

    def test_all_types_subtest(self):
        for name in ["квадрат", "прямокутник", "трикутник"]:
            for length in [1, 5, 10]:
                with self.subTest(figure=name, length=length):
                    self.assertEqual(Figure(name, length).get_figure_length(), length)

    def test_angles(self):
        self.assertEqual(Figure("квадрат", 2).get_angles(), [90] * 4)
        self.assertEqual(Figure("прямокутник", 2).get_angles(), [90] * 4)
        self.assertEqual(Figure("трикутник", 2).get_angles(), [60] * 3)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            Figure("квадрат", -4)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            Figure("коло", 3)


class TestInput(unittest.TestCase):
    @patch("builtins.input", return_value="5")
    def test_ask_number(self, mock_input):
        self.assertEqual(ask_number(), 5)
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="abc")
    def test_ask_number_invalid(self, mock_input):
        with self.assertRaises(ValueError):
            ask_number()


if __name__ == "__main__":
    unittest.main()
