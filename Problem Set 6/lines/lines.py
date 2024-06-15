#importing libraries
import sys

# function to identify file type and line length
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a python file")
        else:
            print(line_count(sys.argv[1]))

# function to count lines
def line_count(file):
    try:
        count = 0
        with open(file, "r") as f:
            for lines in f:
                if not (lines.lstrip().startswith("#") or lines.strip() == ""):
                    count = count + 1
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")

# calling main function
if __name__ == "__main__":
    main()
