#!/usr/bin/python3
def fizzbuzz():
    '''Prints the numbers from `1` to `100` followed by a space.
       For multiples of three, `Fizz` is printed instead of the number.
       For multiples of five, `Buzz` is printed instead of the number.
       For multiples of three and five, `FizzBuzz` is printed instead of the number.'''
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0 :
            print("FizzBuzz", end=" ")
        elif num % 3 == 0 :
            print("Fizz", end=" ")
        elif num % 5 == 0 :
            print("Buzz", end=" ")
        else :
            print("{}".format(num), end=" ")
