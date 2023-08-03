#!/usr/bin/env python3


'''Annotating function parameters and returns values and their types'''

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Annotating the function parameters'''
    return [(i, len(i)) for i in lst]


if __name__ == '__main__':
    print(element_length.__annotations__)
