# Name: Gabriel Pongdee
# Date: 6/20/17

# proj05: functions and lists

# Part I
import random



def main():
    user_number = int(raw_input("Enter a number(i.e. 7)"))
    count = [i for i in range(1, user_number +1 ) if user_number % i == 0]
    prime = len(count)
    if prime != 2:
        print "Your number is not prime."
        print "Your number's factors are " + str(count)
    elif prime == 2:
        print "Your number's factors are " + str(count)
        print "Prime number detected"

main()

print list(set([random.randrange(1, 20) for _ in range(0, random.randint(5, 45))]) and set([random.randrange(1, 20) for _ in range(0, random.randint(5, 45))]))

# Part III

def rightTriangles():
    side1 = float(raw_input("Please enter the length of the first side of your triangle(i.e. 7)."))
    side2 = float(raw_input("Please enter the length of the second side of your triangle."))
    side3 = float(raw_input("Please enter the length of the third side of your triangle."))
    list1 = [side1, side2, side3]
    list1.sort(key=int)
    short_sides = [list1[0], list1[1]]
    square_side_1 = short_sides[0] * short_sides[0]
    square_side_2 = short_sides[1] * short_sides[1]
    square_side_3 = list1[2] * list1[2]

    if square_side_1 + square_side_2 == square_side_3:
        print "Yes, those three lengths can make a right triangle"
        replay()
    elif square_side_1 + square_side_2 != square_side_3:
        print "No, those lengths can not form a right triangle"
        replay()

def replay():
    again = raw_input("Would you like to try a different combination(Yes or No)?").lower()

    if again == "yes" or again == "yeah" or again == "yep":
        print "Ok"
        rightTriangles()
    elif again == "no" or again == "nope" or again == "nah":
        print "Ok, bye"
        quit()
    else:
        print "Sorry, didn't get that. Please try again."

rightTriangles()


# TESTS
# Feel free to add your own tests as needed!
'''
print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")'''
