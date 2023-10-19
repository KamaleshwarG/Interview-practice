def check_repeat(str):
    n = len(str)

    rev_str = str[::-1]
    count = 0

    for i in range(n):
        if(str[i] == rev_str[i]):
            count += 1

    return count


#test 1

input_one = "encyclopedia"
print("The result of test one is :" , check_repeat(input_one))

#test 2
input_two = "abcdecba"
print("The result of test two is :" ,check_repeat(input_two))