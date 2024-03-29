'''
Instrutions:


The starter code provides you with the main menu for a command-line
based grocery list application.

The user should be able to add, update, and remove items.

Small exercise ------------------------------------------------
Using this starter code, you're going to combine the pieces of code
you've written so far to create the functionality for each action (either 
adding, updating, or removing an item).

Each time the user adds, updates, or deletes an item, they should see the main menu again.

Medium exercise ------------------------------------------------
For each sub-menu, show the user another menu with choices for that section of the application.
For example, when Removing Items, show the user this menu:

1. Print items
2. Delete an item
3. Delete multiple items
4. Return to main menu

If they enter "2", prompt them for the index of the item to delete.
If they enter "3", prompt them for a start index and an end index for the slice to delete.

After deleting, show them the "delete" menu again.
To return to the main menu, the user needs to enter "4" at the prompt.

Large exercise ------------------------------------------------
Add a second array that stores whether or not each grocery list item has been obtained.
Every time you add or remove an item, you need to add to or remove from this second list.

Add an additional main menu option for changing the status of any grocery list item.

Update the "Print Items" output so that it shows whether or not an item has been obtained.
'''


groceries = []
groceries = ['milk', 'cheese', 'coffee', 'chips', 'salsa', 'steak', 'potatoes', 'lettus']
main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''
print('Welcome to the grocery list app! Please select from the following chices. ')
print(main_menu)


while True:
    menu_choice = int(input(main_menu))

    # Add if/else statements for each menu item
    if menu_choice == 1: #print the list
        indexes = range(len(groceries))
        for i in indexes:
            item = groceries[i]
            print(f'{i}: {item}')
    elif menu_choice == 2: #add items to the list
        # Prompt for a new item until the just hit Enter
        while True:
            item = input('What do you need from the store? ')
            if item == '':
                break
            groceries.append(item)
    elif menu_choice == 3: #removing groups of items
        indexes = range(len(groceries))
        for i in indexes:
            item = groceries[i]
            print(f'{i}: {item}')
        # Give them the chance to replace 
        start_index_to_replace = int(input('What start index to replace? '))
        end_index_to_replace = int(input('What end index to replace? '))

        if start_index_to_replace == end_index_to_replace:
            # Prompt the user for the new item
            new_item = input('What is the new item? ')

            # - replace the item at that index with the new item
            groceries[start_index_to_replace] = new_item
        else:
            # gather replacements
            replacements = []
            while True:
                new_item = input('What is the new item? ')
                if new_item == '':
                    break
                replacements.append(new_item)
            groceries[start_index_to_replace:end_index_to_replace] = replacements
    elif menu_choice == 4: #deleting items
        indexes = range(len(groceries))
        for i in indexes:
            item = groceries[i]
            print(f'{i}: {item}')
        item_2b_deleted = int(input('Enter the item number to be deleted. '))
        del groceries[item_2b_deleted]
    elif menu_choice == 5: #quit
        break

# - print the updated list and end
for i in indexes:
    item = groceries[i]
    print(f'{i}: {item}')

print('Thank you for using the grocery list app!')