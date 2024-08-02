from employees import addEmployee, modifyEmployee, deleteEmployee, viewLogs, display_database
import os

def mainMenu():
    while True:
        print("\nMain Menu:")
        print("1. Add a user")
        print("2. Modify a user")
        print("3. Delete a user")
        print("4. Display database")
        print("5. View logs")
        print("6. Exit")

        choice = input("Enter a number (1-6): ")

        if choice == "1":
            print("You selected to add a user.")
            addEmployee()
        elif choice == "2":
            print("You selected to modify a user.")
            modifyEmployee()
        elif choice == "3":
            print("You selected to delete a user.")
            deleteEmployee()
        elif choice == "4":
            print("You selected to display the database.")
            display_database()
        elif choice == "5":
            print("You selected to view the logs.")
            viewLogs()
        elif choice == "6":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    mainMenu()
