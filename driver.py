from textbook import Textbook


book1 = Textbook("Programming is the best!", "Joe", "Degere", "19", "1234567", 20, 39.99, "Jerry Springer", 2019)
book2 = Textbook("Let's go Skydiving", "Joe", "Degere", "19", "1234789", 25, 24.99, "Jim Carrey", 2019)
# Have to make a menu
menu_choice = 0

while menu_choice != 5:
    print("Please make a choice from the menu:")
    print("1. Add to inventory")
    print("2. Deduct from inventory")
    print("3. Change the price of the book")
    print("4. Change the year the book was published")
    print("5. End program, Have a good day!")

    menu_choice = int(input())
# Break down which book is chosen in each function
    if menu_choice == 1:
        print("Book 1 or Book 2?")
        choice = int(input())
        if choice == 1:
            qty = int(input("How much would you like to add to the inventory?"))
            book1.add_inventory(qty)
            print("The quantity in the inventory is now" + ' ' + str(book1.quantity) + "\n\n")
        else:
            print("The quantity in book 2 is now" + ' ' + str(book2.quantity) + "\n\n")
    elif menu_choice == 2:
        print("Book 1 or 2?")
        choice = int(input())
        if choice == 1:
            qty = int(input("How many would you like to remove?"))
            result = book1.deducting_inventory(qty)
        elif choice == 2:
            qty = int(input("How many would you like to remove?"))
            result = book2.deducting_inventory(qty)
            if result == 0:
                print("The quantity is now 1" + ' ' + str(book1.quantity) + "\n\n")
            else:
                print("You do not have enough to remove from inventory!")

    elif menu_choice == 3:
        print("Book 1 or 2?")
        choice = int(input())
        if choice == 1:
            price = float(input("What would you like the new price to be?"))
            book1.price = price
            print("The price has been changed to" + ' ' + str(book1.price) + "\n\n")
        elif choice == 2:
            price = float(input("What would you like the new price to be?"))
            book2.price = price
            print("The price has been changed to" + ' ' + str(book2.price) + "\n\n")

    elif menu_choice == 4:
        print("Book 1 or 2?")
        choice = int(input())
        if choice == 1:
            year = int(input("What year would you like to change it to, can be past or future."))
            book1.year = year
            print("The year that" + ' ' + book1.title + ' ' + "came out is actually" + ' ' + str(book1.year) + "\n\n")
        elif choice == 2:
            year = int(input("What year would you like to change it to, can be past or future."))
            book2.year = year
            print("The year that" + ' ' + book2.title + ' ' + "came out is actually" + ' ' + str(book2.year) + "\n\n")

    elif menu_choice == 5:
        print("Thank you for your input, have a great day!")
    else:
        print("Error, choose from the menu above!")
