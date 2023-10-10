"""Problem 3:  Biggest and smallest number in an array
 Write a program to print the biggest and smallest number in the array. 

Input: arr[] = {1, 2, 3, 4, 5}
Output: Maximum is: 5
Minimum is: 1

Input: arr[] = {5, 3, 7, 4, 2}
Output: Maximum is: 7
Minimum is: 2""" 

def find_max_min(arr):
    if not arr:
        return "Array is empty"

    maximum = minimum = arr[0]

    for num in arr[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return "Maximum is:", maximum, "Minimum is:", minimum

# Example usage
arr1 = [1, 2, 3, 4, 5]
result1 = find_max_min(arr1)
print("Input:", arr1)
print("Output:", result1)

arr2 = [5, 3, 7, 4, 2]
result2 = find_max_min(arr2)
print("Input:", arr2)
print("Output:", result2)
