import unittest
from typing import Any, List

from src.number_classifier import NumberClassifier


class TestNumberClassifier(unittest.TestCase):
    """
    Unit tests for the NumberClassifier class.
    This class checks classification of even and odd numbers,
    as well as validation of input types.
    """

    def setUp(self) -> None:
        """Set up a fresh NumberClassifier instance before each test."""
        self.classifier = NumberClassifier()

    def test_getter_returns_correct_value(self) -> None:
        """Test that the getter returns the correct value."""
        self.classifier.number = 42
        self.assertEqual(self.classifier.number, 42)

    def test_setter_updates_value(self) -> None:
        """Test that the setter correctly updates the value."""
        self.classifier.number = 100
        self.assertEqual(self.classifier.number, 100)

    def test_classify_raises_value_error_if_number_is_none(self) -> None:
        with self.assertRaises(ValueError):
            self.classifier.classify()

    def test_setter_raises_type_error_for_invalid_input(self) -> None:
        """Test that the setter raises TypeError for invalid input types."""
        invalid_inputs: List[Any] = ["string", 3.14, [1], {"num": 1}]
        for value in invalid_inputs:
            with self.subTest(input_value=value):
                with self.assertRaises(TypeError):
                    self.classifier.number = value

    def test_even_numbers(self) -> None:
        """Test that even numbers return 'Even'."""
        even_values: List[int] = [-2, 0, 2, 10**6]
        for value in even_values:
            with self.subTest(input_value=value):
                self.classifier.number = value
                self.assertEqual(self.classifier.classify(), "Even")

    def test_odd_numbers(self) -> None:
        """Test that odd numbers return 'Odd'."""
        odd_values: List[int] = [-1, 1, 99, 10**6 + 1]
        for value in odd_values:
            with self.subTest(input_value=value):
                self.classifier.number = value
                self.assertEqual(self.classifier.classify(), "Odd")

    def test_repr_output(self) -> None:
        self.classifier.number = 7
        expected = "NumberClassifier(number=7, classification='Odd')"
        self.assertEqual(repr(self.classifier), expected)
