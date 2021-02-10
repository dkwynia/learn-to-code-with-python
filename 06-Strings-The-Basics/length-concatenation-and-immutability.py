print(len("davidw"))
#print(len(4)) #error int has no len()
#print(len(3.2)) #error float has no len()

print("David" + " " + "Wynia")
print("David" "Wynia")
print("--" * 50)
print(len("--" * 50))

#immutability
#numbers, floats, integers and strings are immutable, which means incapable of change
#he'll make more of this point later

# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True

def long_word(a_string: str) -> bool:
    return len(a_string) > 7

print(long_word("Python") )
print(long_word("magnificent"))

# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False
def first_longer_than_second(str1 : str, str2: str) -> bool:
    return len(str1) > len(str2)

print(first_longer_than_second("Python", "Ruby") )
print(first_longer_than_second("cat", "mouse"))
print(first_longer_than_second("Steven", "Seagal"))