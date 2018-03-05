#!/usr/bin/python
'''task2'''
# pylint: disable= invalid-name
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
s = []


def list_i(list1, list2):
    '''task2'''
    x = [i for i in list1 if i in list2]
    for i in x:
        if i not in s:
            s.append(i)
    return s


print(list_i(a, b))
