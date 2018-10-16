__author__ = 'charles'

# Boolean
print("### 1. The boolean value True or False")
print("False is {0}".format(False))
print("True is {0}".format(True))
print()

print("### 2. Empty string is False.  Non empty string is True.")
print("'false' is {0}".format(bool('false')))
print("'true' is {0}".format(bool('true')))
print("'' is {0}".format(bool('')))
print()

print("### 3. Empty string is False.  Non empty string is True.")
print('"false" is {0}'.format(bool("false")))
print('"true" is {0}'.format(bool("true")))
print('"" is {0}'.format(bool("")))
print()

print("### 4. None (a.k.a null) is False")
print("None is {0}".format(bool(None)))
print()

print("### 5. 0 is False. Other number is True.")
print("-2 is {0}".format(bool(-2)))
print("-1 is {0}".format(bool(-1)))
print("0 is {0}".format(bool(0)))
print("1 is {0}".format(bool(1)))
print("2 is {0}".format(bool(2)))
print()

print("### 6. 0.0 is False. Other decimal is True.")
print("-0.2 is {0}".format(bool(-0.2)))
print("-0.1 is {0}".format(bool(-0.1)))
print("0.0 is {0}".format(bool(0.0)))
print("0.1 is {0}".format(bool(0.1)))
print("0.2 is {0}".format(bool(0.2)))
print()

print("### 7. Empty list is False. Non empty list is True.")
print("[] is {0}".format(bool([])))
print("['a'] is {0}".format(bool(['a'])))
print("['a','b'] is {0}".format(bool(['a','b'])))
print()

print("### 8. Empty tuple is False. Non empty tuple is True.")
print("() is {0}".format(bool(())))
print('("abc") is {0}'.format(bool(("abc"))))
print('("abc","def") is {0}'.format(bool(("abc","def"))))
print()

print("### 8. Empty dictionary or set is False. Non empty set of dictionary is True.")
print(bool({}))
print(bool({"k1":"v1","k2":"v2"}))
print()



