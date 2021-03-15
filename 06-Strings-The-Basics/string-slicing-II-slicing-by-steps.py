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