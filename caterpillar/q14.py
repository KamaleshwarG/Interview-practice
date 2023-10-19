def count_unique_characters(S):
    unique_chars = set()
    seen_chars = set()

    for char in S:
        if char.isalpha():  # Check if the character is a letter
            char_lower = char.lower()  # Convert to lowercase to consider case-insensitive uniqueness
            if char_lower not in seen_chars:
                unique_chars.add(char_lower)
            else:
                unique_chars.discard(char_lower)

            seen_chars.add(char_lower)

    count = len(unique_chars)
    return count

# Input
S = 'encyclopedia'

# Find and print the count of unique characters (considering only one occurrence of each character)
result = count_unique_characters(S)
print(result)
