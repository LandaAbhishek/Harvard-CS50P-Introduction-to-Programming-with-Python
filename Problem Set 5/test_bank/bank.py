# input greatings
greating = input("Greatings: ").lower().strip()

# outcome for greatings
if greating.startswith("hello"):
    print("$0")
elif greating.startswith("h"):
    print("$20")
else:
    print("$100")
