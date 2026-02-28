user = []

while True:
    print("1. show user")
    print("2.add user")
    print("3.update user")
    print("4.delete user")
    print("5.exit")
    
    choice = input("enter your choice (1-5): ")
    
    if choice == "1":
        if len(user) == 0:
            print("no user found.")
        else:
            print("---userlist---")
            for index, u in enumerate(user):
                print(f"{index+1}.{u}")
    
    elif choice == "2":
        new_user = input("enter new user name: ")
        user.append(new_user)
        print("user add sucessfully.")
    
    elif choice == "3":
        if len(user) == 0:
            print("no users to update")
        else:
            for index, u in enumerate(user):
                print(f"{index+1}.{u}")
            
            try:
                user_index = int(input("enter user number to update: ")) - 1
                if 0 <= user_index < len(user):
                    updated_name = input("enter new name: ")
                    user[user_index] = updated_name
                    print("user updated sucessfully.")
                else:
                    print("invalid user number")
            except ValueError:
                print("please enter a valid number")
    
    elif choice == "4":
        if len(user) == 0:
            print("no users to delete")
        else:
            for index, u in enumerate(user):
                print(f"{index + 1}.{u}")
            try:
                user_index = int(input("enter user number to delete: ")) - 1
                if 0 <= user_index < len(user):
                    deleted_user = user.pop(user_index)
                    print(f"{deleted_user} deleted successfully")
                else:
                    print("Invalid user number.")
            except ValueError:
                print("please enter a valid number.")
    
    elif choice == "5":
        print("Exiting program")
        break


 