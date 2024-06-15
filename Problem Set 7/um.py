# importing libraries
import re as r

# function to input text
def main():
    print(count(input("Text: ")))

# function to count um
def count(s):
  m = r.findall(r'\b(um)\b', s, r.IGNORECASE)
  return len(m)

# calling main function
if __name__ == "__main__":
    main()
