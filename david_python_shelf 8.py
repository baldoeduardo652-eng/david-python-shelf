cart = []

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Show Cart")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # SHOW CART
    if choice == "1":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("\n--- Cart Items ---")
            for index, item in enumerate(cart):
                print(f"{index+1}. {item['name']} - Quantity: {item['quantity']}")

    # ADD ITEM
    elif choice == "2":
        item_name = input("Enter item name: ")
        try:
            quantity = int(input("Enter quantity: "))
            cart.append({"name": item_name, "quantity": quantity})
            print("Item added to cart successfully.")
        except ValueError:
            print("Quantity must be a number.")

    # UPDATE ITEM
    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty. Nothing to update.")
        else:
            print("\n--- Cart Items ---")
            for index, item in enumerate(cart):
                print(f"{index+1}. {item['name']} - Quantity: {item['quantity']}")

            try:
                item_index = int(input("Enter item number to update: ")) - 1
                if 0 <= item_index < len(cart):
                    new_quantity = int(input("Enter new quantity: "))
                    cart[item_index]["quantity"] = new_quantity
                    print("Item quantity updated successfully.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

    # REMOVE ITEM
    elif choice == "4":
        if len(cart) == 0:
            print("Cart is empty. Nothing to remove.")
        else:
            print("\n--- Cart Items ---")
            for index, item in enumerate(cart):
                print(f"{index+1}. {item['name']} - Quantity: {item['quantity']}")

            try:
                item_index = int(input("Enter item number to remove: ")) - 1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"{removed_item['name']} removed from cart.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

    # EXIT
    elif choice == "5":
        print("Exiting Shopping Cart. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-5.")

 
