string = input("Please type in a string: ")

length = 1
while length <= len(string):
    print(string[-length:]) 
    length += 1

Please type in a string: test
t
st
est
test



word = input("Please type in a string: ")
output = ""

for char in word:
    output += char
    print(output)

Please type in a string: test
t
te
tes
test


