###############################################################################
# Program Name: Course Information Directory                                  #
#                                                                             #
# Purpose:                                                                    #
#     This program creates dictionaries that store course numbers along with  #
#     their room numbers, instructors, and meeting times. The user enters a   #
#     course number, and the program displays the corresponding course        #
#     information. A sentinel value is used to exit the loop. Exception       #
#     handling is used to catch invalid course entries.                       #
#                                                                             #
# Author: Addison Flynn                                                       #
#                                                                             #
# Date: 4/14/2026                                                             #
#                                                                             #
# Version: 2.4                                                                #
#                                                                             #
###############################################################################
 
# Constants
COLLEGE_NAME = 'Austin Community College'
SENTINEL     = '9999'
DEFAULT      = 'Not Found'
 
 
def main():
 
    # Create the 3 dictionaries with the course number as key value
 
    # Room numbers
    COURSE_ROOMS = {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'NT110': '1244',
        'CM241': '1411'
    }
 
    # Instructors
    COURSE_INSTRUCTOR = {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee'
    }
 
    # Meeting times
    COURSE_MEETING_TIME = {
        'CS101': 'Monday 8:00 a.m',
        'CS102': 'Tuesday 9:00 a.m',
        'CS103': 'Monday 10:00 a.m',
        'NT110': 'Wednesday 11:00 a.m',
        'CM241': 'Thursday 1:00 p.m'
    }
 
    # Welcome message
    WELCOME = f'Welcome to {COLLEGE_NAME} Course Information System.'
    print(WELCOME)
 
    # Display available courses
    print('\nAvailable courses:')
    for COURSE in COURSE_ROOMS.keys():
        print(COURSE)
 
    # Prompt the user for the course number; priming read
    COURSE_NUM = getCourseNumber()
 
    # Use a while loop to iterate over course information
    while COURSE_NUM != SENTINEL:
        try:
            print(f'Course Number: {COURSE_NUM}')
            print(f'\tRoom Number:      {COURSE_ROOMS.get(COURSE_NUM, DEFAULT)}')
            print(f'\tInstructor Name:  {COURSE_INSTRUCTOR.get(COURSE_NUM, DEFAULT)}')
            print(f'\tMeeting Time:     {COURSE_MEETING_TIME.get(COURSE_NUM, DEFAULT)}\n')
        except KeyError:
            print('ERROR: Course not found.\n')
        except:
            print('ERROR: Something bad happened.\n')
        finally:
            # Modifying statement
            COURSE_NUM = getCourseNumber()
 
    GOODBYE = f'Thank you for visiting {COLLEGE_NAME} Course Information System.'
    print(GOODBYE)
 
 
def getCourseNumber():
 
    COURSE = input('\n\nEnter the course number: OR 9999 to exit.\n')
 
    return COURSE.upper()
 
 
if __name__ == '__main__':
    main()
