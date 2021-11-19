# Function "main_loop" - loops over the whole programme
def main_loop():
    import datetime

    print("\n===== Task Manger =====\n\n")
    dashes = "--------------------------------------------------"

    # Store username of current user
    current_user = ["admin"]

    # function to clear a text file
    def clear_txt(file):
        # Open and clear the text file
        with open(file, "w") as file:
            file.write("")

    # Function to display "main menu"
    def commands():

        space_dashes = "\n" + dashes + "\n"

        # If current user is the admin - show all options
        def admin_commands():
            command = input("""Select one of the following options:
r  --> Register user
a  --> Add task
va --> View all tasks
vm --> View my tasks
d  --> Remove user
e  --> Log out
            
> """).lower()

            if command == "r":
                print(space_dashes)
                reg_user()
            elif command == "a":
                print(space_dashes)
                add_task()
            elif command == "va":
                print(space_dashes)
                view_all()
            elif command == "vm":
                print(space_dashes)
                view_mine()
            elif command == "d":
                print(space_dashes)
                rem_user()
            elif command == "e":
                print(space_dashes)
                main_loop()
            else:
                print(f"\n{command} is not an option.\n")
                print(dashes)
                print()
                commands()

        # If current user is not the admin - show only certain options
        def user_commands():

            command = input("""Select one of the following options:
a  --> Add task
va --> View all tasks
vm --> View my tasks
e  --> exit

> """).lower()

            if command == "a":
                print(space_dashes)
                add_task()
            elif command == "va":
                print(space_dashes)
                view_all()
            elif command == "vm":
                print(space_dashes)
                view_mine()
            elif command == "e":
                print(space_dashes)
                main_loop()
            else:
                print(f"\n{command} is not an option.\n")
                print(dashes)
                print()
                commands()

        if current_user[0] == "admin":
            admin_commands()
        else:
            user_commands()

    # Function to return all usernames
    def get_usernames():

        # List to store all usernames
        usernames = []

        with open("users.txt", "r") as users:
            users = users.read().strip()

        # Make a list of all usernames and passwords
        user_details = users.replace(",", "").replace("\n", " ").split(" ")

        # For loop to pick out all usernames from user_details
        for user in user_details:
            if user_details.index(user) % 2 == 0:
                usernames.append(user)

        return usernames

    # Function to return all passwords
    def get_passwords():

        # List to store all passwords
        passwords = []

        with open("users.txt", "r") as users:
            users = users.read().strip()

        # Make a list of all usernames and passwords
        user_details = users.replace(",", "").replace("\n", " ").split(" ")

        # For loop to pick out all passwords from user_details
        for password in user_details:
            if user_details.index(password) % 2 != 0:
                passwords.append(password)

        return passwords

    # Function to return list of all tasks
    def get_tasks():

        # Read contents from "tasks.txt" and store list of tasks in tasks_list
        with open("tasks.txt", "r") as tasks:
            tasks = tasks.read().strip()

        tasks_list = tasks.split("\n")

        return tasks_list

    # Functions to allow users to login
    def login():

        entry = False
        while not entry:
            # Get list of usernames and passwords
            usernames = get_usernames()
            passwords = get_passwords()

            # Request username and password
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            # Check if username and passwords match
            if username not in usernames or password != passwords[usernames.index(username)]:
                print("\nIncorrect username or password.\n")
            else:
                current_user.clear()
                current_user.append(username)

                print(f"\nWelcome back {username}.\n")
                print(dashes)
                print()
                entry = True

        commands()

    # Function to register a new user
    def reg_user():

        # Get list of usernames and passwords
        usernames = get_usernames()
        passwords = get_passwords()

        while True:
            # Request new username
            new_username = input("Username: ")

            # Check if username already taken
            if new_username in usernames:
                print(f"\n{new_username} is already registered.\n")
            else:
                while True:
                    # Request password and password confirmation
                    new_password = input("Password: ")
                    new_password_confirm = input("Confirm password: ")

                    # Check if both password are the same
                    if new_password != new_password_confirm:
                        print("\nPassword do not match.\n")
                    else:
                        break
                break

        # Add new username and password to the list
        usernames.append(new_username)
        passwords.append(new_password)

        # Clear users.txt
        clear_txt("users.txt")
        # Append new username and password to users.txt
        for username in usernames:
            with open("users.txt", "a") as users:
                users.write(f"{username}, {passwords[usernames.index(username)]}\n")

        print(f"\n{new_username} has been registered.\n")
        print(dashes)
        print()

        commands()

    # Function to remove a user
    def rem_user():

        # Get list of usernames, passwords and tasks
        usernames = get_usernames()
        passwords = get_passwords()
        tasks = get_tasks()

        print("WARNING: After removing a user, all tasks assigned to him/her will be deleted.\n")

        while True:
            # Request username of user being removed
            user = input("Username of user being removed: ")

            # Check if username exists
            if user not in usernames:
                print(f"\n{user} does not exist.\n")
            elif user == "admin":
                print("\nYou cannot remove yourself.\n")
            else:
                break

        # Remove all tasks assigned to the removed user
        for task in tasks:
            details = task.split(",")
            if user in details[0]:
                tasks.remove(task)

        # Clear tasks.txt
        clear_txt("tasks.txt")
        for task in tasks:
            with open("tasks.txt", "a") as tasks:
                tasks.write(f"{task}\n")

        # Remove the user's password and username
        passwords.pop(usernames.index(user))
        usernames.remove(user)

        # Clear users.txt
        clear_txt("users.txt")
        for username in usernames:
            with open("users.txt", "a") as users:
                users.write(f"{username}, {passwords[usernames.index(username)]}\n")

        print(f"\nUser {user} successfully removed.\n")
        print(dashes)
        print()
        commands()

    # Function to add new task
    def add_task():

        today = datetime.datetime.now()

        # Get list of tasks and usernames
        tasks_list = get_tasks()
        users = get_usernames()

        while True:
            # Request assigned user
            assigned_user = input("Assigned to: ")

            # Check if assigned user exists
            if assigned_user not in users:
                print(f"\n{assigned_user} has not been registered.\n")
            else:
                break

        # Request task details
        task = input("Task: ")
        date_assigned = today.strftime("%Y/%m/%d")

        while True:
            due_date = input("Due date (y/m/d): ")
            try:
                test_date = datetime.datetime.strptime(due_date, "%Y/%m/%d")
                break
            except:
                print()
                print("Please enter date in correct format.\n")

        description = input("Task description: ")

        tasks_list.append(f"Assigned to:       {assigned_user},Task:              {task},"
                          f"Date assigned:     {date_assigned},Due date:          {due_date},"
                          f"Task description:  {description},Task completed:    No")

        # Clear tasks.txt
        clear_txt("tasks.txt")
        # Append each task to tasks.txt
        for task in tasks_list:
            with open("tasks.txt", "a") as tasks:
                tasks.write(f"{task}\n")

        print("\nTask added")
        print(f"\n{dashes}\n")

        commands()

    # Function to view all tasks
    def view_all():

        # Get a list of all tasks from tasks.txt
        tasks_list = get_tasks()

        if len(tasks_list) == 0 or len(tasks_list[0]) < 3:
            print("There are no tasks.\n")
            print(dashes)
            print()
        else:
            # Use string handling to display all tasks in an easy-to-read format
            tasks_string = ""

            for task in tasks_list:
                task_details = task.split(",")
                for detail in task_details:
                    tasks_string += detail + "\n"
                tasks_string += "\n\n" + "**************************************************" + "\n\n"

            print(tasks_string)
            print(dashes)
            print()

        commands()

    # Function to view current users tasks
    def view_mine():

        # Get list of all tasks
        tasks_list = get_tasks()

        # Create a list with all tasks assigned to current user
        my_tasks = []
        for task in tasks_list:
            task_details = task.split(",")
            if current_user[0] in task_details[0]:
                my_tasks.append(task.replace(",", "\n"))

        # Display tasks in an easy-to-read format
        if len(my_tasks) == 0:
            print("You do not have any tasks.")
        else:
            count = 1
            my_tasks_string = ""
            print()
            for task in my_tasks:
                my_tasks_string += f"{count})\n{task}\n\n"
                count += 1

            print(my_tasks_string)

        print()
        print(dashes)
        print()

        commands()

    login()


main_loop()
