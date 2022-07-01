"""
The goal of this exercise is to convert a string to a new string 
where each character in the new string is "(" if that character appears only once in the original 
string, or ")" if that character appears more than once in the original string. Ignore capitalization 
when determining if a character is a duplicate.
"""
def duplicate_encode(word):
    hash_map = {}
    result_string = ""
    
    for letter in word.lower():
        if letter in hash_map:
            hash_map[letter] = 2
        else:
            hash_map.update({letter: 1})
    
    for letter in word.lower():
        if hash_map[letter] == 1:
            result_string += "("
        else:
            result_string += ")"
    
    return result_string