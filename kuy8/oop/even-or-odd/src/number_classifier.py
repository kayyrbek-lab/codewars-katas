from typing import Optional


class NumberClassifier:
    """
    A class to classify an integer as either 'Even' or 'Odd'.

    Attributes:
        number (Optional[int]): The integer to classify. Can be None
        before initialization.
    """

    def __init__(self, number: Optional[int] = None) -> None:
        """
        Initializes the NumberClassifier with a given integer or None.

        Args:
            number (Optional[int]): The number to classify. Defaults to None
        """
        self._number: Optional[int] = None
        if number is not None:
            self.number = number

    @property
    def number(self) -> Optional[int]:
        """
        Gets the current number.

        Returns:
            Optional[int]: The current number or None.
        """
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        """
        Sets the number after validating that it is an integer.

        Args:
            value (int): The number to set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Input must be an integer.")
        self._number = value

    def classify(self) -> str:
        """
        Classifies the number as 'Even' or 'Odd'.

        Returns:
            str: 'Even' if the number is even, 'Odd' if odd.

        Raises:
            ValueError: If the number is None.
        """
        if self.number is None:
            raise ValueError("Number is not set.")
        return "Even" if self.number % 2 == 0 else "Odd"

    def __repr__(self) -> str:
        """
        Returns a string representation of the obfect.

        Returns:
            str: A string showing the number and its classification.
        """
        if self.number is None:
            return "NumberClassifier(number=None)"
        return (f"NumberClassifier(number={self.number}, "
                f"classification='{self.classify()}')")
