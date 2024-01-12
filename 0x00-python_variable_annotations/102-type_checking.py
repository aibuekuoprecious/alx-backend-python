#!/usr/bin/env python3
""" Type Checking  """
from typing import Tuple, Union, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Zoom Array """
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

# If you want to allow for a float as a factor, change the annotation to factor: Union[int, float]
zoom_3x = zoom_array(array, int(3.0))
