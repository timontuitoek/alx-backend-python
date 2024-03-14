#!/usr/bin/env python3
"""Define and annotate variables."""


# Annotate variable 'a' as an integer with a value of 1
a: int = 1

# Annotate variable 'pi' as a float with a value of 3.14
pi: float = 3.14

# Annotate variable 'i_understand_annotations' as a boolean with value of True
i_understand_annotations: bool = True

# Annotate variable 'school' as a string with a value of "Holberton"
school: str = "Holberton"


def to_str(n: float) -> str:
    """
    Returns the string representation of the given float.
    """
    return str(n)
