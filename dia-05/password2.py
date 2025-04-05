import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_special: bool) -> str:
    special_chars = "!?=+-()#"
    all_chars = string.ascii_lowercase
    
    password = [random.choice(string.ascii_lowercase)]  
    
    if include_numbers:
        all_chars += string.digits
        password.append(random.choice(string.digits))
    
    if include_special:
        all_chars += special_chars
        password.append(random.choice(special_chars))  
    while len(password) < length:
        password.append(random.choice(all_chars))
    
    random.shuffle(password)  
    
    return "".join(password)

for i in range(10):
    print(generate_strong_password(8, True, True))