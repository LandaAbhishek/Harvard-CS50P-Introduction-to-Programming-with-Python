camel_case = input("camelcase: ").strip()

for c in camel_case:
    if c.islower():
        print (c, end="")
    else:
        print ("_" + c.lower(), end="")

print()
