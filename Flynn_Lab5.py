###############################################################################
# Program Name: Prime Number Identifier
#
# Purpose:
#     This program defines a Boolean function named is_prime that determines
#     whether a given integer is a prime number. The program then prompts the
#     user for a starting and ending value and displays all prime numbers
#     within that range.
#
# Author: Addison Flynn
#
# Date: 2/24/2026
#
# Version: 0.3
#
###############################################################################

import math

# --------------------------------------------------
# Boolean function to determine if a number is prime
# --------------------------------------------------
def is_prime(NUMBER):
    # Numbers less than 2 are not prime
    if NUMBER < 2:
        return False

    # 2 and 3 are prime
    if NUMBER == 2 or NUMBER == 3:
        return True

    # Eliminate even numbers greater than 3
    if NUMBER % 2 == 0:
        return False

    # Check odd divisors from 3 to sqrt(NUMBER)
    for COUNTER in range(3, int(math.sqrt(NUMBER)) + 1, 2):
        RESULT = NUMBER % COUNTER
        print(
            "The index is: " + str(COUNTER) +
            " the number is " + str(NUMBER) +
            " and the resulting modulus is: " + str(RESULT)
        )

        if RESULT == 0:
            return False

    # If no divisors were found, the number is prime
    return True


# --------------------------------------------------
# Main program
# --------------------------------------------------
START = int(input("Enter the starting number: "))
END = int(input("Enter the ending number: "))

print("\nPrime numbers in the specified range:")

for NUMBER in range(START, END + 1):
    if is_prime(NUMBER):
        print(NUMBER)
