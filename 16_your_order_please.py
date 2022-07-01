"""
Your task is to sort a given string. 
Each word in the string will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. 
The words in the input String will only contain valid consecutive numbers.
"""
def order(sentence):
    if not sentence:
        return sentence

    result_list = ["" for i in range(9)]
    result = "" 

    for word in sentence.split(" "):
        for letter in word:
            if letter.isnumeric():
                result_list[int(letter) - 1] = word

    for item in result_list:
        if item:
            result += item + " "
    
    return result[:-1]

def main():
    test_string = "wo2rd thi1s b4e sho3uld"
    test_string_changed = "thi1s wo2rd sho3uld b4e"

    result = order(test_string)
    assert result == test_string_changed

    print("passed!")
    print("Original: " + test_string)
    print("Result: " + result)

if __name__ == "__main__":
    main()