#!/usr/bin/env python3


'''A module that concatenates two strings'''


def concat(str1: str, str2: str) -> str:
    '''This function concatenates 2 strings together'''
    return str1 + str2


if __name__ == '__main__':

    str1 = 'sammy'
    str2 = 'kingx'

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
