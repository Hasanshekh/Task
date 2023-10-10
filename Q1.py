"""
Problem 1: Program to count occurrences of a given character in a string.
Count character 'e' in the below string.
	Input "geeksforgeeks". 
	Output: 4

	Count character '3' in the below string.
	Input "abccdefgaa."
	Output : 3"""

def count_occurrences(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count

# Example usage
string1 = "geeksforgeeks"
character1 = 'e'
output1 = count_occurrences(string1, character1)
print(output1)  # Output: 4

string2 = "abccdefgaa"
character2 = '3'
output2 = count_occurrences(string2, character2)
print(output2)  # Output: 3