"""
Homework Assignment #5: Basic Loops

This program is called "Fizz Buzz", which is one of the classic programming challenges.

This program prints the numbers from 1 to 100. But for multiples of three it will print 
"Fizz" instead of the number and for multiples of five it will print "Buzz". For numbers 
which are multiples of both three and five it will print "Buzz". Also, the program prints 
"Prime" if it encounters a number that is prime (divisibe only by itself and one).
"""

def fuzzBuzz():
    for x in range(1,101):
        if (((x % 3) == 0) and ((x % 5) == 0)):
            print("FizzBuzz")
        elif ((x % 3) == 0):
            print("Fizz")
        elif ((x % 5) == 0):
            print("Buzz")
        else:
            print(isPrime(x))

# Function for checking if the number is prime or not
def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return num
        else:
            return "Prime"
    else:
        return num

fuzzBuzz()
