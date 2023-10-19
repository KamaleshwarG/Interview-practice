def smallest_number(n):

    result = list(str(n))

    result.sort()

    if(result[0] == '0'):
        for i in range(1 , len(result)):
            if(result[i] != '0'):
                result[0] , result[i] = result[i] , result[0]
                break

    smallest = int("".join(result))

    return smallest

n = 3101

print(smallest_number(n))