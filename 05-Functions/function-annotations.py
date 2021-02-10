#repeat a string as many times as we want
def word_multiplier(word: str, times: int) -> str: #does not limit the type that can be fed or returned, just annotates
    return word * times

#both of these are legal
print(word_multiplier("dog",5))
print(word_multiplier(4,5))
