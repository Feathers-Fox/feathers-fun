# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

guesses = -1
while guesses < 6:
    guesses = guesses + 1
    print "you have played this game"
    print guesses
    print "times so far!"
    import random

    var = random.randint(1, 9)
    #print var

    guess = int(raw_input("Pick a number... any number (only 1-9 though)"))
    if guess > 9 or guess < 1:
        guess2 = int(raw_input("maybe you didnt hear me. only numbers one through nine!"))   # correct
        if guess2 > 9 or guess2 < 1:
            print "... i SAID any number BETWEEN ONE AND NINE"

            # if guess2 > 9 or guess2 < 1:
        print "...if you arent going to play this game right, why are you here? (***roasted***) and since you were either that stupid or just that much of a brat, you cant play anymore."
        print "goodbye world"
        exit()
    if guess == int(var):
        print "ya got it! thats the correct number!"



    else:
        print str(var)
        print "...was the correct randomly generated answer. sorry! you didnt win. try again, or press control --> D to quit"
    if guess > int(var):
        print "a little too high :|"
    if guess < int(var):
        print "a little too low :|"






