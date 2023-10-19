def alternate_elements_sum(A):

    A.sort()
    result = []

    for i in range(0 , len(A) , 2):
        result.append(A[i])

    return sum(result)


n = 7
A = [6, 5, 4, 2, 1, 3, 7]

# Find and print the alternate numbers after sorting
result = alternate_elements_sum(A)
print(result)