def squared(s, n):
    length = len(s)
    for i in range(n):  # Generate 'n' lines
        line = "".join(s[(i + j) % length] for j in range(n))  # Take 'n' characters, wrapping around
        print(line)

# Testing the function
print("Sample Output:")
squared("ab", 3)
print()
squared("aybabtu", 5)