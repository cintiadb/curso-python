def histogram(s: str):
    frequency = {} 
    
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1  
    
    for letter, count in sorted(frequency.items()):  
        print(f"{letter} {'*' * count}")  
        
histogram("abba")
print()
histogram("statistically")
