tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasks
def list_tasks_notcomplited(task, completed):
    task_notComplited = None
    for task in tasks:
        if task["completed"] == False:
            task_notComplited = task
    return task_notComplited
print(list_tasks_notcomplited(tasks, False))

# Print a list of completed tasks
def list_tasks_complited(task, completed):
    task_complited = None
    for task in tasks:
        if task["completed"] == True:
            task_complited = task
    return task_complited
print(list_tasks_complited(tasks, True))

# Print a list of all task description

# Print a list of tasks where time_taken is at least a given time

# Print any task with a given description


# Extension
# Given a description update that task to mark it as complete.

# Add a task to the list