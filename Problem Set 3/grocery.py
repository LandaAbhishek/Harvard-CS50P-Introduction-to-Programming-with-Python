# grocery list
grocery = []

# input grocery items
while True:
    try:
        items = input().strip().upper()
        grocery.append(items)
    except EOFError:
        break
print()

# import numpy to calculate quantity
import numpy as np
values, keys = np.unique(grocery, return_counts=True)
item_list = {values[i]: keys[i] for i in range(len(values))}
for item in item_list:
    print(item_list[item], item)
