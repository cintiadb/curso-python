my_string = "this is an example"

def no_vowels(my_string):
    for item in "aeiouAEIOU":
        my_string = my_string.replace(item,"")
    return my_string

        
print(no_vowels(my_string))