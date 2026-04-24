'''Sort an array of strings according to string lengths
You are given an array arr[] of strings. Your have to sort the array in ascending order
based on the lengths of the strings. If two strings have the same length, maintain their
original relative order.
Examples:
Input: arr[] = ["GeeksforGeeeks", "I", "from", "am"]'''

def sortByLength(arr):
    return sorted(arr, key=len)


# Example
arr = ["GeeksforGeeeks", "I", "from", "am"]
print(sortByLength(arr))