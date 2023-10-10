"""Problem 5: Swap two numbers without using a temporary variable
Input:integer a = "10", b = "50".
Output: Strings after swap: a = 50 and b = 10"""

#Intial Values
a = "10"
b = "50"

# Convert strings to integers
a = int(a)
b = int(b)

# Perform the swap operation
a = a + b
b = a - b
a = a - b

# Convert integers back to strings
a = str(a)
b = str(b)

# Print the swapped numbers
print("Strings after swap: a =", a, "and b =", b)
