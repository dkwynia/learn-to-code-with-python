# Define a easy_money function that accepts no parameters 
# and always returns the value 100.
def easy_money():
    print(100)

easy_money()


# Define a best_food_ever function that accepts 
# no parameters and always returns the string “Sushi”.

def best_food_ever():
    print("Sushi, (not really)")

best_food_ever()

# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# 
# EXAMPLES:
# convert_to_currency(15)    => "$15"
# convert_to_currency(8)     => "$8"

def convert_to_currency(amount):
    amount_str = str(amount)
    print("$"+amount_str)

convert_to_currency(15)

convert_to_currency(8)