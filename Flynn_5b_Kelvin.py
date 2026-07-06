###############################################################################
# Program Name: Temperature Conversion Application
#
# Purpose:
#     This program allows the user to convert temperatures between
#     Fahrenheit, Celsius, and Kelvin using a menu-based interface.
#     The program continues running until the user enters the
#     sentinel value 'X' to exit.
#
# Author: Addison Flynn
#
# Date: [Enter Submission Date]
#
# Version: 1.2
#
###############################################################################

# ==============================
# Global Constants
# ==============================
FAHRENHEIT_OFFSET = 32
CELSIUS_MULTIPLIER = 1.8
FRACTION_NUMERATOR = 5
FRACTION_DENOMINATOR = 9
KELVIN_OFFSET = 273.15          # Added: offset between Celsius and Kelvin
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
# Function: Celsius to Kelvin      <-- NEW
# ==============================
def celsius_to_kelvin(celsius):
    return celsius + KELVIN_OFFSET


# ==============================
# Function: Kelvin to Celsius      <-- NEW
# ==============================
def kelvin_to_celsius(kelvin):
    return kelvin - KELVIN_OFFSET


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
        print("3. Convert Celsius to Kelvin")      # Added
        print("4. Convert Kelvin to Celsius")      # Added
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

        elif choice == "3":                                         # Added
            temp = float(input("Enter temperature in Celsius: "))
            converted = celsius_to_kelvin(temp)
            print(f"{temp:.2f}°C is {converted:.2f}K")

        elif choice == "4":                                         # Added
            temp = float(input("Enter temperature in Kelvin: "))
            if temp < 0:                                            # Added: Kelvin can't be negative
                print("Error: Kelvin cannot be negative.")
            else:
                converted = kelvin_to_celsius(temp)
                print(f"{temp:.2f}K is {converted:.2f}°C")

        elif choice == EXIT_OPTION:
            print("Exiting program...")

        else:
            print("Invalid selection. Please try again.")


# Run program
main()
