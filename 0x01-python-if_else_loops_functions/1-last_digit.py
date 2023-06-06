#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit=abs(number)%10
str = f"Last digit of {number} is"
if number < 0:
    last_digit*=-1
if last_digit > 5 :
    str=str+ f' {last_digit} and is greater than 5'
elif last_digit == 0 :
    str=str+ f' {last_digit} and is 0'
else:
    str=str+ f' {last_digit} and is less than 6 and not 0'
print(str)
