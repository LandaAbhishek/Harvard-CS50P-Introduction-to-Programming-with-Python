# importing validators package
import validators

# function to input & validate user email
def main():
    if validators.email(input("What's your email address? ").strip()):
        print("Valid")
    else:
        print("Invalid")

# calling main function
if __name__ == "__main__":
    main()
