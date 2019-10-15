# question 1
# Encrypts an imput string of the ASCII characters and prints
# the results. the other input is the distance value

# the ASCII values range from 0 through 127

plainText = input("enter a message: ")
distance = int(input("enter the distance value: "))
code = ""
for ch in plainText:
    ordValue = ord(ch)
    print(ordValue)
    cipherValue = ordValue = distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code += chr(cipherValue)
print(code)