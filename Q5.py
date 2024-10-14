#Try...Except

"""
Types of errors in Python:

IndexError = When the wrong index of a list is retrieved.
AssertionError = It occurs when the assert statement fails
AttributeError = It occurs when an attribute assignment is failed.
ImportError = It occurs when an imported module is not found.
KeyError = It occurs when the key of the dictionary is not found.
NameError = It occurs when the variable is not defined.
MemoryError = It occurs when a program runs out of memory.
TypeError = It occurs when a function and operation are applied in an incorrect type.
"""

#1) Run the following code below and observe the output of the program
# code a try...except statement that avoids the observed error and prints
# out that the program could not be completed

l1 = [1, 2, 3]
print(l1[4])