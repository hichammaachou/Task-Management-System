from user import  AuthenticatedUser1
import json
class Task:
    def __init__(self, title, description, due_date, priority,status,task_type):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.task_type = task_type
class WorkTask(Task):
    def __init__(self, title, description, due_date, priority,status, task_type):
        super().__init__(title, description, due_date, priority,status,task_type)
        
class PersonalTask(Task):
    def __init__(self, title, description, due_date, priority,status, task_type):
        super().__init__(title, description, due_date, priority,status, task_type)

class TaskFactory:
    def create_task(self, title,description, due_date, priority,status, task_type):
        if task_type == 'work':
            return WorkTask(title, description, due_date, priority,status,task_type)
        elif task_type == 'personal':
            return PersonalTask(title, description, due_date, priority,status,task_type)

tasks = []
user_tasks = []
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    print('tasks.json not found')        
def usertasks():
    for i in tasks:
        if i['user'] == AuthenticatedUser1._authenticated_user:
            user_tasks.append(i)

def dump_list():
    
    try:
        with open('tasks.json', 'w') as file:
            json.dump(user_tasks, file, indent=2)
    except FileNotFoundError:
        print('tasks.json not found')
        quit()


def add_task():
    title = input('Enter task title: ')
    description = input('Enter task description: ')
    due_date = input('Enter due date (YYYY-MM-DD): ')
    priority = input('Enter priority (low/medium/high): ')
    task_type = input('Enter task type (work/personal): ')
    status = 'uncomplete'

    factory = TaskFactory()
    task = factory.create_task(title, description, due_date, priority,status,task_type)
    user_tasks.append({
        "title" : task.title,
        "description" : task.description,
        "due_date" : task.due_date,
        "priority" : task.priority,
        "status" : task.status,
        "task_type" : task.task_type,
        "user" : AuthenticatedUser1._authenticated_user

    })
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
            dump_list()
            print('Task title updated successfully.')
    print('No tasks with this index!') 

def view_all():
    print('--- All Tasks ---')
    index = 0
    for i in user_tasks:
        index+= 1
        print(f'{index}. Title: {i["title"]} | Description: {i["description"]} | Due Date: {i["due_date"]} | Priority: {i["priority"]} | Status: {i["status"]} | Type: {i["task_type"]}')   

def change_status():
    while True:
        try:
            index = int(input('Enter the index of the completed task: '))  
        except ValueError:
            print('Please enter a number.')   
        else:
            break      
    if user_tasks[index-1]["status"] == "uncomplete":
        user_tasks[index-1]["status"] = "complete"
    elif user_tasks[index-1]["status"] == "complete":
        user_tasks[index-1]["status"] = "uncomplete"
    dump_list()

def delete_task():

    index = int(input('Enter the index of the task: '))
    user_tasks.remove(user_tasks[index-1])
    dump_list()

def view_complete():
    print('--- Completed Tasks ---')
    index = 0
    for i in user_tasks:
        if i["status"] == "complete":
            index+= 1
            print(f'{index}. Title: {i["title"]} | Description: {i["description"]} | Due Date: {i["due_date"]} | Priority: {i["priority"]} | Status: {i["status"]} | Type: {i["task_type"]}')  
def view_uncomplete():
    print('--- Uncompleted Tasks ---')
    index = 0
    for i in user_tasks:
        if i["status"] == "uncomplete":
            index+= 1
            print(f'{index}. Title: {i["title"]} | Description: {i["description"]} | Due Date: {i["due_date"]} | Priority: {i["priority"]} | Status: {i["status"]} | Type: {i["task_type"]}')      
       