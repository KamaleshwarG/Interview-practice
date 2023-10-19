def check_negative_in_array(n,A,k):

    result = []
    
    for i in range(n):

        group = A[i : i+k]
        first_negative = 0

        if(len(group) != 3):
            break
        else:
            for num in group:
                if num<0:
                    first_negative = num
                    break
                else:
                    first_negative = 0

        result.append(first_negative)
            

    return result



A = [-10,-5,4,0,-3, 2,1,4]
n = 8
k = 3

output = check_negative_in_array(n,A,k)

print("The result is :" , output)





