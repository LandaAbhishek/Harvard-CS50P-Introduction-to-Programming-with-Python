# importing libraries
import sys
import json
import requests

# bitcoin number
def main():
    if len(sys.argv) == 2:
        try:
            price = float(sys.argv[1])
            print(btc_price(price))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

# amount and quantity
def btc_price(quantity):
    try:
        output = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = output.json()
        rate = result["bpi"]["USD"]["rate_float"]
        amount = rate * quantity
        return f"${amount:,.4f}"
    except requests.RequestException:
        return None

# calling main
main()
