#!/usr/bin/python
'''task6'''
# pylint: disable= invalid-name
s = str(input())
w = ['+', '-', '*', '/']

for i in range(4):
    if s.find(w[i]) > 0:
        z = s.index(w[i])

try:
    equally = s.index('=')
    first = int(''.join(map(str, s[0:z:1])))
    second = int(''.join(map(str, s[z + 1:equally:1])))
    result = int(''.join(map(str, s[equally + 1::1])))
    if s[z] == '+':
        if first + second == result:
            print('yes')
        else:
            print('no')
    elif s[z] == '-':
        if first - second == result:
            print('yes')
        else:
            print('no')
    elif s[z] == '*':
        if first * second == result:
            print('yes')
        else:
            print('no')
    elif s[z] == '/':
        if first / second == result:
            print('yes')
        else:
            print('no')

except Exception:
    print('error')
