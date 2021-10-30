#escape characters always begin with \
#new line
print("This will \nbegin on a \nnew line")

#tab
print("\tOnce upon a time")

#include quotes
print ('"To be or not to be", said Hamlet')
#or
print("\"To be or not to be\", said Hamlet")

print("to print a backslash: \\")

#raw strings?


#file_name = "C:\news\travel" <-- will treat the backslashes as escape codes

file_name = r"C:\news\travel" #<-- r means treat the string as raw, ignore escape codes
print(file_name)

some_random_number = 5
some_obscure_calculation = 25
some_additional_statistic_fetched_from_somewhere = 10
final = some_random_number + some_obscure_calculation + some_additional_statistic_fetched_from_somewhere
print(final)

# or you can

final = some_random_number + \
        some_obscure_calculation + \
        some_additional_statistic_fetched_from_somewhere

print(final)

print("misfortune"[10])