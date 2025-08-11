import sys

works = []
quit = False

while not quit:
    #Quitting system
    if not quit:
        #Functions
        def start_menu():
            print("")
            print("--To Do List--")
            print("Select an option:")
            print("1. Add work")
            print("2. Mark work as completed")
            print("3. Remove work")
            print("4. List of works")
            print("5. Exit")
            print("")
        start_menu()
        #User Input
        userInput = input("= ")
        
        if userInput == "5":
            print("")
            print("Exiting the program.. Goodbye!")
            break
        #Output
        if userInput == "1":
            print("")
            work = input("Add the work: ")
            works.append(work)
            print(f"'{work}' has been added to the list!")

        
