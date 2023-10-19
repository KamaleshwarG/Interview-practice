def find_common_string(n , S):
 
    common_prefix = ""

    for i in range(n):
        char = S[0][i]

        if all(s[i] == char for s in S):
            common_prefix +=  char
        else :
            break

    return common_prefix




n = 3
S = ['Ram', 'Ramanathan', 'Ramesh']

result = find_common_string(n , S)

print("The common string is :" , result)