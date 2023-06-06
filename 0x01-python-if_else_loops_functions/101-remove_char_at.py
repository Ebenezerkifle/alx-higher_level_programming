#!/usr/bin/python3
def remove_char_at(str, n):
    newString = ''
    for index in range(0, len(str)):
        if n != index:
            newString += str[index]
    return newString
