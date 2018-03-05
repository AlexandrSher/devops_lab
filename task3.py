#!/usr/bin/python
'''task3'''
# pylint: disable= invalid-name
N = int(input())
d = []
for i in range(9, 1, -1):
    while N % i == 0:
        d.append(i)
        N = N / i
if len(d) == 0:
    print('-1')
else:
    print(''.join(map(str, d[::-1])))
