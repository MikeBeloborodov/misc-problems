"""
Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string, the longest possible, containing distinct letters - 
each taken only once - coming from s1 or s2.
"""

def longest(a1, a2):
    all_letters = []
    result = ""

    for letter in a1:
        if not letter in all_letters:
            all_letters.append(letter)

    for letter in a2:
        if not letter in all_letters:
            all_letters.append(letter)

    for i in range(len(all_letters)):
        min_index = i
        for j in range(i, len(all_letters)):
            if all_letters[j] < all_letters[min_index]:
                min_index = j
        all_letters[i], all_letters[min_index] = all_letters[min_index], all_letters[i]

    for letter in all_letters:
        result += letter

    return result


def main():
    test_string1 = "aretheyhere"
    test_string2 = "yestheyarehere"
    test_string_result = "aehrsty"

    result = longest(test_string1, test_string2)

    assert result == test_string_result
    print("passed!")

if __name__ == "__main__":
    main()