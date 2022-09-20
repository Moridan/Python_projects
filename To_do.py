exit = False
to_do = []

while exit == False:
    choice = input("Type 'Add' to add a To Do. Type 'Remove' to remove a To Do. Type 'Edit' to edit a to do. Type 'View' to view your To Do's. Type 'Exit' to exit: ")
    if choice == "Add":
        to_do.append(input("What would you like to add?: "))
    elif choice == "Remove":
        to_do.remove(input("Type the item do you want to remove?: "))    
    elif choice == "Edit":
        #een input met de vraag welke entry gewijzigd moet worden
        #een input met de vraag wat de nieuwe waarde moet zijn voor die entry
        
        old_to_do = input("which item do you want to edit: ")
        new_to_do = input("What do you name this To Do: ")
        index = to_do.index(old_to_do)
        to_do[index] = new_to_do

    elif choice == "View":
        for choice in to_do:
            print(choice)
    elif choice == "Exit":
        exit = True
