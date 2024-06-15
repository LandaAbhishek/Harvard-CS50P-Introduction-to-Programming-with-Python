# input text
text = input("Input: ")
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
print("Output: ", end="")

# outcome for text
for c in text:
    if c in vowels:
        continue
    print(c, end="")

print()
