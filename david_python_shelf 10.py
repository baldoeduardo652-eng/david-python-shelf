filename = "message.txt"

try:
    with open(filename, "x") as file:
        print("File created successfully.")
except FileExistsError:
    print("Error: File already exists.")

# Step 2: Menu-driven program
while True:
    print("\n=== Simple Messaging App ===")
    print("1. Send a message")
    print("2. View all messages")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        # Append message
        message = input("Enter your message: ")
        try:
            with open(filename, "a") as file:
                file.write(message + "\n")
            print("Message saved successfully.")
        except Exception as e:
            print("Error writing to file:", e)

    elif choice == "2":
        # Read messages
        try:
            with open(filename, "r") as file:
                messages = file.readlines()
                if messages:
                    print("\n--- Messages ---")
                    for msg in messages:
                        print(msg.strip())
                else:
                    print("No messages found.")
        except FileNotFoundError:
            print("Error: File does not exist.")
        except Exception as e:
            print("Error reading file:", e)

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select 1-3.")