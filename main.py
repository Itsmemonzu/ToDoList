"""Copyright (c) 2025 Monzu77

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import sys
import emoji
import re
from rich import print
from rich.console import Console
import os
import platform
import time

# Menu
works = []
quit = False
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
def clear_console():
    # Detect the OS
    current_os = platform.system()
    time.sleep(3)
    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    #Print start_menu
    start_menu()

start_menu()
while not quit:
    #Quitting system
    if not quit:

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
                    correctInput == True
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
    clear_console()
                

        
