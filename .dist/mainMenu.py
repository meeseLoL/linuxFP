#Testing changes

#testing now this too

def addUser():
    #logic
    print("adding a user")

def modUser():
    #logica
    print("modify a user")


def delUser():
    #logic
    print("delete a user")


def viewLog():
    #logic
    print("viewing logs")



def exit():
    #logic
    print("exiting")
    print("maybe")



def w2Update():
    #logic
    print("w2update")




def mainMenu():

    print("\nMain Menu:")
    print("1. Add a user")
    print("2. Modify a user")
    print("3. Delete a user")
    print("4. View logs")
    print("5. Exit")

    choice = input("Enter a number (1-5): ")

    if choice == "1":
        print("You selected to add a user.")
        #call addUser
    elif choice == "2":
        print("You selected to modify a user.")

    elif choice == "3":
        print("You selected to delete a user.")

    elif choice == "4":
        print("You selected to view the logs.")

    elif choice == "5":
        print("Exit")





def main():

    mainMenu()


if name == "main":
    main()


    #test test