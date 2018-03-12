#!/usr/bin/python
'''task2'''
# pylint: disable= invalid-name
print('Add first list:')
a = input().split()
print('Add second list:')
b = input().split()
s = []


def list_i(list1, list2):
    '''task2'''
    x = [i for i in list1 if i in list2]
    for i in x:
        if i not in s:
            s.append(i)
    return s


print(list_i(a, b))
