# a name, an adjective and a noun
mad_libs = "{} laughed at the {} {}."
# send by position
print(mad_libs.format("Bob","green","alien"))
print(mad_libs.format("Jennifer","silly","tomato"))
# Can send more than three, can't send less

# mad_libs = "{0} laughed at the {1} {2}."
# #send by numeric position
# print(mad_libs.format("Bob","green","alien"))
# print(mad_libs.format("Jennifer","silly","tomato"))
# # Can send more than three, can't send less

# mad_libs = "{2} laughed at the {1} {0}."
# #send by numeric position
# print(mad_libs.format("Bob","green","alien"))
# print(mad_libs.format("Jennifer","silly","tomato"))
# # Can send more than three, can't send less

#by descriptors
mad_libs = "{name} laughed at the {adjective} {noun}."
#send by keyword arguments
# print(mad_libs.format(name="Bob",adjective="green",noun="alien"))
# print(mad_libs.format(adjective="silly",noun="tomato",name="Jennifer"))

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name = name, adjective = adjective, noun = noun))