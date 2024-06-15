# importing libraries
import re

# function to print IP address
def main():
    ip_address = input("IPv4 Address: ")
    validation_result = validate(ip_address)
    if validation_result:
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")

# function to validate IP address
def validate(ip):

    # Check format using regular expression
    if not re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False

    octets = ip.split(".")
    if len(octets) != 4:
        return False

    for octet in octets:
        try:
            # Validate each octet is within 0-255 range
            number = int(octet)
            if not 0 <= number <= 255:
                return False
        except ValueError:
            return False  # Handle non-numeric octet values

    return True

# calling main function
if __name__ == "__main__":
    main()
