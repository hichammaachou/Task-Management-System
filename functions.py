from user import AuthenticatedUser1
def menu():
    print(f'''Welcome, {AuthenticatedUser1._authenticated_user}!

1. Add Task
2. Edit Task
3. Mark Task as Complete/Uncomplete
4. Delete Task
5. View All Tasks
6. View Completed Tasks
7. View Uncompleted Tasks
8. Menu
9. Sign Out

    ''')