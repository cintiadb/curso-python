word = input("Please type in a word:")
character_to_find =input("Please type in a charater:")

if character_to_find in word:
    index = word.find(character_to_find)
    
    while True:
        word_len = len(word)
        if index != -1 and index + 3 <= word_len:
            print(word[index:index+3]) 
        word = word[index + 1:]
        index = word.find(character_to_find)
        if index == -1:
            break

"""
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1
    
----------------------------------
contador = 0
for letter in word:
    if letter == character_to_find:
        contador = contador + 1

"""
