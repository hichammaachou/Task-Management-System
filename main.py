from user import User, AuthenticatedUser1,sign_in,sign_up, user_data
from task import Task, add_task, edit_task, dump_list,usertasks,view_all,change_status,delete_task, view_complete,view_uncomplete
from functions import menu
import json
print("""Welcome to the Task Management System!

1. Sign Up
2. Sign In
3. Exit

    """)

while True:
    
    login_choice = input("Enter your choice:")
    if login_choice == "1":

        sign_up()
    elif login_choice == "2":
        if sign_in() == True:
            break

    elif login_choice == "3":
        print("Goodbye! Have a great day!")
        quit()
    else:
        print("Invalid option! Pick again")

usertasks()
menu()
while True:
    
    
    menu_choice = input('Enter your choice: ')
    if menu_choice == "1":
        add_task()
    elif menu_choice == "2":
        edit_task()
    elif menu_choice == "3":
        change_status()
    elif menu_choice == "4":
        delete_task()
    elif menu_choice == "5":
        view_all()
    elif menu_choice == "6":
        view_complete()
    elif menu_choice == "7":
        view_uncomplete()
    elif menu_choice == "8":
        menu()
    elif menu_choice == "9":
        quit()
    else:
        print('Invalid option!')    