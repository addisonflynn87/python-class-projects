###############################################################################
# Program Name: Temperature Conversion Application
#
# Purpose:
#     This program allows the user to convert temperatures between
#     Fahrenheit and Celsius using a menu-based interface.
#     The program continues running until the user enters the
#     sentinel value 'X' to exit.
#
# Author: Addison Flynn
#
# Date: [Enter Submission Date]
#
# Version: 0.6
#
###############################################################################

# ==============================
# Global Constants
# ==============================
FAHRENHEIT_OFFSET = 32
CELSIUS_MULTIPLIER = 1.8
FRACTION_NUMERATOR = 5
FRACTION_DENOMINATOR = 9
EXIT_OPTION = "X"


# ==============================
# Function: Celsius to Fahrenheit
# ==============================
def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_MULTIPLIER + FAHRENHEIT_OFFSET


# ==============================
# Function: Fahrenheit to Celsius
# ==============================
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * \
           FRACTION_NUMERATOR / FRACTION_DENOMINATOR


# ==============================
# Main Program
# ==============================
def main():
    choice = ""

    while choice != EXIT_OPTION:

        print("\nTemperature Conversion Menu")
        print("----------------------------")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("X. Exit")

        choice = input("Enter your choice: ").upper()

        if choice == "1":
            temp = float(input("Enter temperature in Fahrenheit: "))
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp:.2f}°F is {converted:.2f}°C")

        elif choice == "2":
            temp = float(input("Enter temperature in Celsius: "))
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp:.2f}°C is {converted:.2f}°F")

        elif choice == EXIT_OPTION:
            print("Exiting program...")

        else:
            print("Invalid selection. Please try again.")


# Run program
main()
