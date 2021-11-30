

groceries1 = []
while len(groceries1) < 3:
    item = input(f'Enter an item for your grocery list: ')
    groceries1.append(item)

groceries2 = []
while len(groceries2) < 3:
    item = input(f'Enter an item for your grocery list: ')
    groceries2.append(item)

#combine groceries

# or groceries1.extend(groceries2)
groceries3 = groceries1 + groceries2

# print the combined grocery list 
indexes = range(len(groceries3))
for i in indexes:
    item= groceries3[i]
    print(f'{i}: {item}')

# prompt the user for the indes of the item to replace
index_num = int(input('Which number item do you need to replace? '))

# propt the user for the new item
new_item = input('What do you need to add? ')

# replace the tiem at that indes with the new item
groceries3[index_num] = new_item

# print the updated combined list
print(groceries3)