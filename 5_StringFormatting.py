__author__ = 'Charles'
age = 24
price = 1.23

# TypeError: must be str, not int
# print("My age is " + age + " years")

# Use str() to convert number to string
print("My age is " + str(age) + " years")

# TypeError: must be str, not int
#print("The price is " + price + ".)

# Use str() to convert number to string
print("The price is " + str(price) + ".")

# String Formatting
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))

# Can reuse the values
print("""
January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# Python 2 string formatting
print("My age is %d %s %d %s" % (age, "years", 6, "months"))

# Use %2d - 2 spaces, %4d - 4 spaces
# i ** 2 - i * i
# i ** 3 - i * i * i
for i in range(1,12):
    print("No, %2d squared is %4d and cubed is %4d" % (i, i ** 2, i** 3))


# 12.50d - 12 to the left and 50 decimal
print("Pi is approximately %12.50f" % (22/7))

# python 3 string replacement
# argument index:spacel
for i in range(1,12):
    print("No, {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# Auto argument index
for i in range(1,12):
    print("No, {:2} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))

# index:space.decimal
print("Pi is approximately {0:12.50}".format(22/7))

