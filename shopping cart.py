import os
os.system('cls' if os.name == 'nt' else 'clear')


def shopping_cart():

    cart = {}
    a = 1

    while True:
        input_type = input('Would you like to "add", "delete" or "view" items? If you are done type "quit" ')
        
        if input_type.lower() ==  "add" or input_type.lower() == "add items":
            item = input("What would you like to add? ")
            cart[a] = item
            a += 1
            

        elif input_type.lower() == "delete" or input_type.lower() == "delete items":
            if cart == {}:
                print("There are no items in your cart")
            
            else:
                print("item number      item")
                for key, value in cart.items():
                    print(f'{key}                {value}')
                del_item = input("Please enter the item number of the item you would like to delete? ") 
                if int(del_item) not in cart.keys():
                    print("please enter a valid item for your cart")
                else:
                    del cart[int(del_item)]

        elif input_type.lower()  == "view" or input_type.lower() == "view items":
            if cart == {}:
                print("There are no items in your cart")
            else:
                for value in cart.values():
                    print(value)
        
        elif input_type.lower() == "quit":
            for value in cart.values():
                print(value)
            break

        else:
            print("please select a valid option")

shopping_cart()
