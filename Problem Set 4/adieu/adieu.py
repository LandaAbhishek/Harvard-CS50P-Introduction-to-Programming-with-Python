# importing libraries
import inflect
p = inflect.engine()
names_list = []

# input name
while True:
    try:
        name = input("Name: ").title().strip()
        names_list.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(names_list))
        break
