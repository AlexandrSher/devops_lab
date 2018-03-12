#!/usr/bin/python
'''task1'''
# pylint: disable= invalid-name
year = int(input())


def is_leap(yr):
    '''task1'''
    return yr % 4 != 0 or (yr % 400 != 0 and yr % 100 == 0)
   
print(is_leap(year))
