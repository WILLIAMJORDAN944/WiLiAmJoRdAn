# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
# raw_input ("lets play a game of hangman, press RETURN to start")
#
# raw_input ("guess a letter for the word")
raw_input ("press RETURN to see if the word is a palindrome")
str  = "racecar"





lst = []
for letter in str:
    lst.append(letter)

print lst

str = "racecar"
lst2 = []
for letter in str:
    lst.reverse()

print lst
