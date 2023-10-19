def countOccurence(num , key):
    count = 0

    # num_set = set(str(num))
    # print(num_set)
    # str_num = str(num)
    # for digit in str_num:
    #     if digit in num_set:
    #         count+=1

    str_num  = list(str(num))

    print(str_num)
    for digit in str_num:
        if( digit == str(key)):
            count+=1

    return count

result = countOccurence(123345534 , 2)

print( result)