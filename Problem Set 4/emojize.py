# importing emoji library
import emoji

#input text
text = input("Input: ")

# output emojis
emojis = emoji.emojize(text, language="alias")
print(f"Output: {emojis}")
