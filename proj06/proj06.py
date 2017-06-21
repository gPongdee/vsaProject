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

x = random.choice(wordlist)
word = []
for letter in x:
    word.append(letter)
print x
print "I am thinking of a " + str(len(word)) + " letter word"

def main():
    guesses_made = []
    lives = 6
    a = len(x) * "_,"
    print a
    while lives > 0:
        player_input = raw_input("Guess a letter(i.e. t)").lower()
        player_guess = player_input[0]
        for i in player_guess:
            intersection2 = [el for el in guesses_made if el in player_guess]
            if intersection2 == []:
                guesses_made.append(i)
                intersection = [el for el in word if el in player_guess]
                if intersection == []:
                    print "Incorrect guess"
                    lives = lives - 1
                    print "You lost a life :( Lives = " + str(lives) + "."
                elif intersection != []:
                    print "Good guess"
                print "You have guessed these letters ", guesses_made
            elif intersection2 != []:
                print "You have already guessed that letter"
                print "You have guessed these letters ", guesses_made

        if lives == 0:
            print "Game Over"
            print "The word was",x
            quit()

        set2 = set(guesses_made)
        correct_guesses = [el for el in word if el in set2]
        print correct_guesses
        if correct_guesses == word:
            print "You win!"
            quit()



main()






# your code begins here!
'''
x = "testing"

word = []
for letter in x:
    word.append(letter)
print word
a = len(word) * "_,"
print a
player_input = raw_input("input a single letter")
player_guess = player_input[0]




def wordReplace(player_guess, a):


    while lives > 0:
        player_input = raw_input("Guess a letter(i.e. t)").lower()
        player_guess = player_input[0]
        for i in player_guess:
            intersection2 = [el for el in guesses_made if el in player_guess]
            if intersection2 == []:
                guesses_made.append(i)
                intersection = [el for el in word if el in player_guess]
                if intersection == []:
                    print "Incorrect guess"
                    lives = lives - 1
                    print "You lost a life :( Lives = " + str(lives) + "."
                elif intersection != []:
                    print "Good guess"
                print "You have guessed these letters ", guesses_made
            elif intersection2 != []:
                print "You have already guessed that letter"
                print "You have guessed these letters ", guesses_made

'''