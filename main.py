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

from rich import print
import os
import platform
import time
from tinydb import TinyDB, Query
from tinydb.operations import set


# Database query
database = TinyDB('db.json')
Work = Query()

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
    time.sleep(1.5)
    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    start_menu()

def run_function():
    start_menu()

    while True:
        user_input = input("= ")

        # Exit
        if user_input == "5":
            print("")
            print("[red]Exiting the program.. Goodbye![/]")
            break

        # Output
        elif user_input == "1":
            print("")
            work = input("Add the work: ").strip()

            work_is_here = False
            for item in database.all():
                if item['work'].lower() == work.lower() and not work_is_here:
                    work_is_here = True

            if not work_is_here:
                database.insert({'work': work, 'completed': False})
                print("")
                print(f"'{work}' [white]has been added to the list![/]")
            else:
                print("[red]This is already in the list![/]")

        elif user_input == "2":
            print("")

            if not database:
                print("[red]No works to mark as completed.[/]")
            else:
                number = 1

                print("[white]Select the work you want to mark as completed:[/]")

                # show all
                for item in database:
                    emoji = '❌' if item['completed'] == False else '✅'

                    print(f"{number}. {emoji} {item['work']}")
                    number += 1

                # input for removing work
                print("")
                work_del = 0  # the work to complete

                # check for correct input
                try:
                    work_del = int(input("= "))-1
                except:
                    print("")
                    print("[red]You must input a correct number![/]")

                # Error: Work is already marked as completed
                if not work_del > len(database)-1 and work_del >= 0:
                    item = database.all()[work_del]

                    if item['completed']:
                        print("")
                        print("[red]The work is already marked as completed![/]")

                    else:
                        database.update(set('completed', True), Work.work == item['work'])
                        print("")
                        print("[green] Work marked as completed![/]")
                else:
                    print("")
                    print("[red]Wrong input! Please try again.[/]")

        elif user_input == "3":
            print("")
            if not database:
                print("[red]No works to remove.[/]")
            else:
                number = 1

                print("[white]Select the work you want to remove:[/]")
                for item in database:
                    emoji = '❌' if item['completed'] == False else '✅'
                    print(f"{number}. {emoji} {item['work']}")
                    number += 1

                # Input for deleting work
                print("")
                work_del = 0
                try:
                    work_del = int(input("= "))-1
                except:
                    print("")
                    print("[red]You must input a correct number![/]")

                if not work_del > len(database)-1 and work_del >= 0:
                    item = database.all()[work_del]
                    print("")
                    database.remove(Work.work == item['work'])
                    print("[red]Work has been removed![/] 🗑️")
                else:
                    print("")
                    print("[red]Wrong input! Please try again.[/]")

        elif user_input == "4":
            if database:
                number = 1

                print("")
                print("[bold][cyan]--List of works--[/][/]")
                for item in database:
                    emoji = '❌' if item['completed'] == False else '✅'
                    print(f"{number}. {emoji} {item['work']}")
                    number += 1
            else:
                print("")
                print("[red]There are no works to list![/]")

        else:
            print("[red]Invalid command![/]")

        if user_input not in ["4"]:
            clear_console()

# main running program
try:
    run_function()
except KeyboardInterrupt:
    print("\n[red]Program closing.[/]")
