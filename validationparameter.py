def new_person(name: str, age: int):
    if not name or len(name.split()) < 2 or len(name) > 40:
       raise ValueError("That is not a valid name") 
    if age <0 or age > 150:
        raise ValueError("That is not a valid age")
    
    return name, age

new_person("Cintia Dias",30)


