################################################################################
#   Purpose:  Calculate the total price of produce purchased.
#
#   Author: Addison Flynn
#
#   Date Written: 1/30/2026
#
#   Version: 3.14.3
#
################################################################################

from datetime import datetime as dt

# =========================
# Constants
# =========================
APPLE_PRICE = 0.75
PEAR_PRICE = 0.65
PEACH_PRICE = 0.85
TAX_RATE = 0.0825

STORE_NAME = "Addison's Fruit Stand"
BORDER = "+"
BORDER_WIDTH = 60

# =========================
# Date & Time
# =========================
timestamp = dt.now()
formatted_date = timestamp.strftime("%m/%d/%Y %H:%M:%S")

# =========================
# User Input
# =========================
APPLES = float(input("Enter pounds of apples purchased: "))
PEARS = float(input("Enter pounds of pears purchased: "))
PEACHES = float(input("Enter pounds of peaches purchased: "))

# =========================
# Calculations
# =========================
APPLE_TOTAL = APPLES * APPLE_PRICE
PEAR_TOTAL = PEARS * PEAR_PRICE
PEACH_TOTAL = PEACHES * PEACH_PRICE

SUBTOTAL = APPLE_TOTAL + PEAR_TOTAL + PEACH_TOTAL
TAX = SUBTOTAL * TAX_RATE
GRAND_TOTAL = SUBTOTAL + TAX

# =========================
# Receipt Output
# =========================
print()
print(BORDER * BORDER_WIDTH)
print(STORE_NAME.center(BORDER_WIDTH))
print(formatted_date.center(BORDER_WIDTH))
print(BORDER * BORDER_WIDTH)

print(f"{'Apples subtotal:':<25} ${APPLE_TOTAL:>8.2f}")
print(f"{'Pears subtotal:':<25} ${PEAR_TOTAL:>8.2f}")
print(f"{'Peaches subtotal:':<25} ${PEACH_TOTAL:>8.2f}")

print("-" * BORDER_WIDTH)
print(f"{'Total before tax:':<25} ${SUBTOTAL:>8.2f}")
print(f"{'Sales tax:':<25} ${TAX:>8.2f}")
print(f"{'Grand total:':<25} ${GRAND_TOTAL:>8.2f}")

print(BORDER * BORDER_WIDTH)
