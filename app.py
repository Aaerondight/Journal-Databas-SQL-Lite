from database import *

menu = """Please select an option:
1) Add new entry pattern
2) View entries
3) Exit

Selection: """

welcome = "Welcome to the diary!"

print(welcome)

def prompt_add_entry():
    content = input("What have you learned today? ")
    date = input("Enter the date: ")
    add_entry(content, date)

def prompt_view_entries(entries):
    entries = get_entries()

    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n")

while (user_input := input(menu)) != "3":

    if user_input == "1":
        prompt_add_entry()
    elif user_input == "2":
        prompt_view_entries(get_entries())
    else:
        print("Wrong Input")



