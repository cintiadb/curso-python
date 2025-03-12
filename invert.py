def invert(dictionary: dict):
    inverted_dict = {}  
    
    for key, value in dictionary.items():
        inverted_dict[value] = key 

    dictionary.clear() 
    dictionary.update(inverted_dict) 

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)
