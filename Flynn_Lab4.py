################################################################################
# Program Name: Tuition Projection Program
#
# Purpose:Calculates tuition increases over the next 5 years
#   
# Author: Addison Flynn
#
# Date Written: 2/18/2026
#
# Version: 0.3
#
################################################################################

# Constants
BORDER = "+"
BORDER_WIDTH = 60
WGBORDER = "-"
WGBORDER_WIDTH = 60
INITIAL_TUITION = 8000.00
INCREASE_RATE = 0.03
YEARS = 5

# -----------------------------
# Welcome Message
# -----------------------------

print(WGBORDER * WGBORDER_WIDTH)
print("Welcome to the Tuition Projection Program.")
print(WGBORDER * WGBORDER_WIDTH)

# Display current tuition
print(BORDER * BORDER_WIDTH)
print(f"\nThe current tuition cost per semester is ${INITIAL_TUITION:,.2f}.\n")

# Variable to hold updated tuition
tuition = INITIAL_TUITION

# FOR loop to calculate tuition for the next 5 years
for year in range(1, YEARS + 1):
    tuition += tuition * INCREASE_RATE
    print(BORDER * BORDER_WIDTH)
    print(f"\nIn {year} year(s), the tuition per semester will be ${tuition:,.2f}.\n")
    
print(BORDER * BORDER_WIDTH)

# -----------------------------
# Goodbye Message
# -----------------------------

print(WGBORDER * WGBORDER_WIDTH)
print("Thank you for using the Tuition Projection Program.")
print(WGBORDER * WGBORDER_WIDTH)
