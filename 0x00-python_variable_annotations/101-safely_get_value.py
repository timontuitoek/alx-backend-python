from typing import Dict, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default:
                     Optional[T] = None) -> Optional[T]:
    """
    Returns the value associated with the given key in the dictionary safely.
    """
    if key in dct:
        return dct[key]
    else:
        return default
