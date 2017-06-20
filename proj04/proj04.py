# Name:
# Date:

def main():
    user_string = raw_input("Type a word or phrase: ").lower().replace(" ", "")
    opp_string = user_string[::-1].lower().replace(" ", "")
    if user_string == opp_string:
        print "Palindrome yay!"
    elif user_string != opp_string:
        print "That is not a palindrome."
    replay()
def replay():
    again = raw_input("Would you like to try another phrase(yes or no)?").lower()
    if again == "yes" or again == "yeah" or again == "yep":
        print "Ok"
        main()
    elif again == "no" or again == "nope" or again == "nah":
        print "Bye"
        quit()
main()

