# importing packages
from datetime import date
import inflect as inf
import sys as s
import operator as op

# function to input date of birth
def main():
    try:
        dob = input("Date of Birth: ")
        # to validate date of birth in iso format
        diff = op.sub(date.today(), date.fromisoformat(dob))
        print(convert(diff.days))
    except ValueError:
        s.exit("Invalid date")

# function to convert minuts from numbers to words
def convert(time):
    p = inf.engine()
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

# calling main function
if __name__ == "__main__":
    main()
