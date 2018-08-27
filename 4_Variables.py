__author__ = 'Charles'

# Data Types, Operator and Precedence
a = 11
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a + b / 3 - 4 * 12)
# 11 + (3 / 3) - (4 * 12)
# 11 + 1 - 48

print((((a+b) / 3) -4) * 12)
c = a + b
d = c / 3
e = d - 4
print(e * 12)

# Sequence of characters
parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])

# IndexError: string index out of range
# print(parrot[14])

print(parrot[-1])
print(parrot[0:6])
print(parrot[-4:-2])
print(parrot[:6])
print(parrot[6:])
print(parrot[0:6:2])

number = "9,223,372,036,854,775,807"
print(number[1::4])
number2 = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(number2[0::3])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's probably pining")
print("Hello " *5)
print("Hello " * (5+4))
print("Hello " * 5 + "4")

today = "friday"
print("Today : " + today)
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days)
print("2: " + days[:-1])
print("0: " + days[:-1])
print(days[:])
# Slicing pythong string
# string[start:end] - blank mean beginning or last
# string[start:end:skip] - return, skip, return
# skip always from left to right
print(days[::2])


print(days[::5])
