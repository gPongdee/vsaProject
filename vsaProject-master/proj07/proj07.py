# Name:
# Date:

# proj07: Word Game

import random
import string
from collections import Counter
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
n = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k':
        5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u':
        1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):

    #player_word = raw_input("Please input a word using the letters in your hand: ").lower()
    x = (word)
    player_word = []
    for letter in x:
        player_word.append(letter)
    for i in range(0, len(player_word)):
        player_word[i] = SCRABBLE_LETTER_VALUES.get(player_word[i], 0)

    if len(word) != n:
        score = sum(player_word) * len(word)
    elif len(word) == n:
        score = (sum(player_word) * len(word)) + 50
    return score


    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    #print                                # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    '''
    hand = {"w": 5, "o": 2, "r": 1, "k": 7}
    word = ['w', 'o', 'o', 'r', 'k', 'k']
    '''
    hand2 = hand.copy()
    var1 = Counter(word)
    #print var1

    for i in range(0, len(word)):
        l = var1[i]
        hand2[word[i]] -= l + 1
    return hand2












    # TO DO ...

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list, hand2):

    x = []
    for letter in word:
        x.append(letter)
    y = "".join(x)
    #print y
    if y in word_list:
        hand_keys = []
        word_count = Counter(word)
        # print "List: wordCount", word_count

        word_list1 = []
        for letter in word:
            word_list1.append(letter)
        # print "List: wordList", word_list1

        for i in hand2:
            hand_keys.append(i)
        # print "List: handKeys", hand_keys


        for i in range(0, len(word_list1)):

            if word_list1[i] not in hand_keys:
                return False
            elif word_list1[i] in hand2:
                if word_count[word_list1[i]] > hand2[word_list1[i]]:
                    return False

        if word_count[word_list1[i]] <= hand2[word_list1[i]]:
            return True

    elif y not in word_list:
        return False








    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO...

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list, hand2):


    score_total = []
    print "Hand: ", display_hand(hand)
    word = 'p'
    while word != '.':

        if empty_hand_tester(hand2) == True:
            print "Hand Finished! Your score is ", sum(score_total)
            play_game(word_list, hand)
            #print "Hand Finished! Your score is ", sum(score_total)
            #play_game(word_list, hand)

        word = raw_input("Please enter a word using the letters in your hand: ")
        score = get_word_score(word, n)
        if word == '.':
            print "Finish! Your score is ", sum(score_total)
            play_game(word_list, hand)
        elif is_valid_word(word, hand, word_list, hand) == False:
            print "That is an invalid word, please enter another one."
            continue
        elif is_valid_word(word, hand, word_list, hand) == True:
            update_hand(hand, word)
            print "Hand: ", display_hand(hand)
            print "Score: ", score
            score_total.append(score)
            hand = update_hand(hand, word)

def empty_hand_tester(hand2):
    for i in hand2:
        if hand2[i] != 0:
            return False
    return True

    # TO DO ...

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list, hand):
    word = 'p'
    again = raw_input("Would you like to play again? Enter n for a new random hand, enter r to replay the previous hand, enter e to exit the game. ")
    if again == 'n':
        print "Ok"
        hand = deal_hand(n)
        hand2 = hand.copy()
        play_hand(hand, word_list, word)
        return hand2
    elif again == "r":
        print "Ok"
        hand2 = hand.copy()
        play_hand(hand, word_list, word)
    elif again == 'e':
        print "Ok, bye"
    else:
        print "Input a valid response"
        play_game(word_list, hand)











"""
Allow the user to play an arbitrary number of hands.

* Asks the user to input 'n' or 'r' or 'e'.

* If the user inputs 'n', let the user play a new (random) hand.
    When done playing the hand, ask the 'n' or 'e' question again.

* If the user inputs 'r', let the user play the last hand again.

* If the user inputs 'e', exit the game.

* If the user inputs anything else, ask them again.
"""
# TO DO...

#
# Build data structures used for entire session and play game

if __name__ == '__main__':
    word_list = load_words()
    hand = deal_hand(n)
    play_game(word_list, hand)
