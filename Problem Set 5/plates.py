# input plate
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# conditions for valid and invalid
def is_valid(s):
    if s[0:2].isalpha() and \
    2 <=  len(s) <= 6 and \
    first_not_zero(s) and \
    number_at_end(s) and \
    check_punctuation(s):
        return True
    else:
        return False

# first position should not be zero
def first_not_zero(n):
    for char in n:
        if char.isdigit():
            break
    if char != "0":
        return True

# should end with number
def number_at_end(num):
    if num.isalpha():
        return True
    else:
        first_digit = None
        for i in num:
            if i.isdigit():
                first_digit = i
                break
        _, end = num.split(first_digit, 1)
        for j in end:
            if j.isalpha():
                return False
    return True

# no punctuations allowed
def check_punctuation(p):
    import string
    for char in p:
        if char in string.punctuation:
            return False
    return True

# calling main function
main()
