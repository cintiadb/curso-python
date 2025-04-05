import string

def separate_characters(my_string: str):
    letters = ""
    punctuation = ""
    others = ""
    
    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuation += char
        else:
            others += char
    
    return (letters, punctuation, others)


parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])  
print(parts[1])  
print(parts[2])  

"""
Explanation:
string.ascii_letters: This constant contains all lowercase and uppercase ASCII letters (a-zA-Z).

string.punctuation: This constant contains all punctuation characters, such as !"#$%&'()*+,-./:;<=>?@[\]^_{|}~`.

We iterate through each character in the input string, checking whether it belongs to one of these categories (letters, punctuation, or others). The characters are then added to the respective string."""