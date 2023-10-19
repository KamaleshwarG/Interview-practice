def arrangeEvenOdd(A, n):

    odd = []
    even = []

    for i in range(n):
        if( A[i]%2 == 0):
            even.append(A[i])
        else:
            odd.append(A[i])

    result = even.extend(odd)

    return result


n = 6
A = [5, 4, 1, 6, 3, 2]

result = arrangeEvenOdd(A , n)
print("The even and odd numbers are arranged:" , result)