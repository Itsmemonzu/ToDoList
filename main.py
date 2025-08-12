import sys
import emoji
import re
from rich import print
from rich.console import Console
# Menu
works = []
quit = False

while not quit:
    #Quitting system
    if not quit:
        #Functions
        def start_menu():
            print("")
            print("[bold][cyan]--To Do List--[/][/]")
            print("[bold][white]Select an option:[/][/]")
            print("")
            print("[green]1.[/] [yellow]Add work[/]")
            print("[green]2.[/] [yellow]Mark work as completed[/]")
            print("[green]3.[/] [yellow]Remove work[/]")
            print("[green]4.[/] [yellow]List of works[/]")
            print("[green]5.[/] [yellow]Exit[/]")
            print("")

        start_menu()

        userInput = input("= ")

        # Exit
        if userInput == "5":
            print("")
            print("[red]Exiting the program.. Goodbye![/]")
            break
        #Output
        if userInput == "1":
            print("")
            work = input("Add the work: ")
            works.append("❌ "+work)
            print("")
            print(f"'{work}' [white]has been added to the list![/]")

        if userInput == "2":

            print("")
            if not works:
                print("[red]No works to mark as completed.[/]")
            else:
                number = 1

                print("[white]Select the work you want to mark as completed:[/]")
                for work in works:
                    print(f"{number}. {work}") 
                    number += 1
                # Input for removing work
                print("")
                try:
                    workDel = int(input("= "))-1
                except:
                    print("")
                    print("[red]You must input a correct number![/]")
                
                # Error: Work is already marked as completed
                if not workDel > len(works)-1 and workDel >= 0 and "✅" in works[workDel]:
                    print("")
                    print("[red]The work is already marked as completed![/]")
                # Marking work as completed
                elif not workDel > len(works)-1 and workDel >= 0 and not "✅" in works[workDel]:
                    workDel = int(workDel)
                    
                    works[workDel] = re.sub(r'❌ ', '✅ ', works[workDel])
                    print("")
                    print(f"'{re.sub(r'✅ ', '', works[workDel])}' [green]has been marked as complete![/] ✅")
                else:
                    print("")
                    print("[red]Wrong input! Please try again.[/]")
        if userInput == "3":

            print("")
            if not works:
                print("[red]No works to remove.[/]")
            else:
                number = 1

                print("[white]Select the work you want to remove:[/]")
                for work in works:
                    print(f"{number}. {work}") 
                    number += 1
                # Input for deleting work
                print("")
                try:
                    workDel = int(input("= "))-1
                except:
                    print("")
                    print("[red]You must input a correct number![/]")
                
                if not workDel > len(works)-1 and workDel >= 0:
                    workDel = int(workDel)
                    if "❌" in works[workDel]:
                        works[workDel] = re.sub(r'❌ ', '', works[workDel])
                    elif "✅" in works[workDel]:
                        works[workDel] = re.sub(r'✅ ', '', works[workDel])
                    print("")
                    print(f"'{works[workDel]}' [red]has been removed![/] 🗑️")
                    works.pop(workDel)
                else:
                    print("")
                    print("[red]Wrong input! Please try again.[/]")
        if userInput == "4":
            if works:
                number = 1
                
                print("")
                print("[white]List of works:[/]")
                for work in works:
                    print(f"{number}. {work}") 
                    number += 1
            else:
                print("")
                print("[red]There are no works to list![/]")


                

        
