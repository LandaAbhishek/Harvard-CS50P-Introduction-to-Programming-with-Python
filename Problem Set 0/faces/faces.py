# define function to convert text
def main():
    result = convert(input())
    print(result)

# define function to replace symbols with emoji
def convert(text):
    text = text.replace(":)", '🙂').replace(":(", '🙁')
    return text

main()

