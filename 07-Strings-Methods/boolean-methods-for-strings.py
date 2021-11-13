#lower case check
print("winter".islower())
print("winter 12#$".islower())
print("Winter".islower())
#upper case check
print("SUMMER".isupper())
print("SUMMER 12#$".isupper())
print("sUMMER 12#$".isupper())
#title case check
print("The 4 Seasons".istitle())

print()

#all characters alphabetic
print("asdf".isalpha())
print("asdf 12$".isalpha())
print("asdf".isalpha())
print("asdf 12$".isalpha())
#all characters numeric
print("12".isnumeric())
print("asdf 12".isnumeric())

#all characters either alpha or numeric
print("asdf123".isalnum())
print("asdf 123".isalnum())
print("123%".isalnum())

#all characters spaces
print(" ".isspace())

