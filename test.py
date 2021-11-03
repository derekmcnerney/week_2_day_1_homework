
# Problem 1

def show_instructions():
    print("""Type 'add' to add new items to your shopping cart.
Type 'quit' to exit the program.
Type 'show' to list all items in your shopping cart.""")
    print("<3"*30)


def shopping_cart():
    input('Welcome to Hello Kitty! Press any key to continue. ')
    print("<3"*30)

    cart = []
    done = False
    show_instructions()
    while not done:
        
      

        

        choice = input(
            "What is your choice? Add | Remove | Show | Quit? ").lower()
        if choice == 'add':
            your_item = input(
                "Type in the item you wish to purchase. ").title()

            cart_selection = {
                'Name': your_item,
                
            }
            cart.append(cart_selection)
        elif choice == 'remove':
            your_item = input(
                "Type in the item you wish to remove. ").title()

            cart_selection = {
                '-': your_item,
            }

            cart.remove(cart_selection)

        elif choice == 'show':
            for item in cart:
                print(item)
            input('Press any key to continue ')
        elif choice == 'quit':
            confirm = input('Are you sure you want to quit? Y/N? ').lower()
            if confirm == 'y':
                done = True
                for item in cart:
                        print(item)
            elif confirm == 'n':
                continue

shopping_cart()
    