# importing libraries
import csv as c
import sys as s

# function to identify file type and arguments length
def main():
    if len(s.argv) < 3:
        s.exit("Too few command-line arguments")
    elif len(s.argv) > 3:
        s.exit("Too many command-line arguments")
    else:
        if s.argv[1][-4:] != ".csv":
            s.exit("Not a CSV file")
        else:
            clean(s.argv[1], s.argv[2])

# function to convert input to output
def clean(input, output):
    try:
        with open(input) as input:
            read = c.DictReader(input)
            with open(output, "w") as output:
                head = ["first", "last", "house"]
                write = c.DictWriter(output, fieldnames = head)
                write.writeheader()
                for students in read:
                    last, first = students["name"].split(", ")
                    house = students["house"]
                    write.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        s.exit(f"Could not read {input}")

# calling main function
if __name__ == "__main__":
    main()
