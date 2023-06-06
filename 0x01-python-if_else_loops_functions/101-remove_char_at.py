#!/usr/bin/python3
def remove_char_at(str, n):
    result = ''
    for index in range(0, len(str)):
        if n != index:
            result += str[index]
    return result
