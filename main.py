from user import User, AuthenticatedUser1,sign_in,sign_up, user_data

import json
print("""Welcome to the Task Management System!

1. Sign Up
2. Sign In
3. Exit

    """)
loop = True

while True:
    
    login_choice = input("Enter your choice:")
    if login_choice == "1":

        sign_up()
    elif login_choice == "2":
        print(user_data)
        if sign_in() == True:
            break

    elif login_choice == "3":
        print("Goodbye! Have a great day!")
        quit()
    else:
        print("Invalid option! Pick again")

while True:
    print(f'''Welcome, {AuthenticatedUser1._authenticated_user}!

1. Add Task
2. Edit Task
3. Mark Task as Complete/Uncomplete
4. Delete Task
5. View All Tasks
6. View Completed Tasks
7. View Uncompleted Tasks
8. View Task Statistics
9. Sign Out

    ''')