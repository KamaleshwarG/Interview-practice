def check_index(A):

    result = []

    for i in range(len(A)):
        
        for j in range(len(A)):
            if(i == A[j]):
                result.append(j)
                

    return result


n = 6
A = [1, 4, 5, 2, 0, 3]

print(check_index(A))