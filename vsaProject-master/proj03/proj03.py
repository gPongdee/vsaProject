# Name: Gabriel Pongdee
# Date: 6/20/17
import random

""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""










def main():
    randnumber = random.randint(0, 9)
    tries = int(raw_input("How many turns do you want(Please enter as a number, i.e. 3)?"))
    count = 1

    while count <= tries:
        guess = raw_input("Please enter a number between one and nine(i.e. 7)").lower()

        if int(guess) > randnumber:
            print "Too high, guess again."
            tries = tries - 1
            print "You have " + str(tries) + " tries left."
        elif int(guess) == randnumber:
            print "Correct! Congratulations!"
            playAgain()
        elif int(guess) < randnumber:
            print "Too low, guess again."
            tries = tries - 1
            print "You have " + str(tries) + " tries left."
        elif guess == "exit":
            print "Ok, bye."
            quit()
        else:
            print "Sorry, didn't get that. Please try again"

    if tries == 0:
        playAgain()


def playAgain():
    again = raw_input("Would you like to play again(Yes or No)?").lower()

    if again == "yes" or again == "yeah" or again == "yep":
        print "Ok, new game"
        main()
    elif again == "no" or again == "nope" or again == "nah":
        print "Ok, game over"
    else:
        print "Sorry, didn't get that. Please try again."




main()