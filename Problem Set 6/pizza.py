# importing libraries
import csv as c
import sys as s
from tabulate import tabulate as t

# function to identify file type and line length
def main():
    if len(s.argv) < 2:
        s.exit("Too few command-line arguments")
    elif len(s.argv) > 2:
        s.exit("Too many command-line arguments")
    else:
        if s.argv[1][-4:] != ".csv":
            s.exit("Not a CSV file")
        else:
            print(tabulize(s.argv[1]))

# function to read and tabulize format to tabulate
def tabulize(file):
    try:
        with open(file) as f:
            read = c.reader(f)
            tables = t(read, headers="firstrow", tablefmt="grid")
            return tables
    except FileNotFoundError:
        s.exit("File does not exist")

# calling main function
if __name__ == "__main__":
    main()
