#!/usr/bin/python3
#5-text_indentation.py
#Abeniezer Kifle

"""A function that prints a text with 2 new lines after ., ? and :"""

def text_indentation(text):
    """text indenetation
    
    text: an input text
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for index in range(len(text)):
        if text[index] == '.' or text[index] == ':' or text[index] == '?':
            print(text[index], end='\n\n')
        elif index > 0 and (text[index - 1] == '.' or text[index - 1] == ':' or text[index - 1] == '?'):
            continue
        else: print(text[index], end='')
