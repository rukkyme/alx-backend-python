#!/usr/bin/env python3

'''This returns summation of two float numbers'''


def add(a: float, b: float) -> float:
    return a + b


if __name__ == '__main__':

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
