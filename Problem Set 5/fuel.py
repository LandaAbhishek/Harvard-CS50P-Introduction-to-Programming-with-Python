# defining main function and input fraction
def main():
    x = get_fraction("Enter the Fraction (X/Y): ")
    print(x)

# setting integers, values and percentage formula
def get_fraction(fraction):
    while True:
        try:
            x, y = input(fraction).split("/")
            x = int(x)
            y = int(y)
            if 0 <= x/y <= 0.1:
                return("E")
            elif 0.9 <= x/y <= 1:
                return("F")
            elif 0.1 < x/y < 0.9:
                return str(round(x/y*100)) + "%"
        # defining errors
        except (ValueError, ZeroDivisionError):
            pass

# calling main function
main()
