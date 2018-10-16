__author__ = 'charles'

# Python block done by indention
for i in range(1, 12):
    print("No {:2} squared is {:3} and cubed is {:5}".format(i, i ** 2, i ** 4))

# Multiple statements within same block
for i in range(1, 12):
    print("No {:2} squared is {:3}".format(i, i ** 2))
    print("No {:2} cubed is {:5}".format(i, i ** 3))
    print("Next\n")
