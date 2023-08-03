#!/usr/bin/env python3


'''A module that returns a function'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    
    return lambda k: k * multiplier


if __name__ == '__main__':
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
