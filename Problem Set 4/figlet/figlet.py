# importing libraries
import sys
import random
from pyfiglet import Figlet

# assigning values
figlet = Figlet()
argv1 = ["-f", "--font"]
font1 = random.choice(figlet.getFonts())
style = figlet.getFonts()

# setting text style
def main():
    if len(sys.argv) < 2:
        font = font1
        figletize("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in style:
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        sys.exit("Invalid Use")

# rendering text
def figletize(Text, font):
    text = input(Text)
    figlet.setFont(font=font)
    print(f"Output:\n{figlet.renderText(text)}")

# calling main function
main()
