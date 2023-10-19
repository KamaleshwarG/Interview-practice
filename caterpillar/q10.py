# def find_inbetween_numbers(A , s , e , n):

#     A.sort()
#     result = []

#     for i in range(n):
#         if(A[i] == s):
#             start = i
#         if(A[i] == e):
#             end = i

#     for j in range(start , end):
#         result.append(A[j])

#     return result


# n = 9
# A = [10, 15, 12, 11, 5, 3, 2, 4, 7]
# start = 2
# end = 10

# print(find_inbetween_numbers(A , start , end , n))


def numbers_between_range(A, start, end):
    result = []

    for num in A:
        if start <= num <= end:
            result.append(num)

    return result

# Input
n = 9
A = [10, 15, 12, 11, 5, 3, 2, 4, 7]
start = 2
end = 10

# Find and print the numbers within the given range
result = numbers_between_range(A, start, end)
print(result)
