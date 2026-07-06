###############################################################################
# Program Name: World Series Winners Counter
#
# Purpose:
#     This program allows the user to enter the name of an MLB baseball team
#     and displays the number of times that team won the World Series from
#     1903 through 2024. The program reads team names from a file and counts
#     how many times the selected team appears in the list.
#
# Author: Addison Flynn
#
# Date: 3/26/2026
#
# Version: 1.0
#
###############################################################################
def main():
    try:
        # Open the file
        INFILE = open("WorldSeriesWinners.txt", "r")
        # Read the file into a list
        WINNERS_LIST = INFILE.readlines()
        # Close the file
        INFILE.close()
        # Ask the user for a team name
        TEAM_NAME = input("Enter the name of an MLB team: ")
        # Create a counter variable
        WIN_COUNT = 0
        # Step through the list and count matches
        for INDEX in range(len(WINNERS_LIST)):
            WINNERS_LIST[INDEX] = WINNERS_LIST[INDEX].rstrip('\n')
            if WINNERS_LIST[INDEX] == TEAM_NAME:
                WIN_COUNT += 1
        # Display the result
        print()
        print(TEAM_NAME, "won the World Series", WIN_COUNT, "times from 1903 through 2024.")
    except FileNotFoundError:
        print("The file WorldSeriesWinners.txt was not found.")
    except IndexError:
        print("An index error occurred while processing the list.")
# Call the main function
main()
