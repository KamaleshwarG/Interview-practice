def remove_vowel(S):
    result = ""
    vowels = "aeiou"

    for char in S:
        if char not in vowels:
            result += char

    return result

S = "encyclopedia"
print(remove_vowel(S))