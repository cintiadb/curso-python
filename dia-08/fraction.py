from fractions import Fraction

def fractionate(amount: int):
    # Create a list with 'amount' number of Fraction(1, amount)
    return [Fraction(1, amount) for _ in range(amount)]

# Example usage
for p in fractionate(3):
    print(p)

print()

print(fractionate(5))