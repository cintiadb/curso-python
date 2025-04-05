import json

def print_persons(filename: str):
    with open("person.json") as my_file:
        data = my_file.read()

        for person in data:
            name = person['name']
            age = person['age']
            hobbies = person['hobbies']
            hobbies_str = ', '.join(hobbies)
            print(f"{name} {age} years ({hobbies_str})")

