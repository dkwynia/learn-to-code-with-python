empty_space = "               content                 "
print(len(empty_space))
print(empty_space.rstrip())
print(len(empty_space.rstrip()))
print(empty_space.rstrip().lstrip())
print(len(empty_space.rstrip().lstrip()))

website="www.python.org"
print(website.lstrip("w"))
print(website.rstrip("org"))
print(website.strip("worg."))
# strip lstrip and rstrip only pull characters from the beginning, the end or both
# defaults to stripping space