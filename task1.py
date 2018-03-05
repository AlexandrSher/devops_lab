#!/usr/bin/python
'''task1'''
# pylint: disable= invalid-name
year = int(input())


def is_leap(yr):
    '''task1'''
    leap = False
    if yr % 4 != 0 or (yr % 400 != 0 and yr % 100 == 0):
        leap = False
    else:
        leap = True

    return leap


print(is_leap(year))


if year % 4 != 0:
    print('no')
elif year % 100 == 0:
    if year % 400 == 0:
        print('yes')
    else:
        print('no')
else:
    print('yes')
