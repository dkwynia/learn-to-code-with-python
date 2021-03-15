#checking for inclusion and exclusion

announcement = "The winners of the prize are Boris, Andy, and Adam"

print("Boris" in announcement) #prints True
print("boris" in announcement) #prints False
print("Steven" in announcement) #prints False

#doesn't check where the string is, or how many times, just is it in the string

print(" " in announcement) #prints True, there is a space in announcment



print("Boris" not in announcement) #prints False
print("boris" not in announcement) #prints True
print("Steven" not in announcement) #prints True

print(" " not in announcement) #prints False, there is a space in announcment



