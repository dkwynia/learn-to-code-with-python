#0 is false, everything else is true
if 3:
    print("Hello")

if 0:
    print("nope")

if -1:
    print("Hello")

if "":
    print("nope, won't print")

if "Hello":
    print("Hello")

#function bool evaluates truthiness of expression
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("hi"))