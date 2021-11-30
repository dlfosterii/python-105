
# To fill the grocery list:
# - prompt until they enter empty string

groceries1 = []
while True:
    item = input(f'Enter an item for your grocery list: ')
    #if they enter an empty string "break"
    if item == '':
        break
    groceries1.append(item)

groceries2 = []
while True:
    item = input(f'Enter some more items for your grocery list: ')
    if item == '':
        break
    groceries2.append(item)

#combine groceries

# or groceries1.extend(groceries2)
groceries3 = groceries1 + groceries2

# print the combined grocery list 
# # Show them the list
# - that is, print() it!
indexes = range(len(groceries3))
for i in indexes:
    item= groceries3[i]
    print(f'{i}: {item}')

# prompt the user for the index of the item to replace
# # Give them a chance to replace stuff in list
# - prompt for a subset of items to replace
#   - if start and end same, replace 1
#   - if different, replace with a list
#         - (prompt until they enter empty string)
index_num0 = input('Do you want to edit your list?(y/n) ')
if index_num0 == 'y':
    index_num1 = int(input('Which number item do you want to start changes with? '))
    index_num2 = int(input('Which number item do you want to END changes with? '))
else:
    indexes = range(len(groceries3))
    for i in indexes:
        item= groceries3[i]
        print(f'{i}: {item}')


# propt the user for the new item
new_item = input('What do you need to add? ')

# replace the tiem at that indes with the new item
groceries3[index_num] = new_item

# print the updated combined list
print(groceries3)



# # Come back to the classroom at 2pm to discuss!
# # To fill the grocery list:
# - prompt until they enter empty string
# # Show them the list
# - that is, print() it!
# # Give them a chance to replace stuff in list
# - prompt for a subset of items to replace
#   - if start and end same, replace 1
#   - if different, replace with a list
#         - (prompt until they enter empty string)