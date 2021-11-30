#prompt user for a single grocery item
#   -append it toa the 'grocieres' list
#in an infinate loop, prompt the user, prompt the user for an item
#   -append the item to the list
#   -print()the list after you add the item

#to exit out of the loopm oress Ctrl-C
groceries = []

while True:
    item = input(f'Enter an item for your grocery list: ')
    groceries.append(item)

    print(groceries)
