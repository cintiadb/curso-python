import json

def print_persons(filename: str):
    with open(filename,"r") as my_file:
        data = json.load(my_file) 
        for person in data:
            name = person["name"]
            age = person["age"]
            hobbies = person["hobbies"]
            hobbies_str = ', '.join(hobbies)
            print(f"{name} {age} years ({hobbies_str})")


print_persons(filename="person.json")