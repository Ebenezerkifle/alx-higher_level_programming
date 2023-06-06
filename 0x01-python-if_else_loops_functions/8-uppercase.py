#!/usr/bin/python3

#ASCII 
# A - Z =======> 65 - 90
# a - z =======> 97 - 122
# 97 - 65 = 32 -- the difference

def uppercase(str):
    for index in range(0, len(str)):
        if ord(str[index]) >= 97 and ord(str[index]) <= 122:
            print('{}'.format(chr(ord(str[index]) - 32)), end='')
        else:
            print('{}'.format(str[index]), end='')
