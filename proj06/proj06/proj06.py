# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
print ("Welcome to Hangman! Be ready to lose...")

listwrong=[]

print wordlist
chosenword=choose_word(wordlist)
print chosenword
guesses = 0

chosenletter= raw_input("Type in a letter please! And after 8 trials of defeat, you shall perish.")

for guesses in range(1,9):
    if chosenletter != chosenword:
        print guesses

for letters in chosenword:
    #print [""]
    if letters == chosenletter:
        print letters
    else:
        print [""]
    # for letters in chosenletter:
    #     if letters in chosenword:
    #         chosenword.append(letters)