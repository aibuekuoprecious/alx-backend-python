#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns arguments as a function that multiplies a float by multiplier """
    def inner_function(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return inner_function
