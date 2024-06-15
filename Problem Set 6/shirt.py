# importing libraries
import os as o
import sys as s
from PIL import Image, ImageOps

# function to validate and process image
def main():
    if len(s.argv) < 3:
        s.exit("Too few command-line arguments")
    elif len(s.argv) > 3:
        s.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        input = o.path.splitext(s.argv[1])
        output = o.path.splitext(s.argv[2])
        if output[1].lower() not in format:
            s.exit("Invalid output")
        elif input[1].lower() != output[1].lower():
            s.exit("Input and output have different extensions")
        else:
            photo_edit(s.argv[1], s.argv[2])

# function to overlay image onto shirt
def photo_edit(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_crop = ImageOps.fit(input, shirt.size)
            input_crop.paste(shirt, mask = shirt)
            input_crop.save(output)
    except FileNotFoundError:
        s.exit(f"Input does not exist")

# calling main function
if __name__ == "__main__":
    main()
