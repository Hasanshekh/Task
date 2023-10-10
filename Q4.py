"""Problem 4:  Swap two Strings Without Using any Third Variable
 Input: a = "Hello", b = "World".
Output: Strings after swap: a = World and b = Hello"""

# Input strings
a = "Hello"
b = "World"

# Swap the strings without a third variable
a = a + b
b = a[:len(a) - len(b)]
a = a[len(b):]

# Print the result
print("Strings after swap: a =", a, "and b =", b)
