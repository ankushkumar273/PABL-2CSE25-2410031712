def union_of_arrays(a, b):
    union_set = set()

    # Add elements from first array
    for num in a:
        union_set.add(num)

    # Add elements from second array
    for num in b:
        union_set.add(num)

    # Convert set to list (any order is fine)
    return list(union_set)


# Example usage
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

result = union_of_arrays(a, b)
print("Union of arrays:", result)
