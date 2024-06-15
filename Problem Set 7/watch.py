# importing libraries
import re as r

# function to print parse
def main():
    print(parse(input("HTML: ")))

# function to convert html iframe to short URL
def parse(s):
     if url := r.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{url.group(2)}"
     else:
        return None

# calling main function
if __name__ == "__main__":
    main()
