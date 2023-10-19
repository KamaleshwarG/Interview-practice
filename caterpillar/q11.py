def arrange_elements_asc_desc(A, k):
    # Sort the first k elements in ascending order
    first_part = sorted(A[:k])

    # Sort the remaining elements in descending order
    second_part = sorted(A[k:], reverse=True)

    # Combine the two parts to get the final result
    result = first_part + second_part

    return result

# Input
n = 10
A = [9, 5, 2, 1, 4, 3, 0, 7, 6, 8]
k = 5

# Arrange elements and print the result
result = arrange_elements_asc_desc(A, k)
print(result)
