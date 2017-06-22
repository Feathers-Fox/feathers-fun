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

#print wordlist
chosenword=choose_word(wordlist)
print chosenword
guesses = 1

emptylist = []
for letters in chosenword:
    emptylist.append("_")
print emptylist

chosenletter = raw_input("Type in a letter please! And after 8 trials of defeat, you shall perish.")
print [chosenletter]

while guesses > 0:
    if chosenletter not in chosenword:
        print ("that is incorrect")
        guesses = guesses-1
        listwrong.append(chosenletter)
        print listwrong

if letters == chosenword:
    print "Correct, you are still terrible, but just keep trying... hahahaha!"

if chosenletter == chosenword:
    print ("You must have cheated to accomplish beating me, but u have won :(")


# for letters in chosenword:
#     if letters== chosenletter:
#         print letters


#         while chosenword < chosenletter:
#
#             print fools_game
# for guesses in range(1,9):
#     if chosenletter > chosenword:
#         print True
#
#     else:
#         print guesses
#
# for letters in chosenword:
#     print [""]
#
# #
# for letters in chosenword:
#
#         if letters == chosenletter:
#
#             print letters
#
#     else:
#         print [""]

# for guesses in chosenword:
#     if chosenword < letters:
#         print fools_game


