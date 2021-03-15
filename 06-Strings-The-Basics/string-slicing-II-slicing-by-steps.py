alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10])
print(alphabet[0:10:2]) #skipping every other character, returning even numbered indexes

print(alphabet[0:26:3])
print(alphabet[:26:3])
print(alphabet[0::3])
print(alphabet[::3])

print(alphabet[4:20:5])
print(alphabet[-20:-8:5])
print(alphabet[::-3])
print(alphabet[::-1])

# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")   => "dyn"
# first_three_characters("empire")    => "emp"

def first_three_characters(phrase):
    return phrase[0:3]

def last_five_characters(phrase):
    return phrase[-5:]

def is_palindrome(str1):
    return str1[::-1]==str1

print(first_three_characters("dynasty"))
print(first_three_characters("empire"))
print(first_three_characters("racecar"))
print(last_five_characters("dynasty"))
print(last_five_characters("empire"))
print(last_five_characters("racecar"))
print(is_palindrome("dynasty"))
print(is_palindrome("empire"))
print(is_palindrome("racecar"))