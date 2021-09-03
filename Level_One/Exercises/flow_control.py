"""
Write a program which asks the user for a number. 
If number is even print ‘Even’, else print ‘Odd’.
"""

from typing import Coroutine


def checkNumber(number):
    if(number % 2 == 0):
        return 'Even'
    else:
        return 'Odd'

print('2 is a ', checkNumber(2), 'number')


"""Write a program to print counting from 1 to 10."""

def count_to_ten():
    for i in range(0, 10):
        print(i + 1)

print(count_to_ten())

"""Write a program which prints all the divisors of a number."""
# Divisors mean all the numbers that input number can divide into without a remainder.

def all_divisor(number):
    divisors = [1, number]

    for i in range(2, number):
        if(number % i == 0):
            divisors.append(i)
    return divisors

print(all_divisor(15))
