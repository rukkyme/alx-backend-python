#!/usr/bin/env python3


'''a module that takes a float as argument and returns a string'''


def to_str(n: float) -> str:
    return str(n)


if __name__ == '__main__':
    print(f'to_str(3.142)')
    print(to_str(0.00))

    print(to_str.__annotations__)