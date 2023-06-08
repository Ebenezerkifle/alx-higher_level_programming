#!/usr/bin/python3
"""if is used to block the execusion with import."""
if __name__ == "__main__":
    import sys
    list = sys.argv
    count = len(list)
    arg = ''
    if(count == 1):
        arg = 'argument:'
    elif count == 0:
        arg = 'arguments.'
    else:
        arg = 'arguments:'

    print('{} {}'.format(count, arg))

    for i in range(count):
        print('{}: {}'.format(i+1, list[i]))
