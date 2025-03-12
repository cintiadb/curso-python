def factorials(n: int):
    d = {}  # Initialize an empty dictionary
    fact = 1  # Start with factorial of 1
    
    for i in range(1, n + 1):
        fact *= i  # Compute factorial iteratively
        d[i] = fact  # Store it in the dictionary
    
    return d  # Return the dictionary

# Example usage
k = factorials(5)
print(k[1])  # Output: 1
print(k[3])  # Output: 6
print(k[5])  # Output: 120