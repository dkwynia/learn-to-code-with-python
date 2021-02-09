#normal
def add(a, b):
    return a + b

print(add(3,5))

#default arguments
def add(a = 0, b = 0): #can have some default, others not, the defaults have to come last
    return a + b

print(add(7,8))
print(add(10))
print(add())