__author__ = 'charles'

# Read input and store in variable name
name = input("Please enter your name: ")

# Read input, convert to int and store in variable age
age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# Conditional statement
if age >= 18:
    # 18 or greater print this
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    # Less than 18 print this
    print("Please come back in {0} years".format(18-age))





