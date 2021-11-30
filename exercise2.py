

groceries1 = []
while len(groceries1) < 3:
    item = input(f'Enter an item for your grocery list: ')
    groceries1.append(item)

groceries2 = []
while len(groceries2) < 3:
    item = input(f'Enter an item for your grocery list: ')
    groceries2.append(item)

#combine groceries

groceries1.extend(groceries2)
# or groceries3 = groceries1 + groceries2