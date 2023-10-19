def find_error_occurrence(S, R):
    error = abs(S - R)
    return error

# Input for Test Case 01
S1 = 5
R1 = 9

# Input for Test Case 02
S2 = 5
R2 = 8

# Find and print the error occurrence for both test cases
error1 = find_error_occurrence(S1, R1)
error2 = find_error_occurrence(S2, R2)

print(error1)  # Output for Test Case 01
print(error2)  # Output for Test Case 02
