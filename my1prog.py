#!/usr/bin/python
import sys
num = 0
i=0
total=1
total2=1
total3=1
total4 =1
num = input()
while True:
        i = i + 1
        total3 = total2
        total2 = total4
        total = total2 + total3
        total4 = total
        if num == i:
                break
print total3
