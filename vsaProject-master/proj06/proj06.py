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





def main():
    wordlist = load_words()

    x = random.choice(wordlist)
    word = []
    for letter in x:
        word.append(letter)

    #print x
    print "I am thinking of a(n) " + str(len(word)) + " letter word"
    print "_" * len(word)
    lives = 6
    a = ["_"] * len(word)
    guessed_letters = []
    while lives > 0:
        player_input = raw_input("Input a single letter: ")
        player_guess = player_input[0]
        intersection2 = [el for el in guessed_letters if el in player_guess]
        if intersection2 == []:
            intersection = [el for el in word if el in player_guess]
            if intersection == []:
                print "Sorry, incorrect"
                lives = lives - 1
                print "You lost a life. Lives = " + str(lives)
                print "".join(a)
                for o in player_guess:
                    guessed_letters.append(o)
                    set1 = set(guessed_letters)
                    print "You have guessed the following letters: ", set1
            elif intersection != []:
                for i in range(0, len(word)):
                    if word[i] == player_guess:
                        a[i] = player_guess

                    if i == len(word) -1:
                        print "Good guess :)"
                        print "".join(a)
                        for o in player_guess:
                            guessed_letters.append(o)
                            set1 = set(guessed_letters)
                            print "You have guessed the following letters: ", set1

            print "---------------------"

        elif intersection2 != []:
            print "You have already guessed that letter, please try again."


        if "".join(a) == x:
            print "Congratulations, you win!"
            playAgain()

        if lives == 0:
            print "Game Over"
            print "The word was",x
            playAgain()


def playAgain():
    again_input = raw_input("Would you like to play again(Yes or No)? ").lower()
    again = again_input[0]

    if again == "y":
        print "Ok"
        main()
    elif again == "n":
        print "Ok, bye"
        quit()
    else:
        print "Sorry, didn't get that. Please try again."
        playAgain()





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