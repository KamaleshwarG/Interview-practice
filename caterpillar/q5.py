def count_special_characters(S):

    special_characters = "!@#$%^&*()_-+=:;<>?/|\[]~`.,"

    count = 0
    for s in S:
        if s in special_characters:
            count += 1

    return count

S = 'mca@2022\ #23.89'

# Find and print the number of special characters
result = count_special_characters(S)
print(result)