###############################################################################
# Program Name: Average Calculator from File
#
# Purpose:
#     This program asks the user for a filename, reads integers from the file,
#     and calculates the average of all valid numbers in the file.
#
#     The program handles the following exceptions:
#     - IOError: Issues opening/reading the file
#     - FileNotFoundError: File does not exist
#     - ValueError: Non-numeric data in the file (skips invalid data)
#
# Author: Addison Flynn
#
# Date: 3/26/2026
#
# Version: 1.7
#
###############################################################################

def main():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename: ")

        # Open the file
        infile = open(filename, "r")

        total = 0
        count = 0

        # Read each line in the file
        for line in infile:
            line = line.rstrip('\n')

            try:
                number = int(line)
                total += number
                count += 1

            except ValueError:
                print("File must have only numbers. Try again.")
                # Continue reading remaining lines
                continue

        infile.close()

        # Calculate and display average
        if count > 0:
            average = total / count
            print("Average:", average)
        else:
            print("No valid numbers found in file.")

    except FileNotFoundError:
        print("File not found.")

    except IOError:
        print("Trouble opening file. Try again.")


# Call the main function
main()
