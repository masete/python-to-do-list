from tasks import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished
from accounts import accounts, add_account, login


options = """
   1. creating a task
   2. deleting a task
   3. deleting all tasks
   4. Marking a task finished
   0. To exit the program.
   """


def controller():
    """
        Allows a user to choose from a wide range of tasks and performs a task in response to
        the selected option.
    """
    print(f"{options}")
    selection = int(input("Make a selection: "))

    if selection and selection == 1:
        task = str(input("Enter a task: "))
        if task and task != " ":
            create_task(task)
            print("Task successfully created.")
            print("You currently have: {} items in your todo-list".format(len(todo_list)))

    elif selection and selection == 2:
        task = input("Enter task to delete. ")
        delete_task(task)

    elif selection and selection == 3:
        delete_all_tasks(todo_list)
        print("All tasks have been deleted. ")
        print("{} items in todo-list:".format(len(todo_list)))

    elif selection and selection == 4:
        task = input("Enter task to Finish: ")
        mark_as_finished(task)

    elif selection == 0:
        quit()

    else:
        controller()

    controller()


if __name__ == "__main__":
        name = input("Enter username ")

        while name in accounts:
            password = input("Enter password ")

            # login
            login(name, password)
            print("Welcome {}".format(name))
            controller()
            break
    # create account
        password = input("Choose password ")
        add_account(name, password)
        controller()
