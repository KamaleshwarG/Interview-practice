def alternate_elements_in_array(A):

    A.sort()
    result = []

    for i in range(0 , len(A) , 2):
        result.append(A[i])

    return result


n = 7
A = [6, 5, 4, 2, 1, 3, 7,8,9,11,10,15,12,13,14]

# Find and print the alternate numbers after sorting
result = alternate_elements_in_array(A)
print(result)