def even_or_odd(number: int) -> str:
    """
    Determines whether a given integer is even or odd.

    Args:
        number (int): The integer to evaluate.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return "Even" if number % 2 == 0 else "Odd"
