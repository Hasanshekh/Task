"""
Problem 2:  Determine whether a given string is Palindrome
A string “madam” is a palindromic string because it reads the same forwards and backward. 
Input: “anna”
Output: true

Input: “India”
Output: false"""
def is_palindrome(string):
    # Reverse the string
    reversed_string = string[::-1]

    # Compare the reversed string with the original string
    if string == reversed_string:
        return True
    else:
        return False

# Test the function with the given inputs
input1 = "anna"
print(is_palindrome(input1))  # Output: True

input2 = "India"
print(is_palindrome(input2))  # Output: False