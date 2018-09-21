
# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = []



def create_task(task):
    if task in todo_list:
        return "task and exit"
    else:
        todo_list.append(task)
        return "{} has been added".format(task)


# Write a function deletes a task


def delete_task(task):
    if task not in todo_list:
        return "task not todolist"
        removed = todo_list.pop(todo_list.index(task))
        return"{} has been removed".format(removed)


# Write a function that marks a task finished

pass
def mark_as_finished(task):
      if task in todo_list:
        todo_list.append ()
      else:
        print ("add list")

# Write a function deletes all tasks


def delete_all_tasks():
      if not todo_list:
          return "todolist is empty"
      else:
       todo_list.clear()
    
