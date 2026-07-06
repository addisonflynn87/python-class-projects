################################################################################
# Program Name: Primary Color Mixer
#
# Purpose:
#   This program prompts the user to enter two primary colors and determines
#   the resulting secondary color when the two are mixed.
#
# Author: Addison Flynn
#
# Date Written: 1/29/2026
#
# Version: 1.1
#
################################################################################

# -----------------------------
# Welcome Message
# -----------------------------
print("\nWelcome to the Color Mixture Program.\n")

# -----------------------------
# Input Section
# -----------------------------
# Ask the user to enter two colors. Convert input to lowercase so the program
# will work correctly regardless of how the user capitalizes their input.

COLOR1 = input("Enter the first primary color: \n").lower()
COLOR2 = input("Enter the second primary color: \n").lower()

# -----------------------------
# Processing Section
# -----------------------------
# Determine whether the inputs are valid primary colors and identify the
# resulting secondary color.

if (COLOR1 == "red" and COLOR2 == "blue") or (COLOR1 == "blue" and COLOR2 == "red"):
    RESULT = "purple"
elif (COLOR1 == "red" and COLOR2 == "yellow") or (COLOR1 == "yellow" and COLOR2 == "red"):
    RESULT = "orange"
elif (COLOR1 == "blue" and COLOR2 == "yellow") or (COLOR1 == "yellow" and COLOR2 == "blue"):
    RESULT = "green"
else:
    RESULT = None

# -----------------------------
# Output Section
# -----------------------------
# Display the result. If the colors were invalid, show an error message.
# Otherwise, display the correct mixing statement.

if RESULT is None:
    print("You didn't input two primary colors.\n")
else:
    print(f"When you mix {COLOR1} and {COLOR2}, you get {RESULT}.\n")

# -----------------------------
# Goodbye Message
# -----------------------------
print("Thank you for using the Color Mixture Program.")
