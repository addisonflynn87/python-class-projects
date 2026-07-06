###############################################################################
# Program Name: Pig Latin Translator                                          #
#                                                                             #
# Purpose:                                                                    #
#     This program allows the user to translate a sentence either from        #
#     English to Pig Latin or from Pig Latin to English. The program uses a   #
#     menu-driven interface and processes each word in the sentence           #
#     individually. Punctuation is preserved during translation.              #
#                                                                             #
# Author: Addison Flynn                                                       #
#                                                                             #
# Date: 4/11/2026                                                             #
#                                                                             #
# Version: 2.3                                                                #
#                                                                             #
###############################################################################
 
# Constants
VOWELS      = ('a', 'e', 'i', 'o', 'u')
C_SUFFIX    = 'ay'
V_SUFFIX    = 'yay'
PUNCTUATION = ['.', '?', '!']
EXIT_OPTION = 'X'
 
 
# Main menu-driven program
def main():
 
    print('Welcome to the piglatin translator.')
 
    displayMenu()
 
    # Priming read
    OPTION = input('Enter the option for translation.')
 
    while OPTION.upper() != EXIT_OPTION:
 
        if OPTION.upper() == 'P':
            translate2Piglatin()
        elif OPTION.upper() == 'E':
            translate2English()
        else:
            print('ERROR: Invalid option.')
 
        displayMenu()
 
        # Modifying statement
        OPTION = input('Enter the option for translation.')
 
    print('Thank you for using the piglatin translator.')
    exit()
 
 
# Function to translate English to Pig Latin
def translate2Piglatin():
 
    print('You selected to translate a phrase from English to piglatin.')
 
    PHRASE = getPhrase()
 
    # Boolean flag
    HAS_PUNCTUATION = False
 
    # Create empty list to capture translated words
    TRANSLATED = []
 
    # Examine for punctuation, and save for later
    if PHRASE[-1] in PUNCTUATION:
        PUNCTUATION_MARK = PHRASE[-1]
 
        # Setting the flag for a phrase with punctuation
        HAS_PUNCTUATION = True
 
        # Modify the phrase to remove punctuation during translation
        PHRASE = PHRASE[ : -1]
 
    # Split phrase into a list of words
    WORDS = PHRASE.split()
 
    # Determine if the word starts with a vowel
    for WORD in WORDS:
 
        # If the word starts with a vowel, append 'yay' suffix to the word
        if WORD[0].lower() in VOWELS:
            WORD = WORD + V_SUFFIX
        else:
            # If the word starts with a consonant, move the first letter and add 'ay'
            FIRST = WORD[0].lower()
            WORD  = WORD[1: ] + FIRST + C_SUFFIX
 
        TRANSLATED.append(WORD)
 
    # Use the join method to re-create the phrase from the list
    PIGLATIN = ' '.join(TRANSLATED)
 
    # Display the translated phrase
    if HAS_PUNCTUATION:
        PIGLATIN += PUNCTUATION_MARK
 
    print(PIGLATIN)
 
 
# Function to translate Pig Latin to English
def translate2English():
 
    print('You selected to translate a phrase from piglatin to English.')
 
    PHRASE = getPhrase()
 
    # Boolean flag
    HAS_PUNCTUATION = False
 
    # Create empty list to capture translated words
    TRANSLATED = []
 
    # Examine for punctuation, and save for later
    if PHRASE[-1] in PUNCTUATION:
        PUNCTUATION_MARK = PHRASE[-1]
 
        # Setting the flag for a phrase with punctuation
        HAS_PUNCTUATION = True
 
        # Modify the phrase to remove punctuation during translation
        PHRASE = PHRASE[ : -1]
 
    # Split phrase into a list of words
    WORDS = PHRASE.split()
 
    # Determine translation rule based on suffix
    for WORD in WORDS:
 
        # If word ends with 'yay', it originally started with a vowel
        if WORD.endswith(V_SUFFIX):
            WORD = WORD[ : -len(V_SUFFIX)]
        else:
            # Remove 'ay' and move the consonant back to the front
            WORD  = WORD[ : -len(C_SUFFIX)]
            WORD  = WORD[-1] + WORD[ : -1]
 
        TRANSLATED.append(WORD)
 
    # Use the join method to re-create the phrase from the list
    ENGLISH = ' '.join(TRANSLATED)
 
    # Display the translated phrase
    if HAS_PUNCTUATION:
        ENGLISH += PUNCTUATION_MARK
 
    print(ENGLISH)
 
 
# Function to get a phrase from the user
def getPhrase():
 
    PHRASE = input('Enter a phrase to be translated.')
 
    return PHRASE
 
 
# Function to display the menu
def displayMenu():
 
    print('\nEnter P to translate from English to piglatin.')
    print('Enter E to translate from piglatin to English.')
    print('Enter X to exit.\n')
 
 
if __name__ == '__main__':
    main()
