address = "Attractive Street, Beverly Hills, CA 90210"
#          012345678901234567890123456789012345678901 
print(address[0:17]) #from first index to character prior to last index
print(address[19:32])

print ("\n")

print(address[34:-6])
print(address[-8:-6])
print(address[-8:36])
#the prior three are equivalent

print ("\n")

print(address[2:]) #start at index 2 (third character) and pull through end of string
print(address[:32]) #start at beginning of string (index 0) and pull up to (but don't include) index 32
print(address[-10:]) #start 10 characters from the end and return everything after that

print(address[:]) #return full string
