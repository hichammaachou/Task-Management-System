from user import  AuthenticatedUser1
import json
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

tasks = []
user_tasks = []
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    print('tasks.json not found')        

for i in tasks:
    if i['user'] == AuthenticatedUser1._authenticated_user:
        user_tasks.append(i)

def dump_list():
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=2)
    except FileNotFoundError:
        print('tasks.json not found')
        quit()


def add_task():
    title = input('Enter task title: ')
    description = input('Enter task description: ')
    due_date = input('Enter due date (YYYY-MM-DD): ')
    priority = input('Enter priority (low/medium/high): ')

    task = Task(title, description, due_date, priority)
    user_tasks.append({
        "title" : task.title,
        "description" : task.description,
        "due_date" : task.due_date,
        "priority" : task.priority,
        "user" : AuthenticatedUser1._authenticated_user

    })  
    tasks.extend(user_tasks)
    dump_list()


    print('Task added successfully.')

def edit_task():
    if user_tasks == []:
        print('You have no tasks to edit!')
        return
    while True:
        try:
            task_index = int(input('Enter the index of the task to edit: '))
        except ValueError:
            print('Please enter a number.')
        else:
            break


    
    for i in range(len(user_tasks)):
        if i == task_index-1:
            new_title = input('Enter new task title: ')
            user_tasks[i]['title'] = new_title
            tasks.extend(user_tasks)
            dump_list()
        elif i != task_index-1:
            print('No tasks with this index!')    
            break