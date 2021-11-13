# find always returns an integer, either the index number, or -1
browser = "Google Chrome"
print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("Z"))
print()
print(browser.find("o"))
print(browser.find("o",3)) #still returns the index of the character, but it starts looking from 3 (remembering that the first char is 0)
#in only tells that a substring exists, .find tells you where it is

browser = "Google Chrome"
print(browser.index("C"))
print(browser.index("Z")) #find returns -1, index crashes out with a ValueError

txt = "Hello, welcome to my world."

print(txt.rfind("o"))
print(txt.rindex("o"))

browser = "Google Chrome"

print(browser.rfind("o"))
print(browser.rfind("O"))
print(browser.rfind("G"))