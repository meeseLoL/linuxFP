#Contributors: Dann, Justin, Lloyd

from employees import addEmployee, modifyEmployee, deleteEmployee, viewLogs, display_database
import os
import subprocess
import webbrowser
import display_db


def run_awk_script():
    keyword = input("Enter keyword to filter logs: ")
    if keyword:
        subprocess.run(['awk', f'/{keyword}/', 'logs.txt'])
    else:
        print("No keyword provided.")


def run_perl_script():
    try:
        subprocess.run(['perl', 'process_logs.pl'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the Perl script: {e}")

# Displays the menu
def mainMenu():
    while True:
        print("\nMain Menu:")
        print("1. Add a user")
        print("2. Modify a user")
        print("3. Delete a user")
        print("4. Display database")
        print("5. View logs")
        print("6. Filter logs by keyword")
        print("7. View # of log entries")
        print("8. Exit")

        choice = input("Enter a number (1-8): ")

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
            display_database() # Displays the data base in the terminal
            subprocess.Popen(['python', 'app.py']) # executes app.py
            webbrowser.open('http://127.0.0.1:5000') # opens the browser to view the employee database
        elif choice == "5":
            print("You selected to view the logs.")
            viewLogs()
        elif choice == "6":
            print("You selected to filter the logs by a keyword, please enter a keyword: ")
            run_awk_script()
        elif choice == "7":
            print("You selected to View # of log entries.")
            run_perl_script()
        elif choice == "8":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    mainMenu()
