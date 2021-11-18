# Function "main_loop" - loops over the whole programme
def main_loop():

    print("\n===== Task Manger =====\n\n")
    dashes = "--------------------------------------------------"

    # Store username of current user
    current_user = []

    # Function to return all usernames
    def get_usernames():

        # List to store all usernames
        usernames = []

        with open("users.txt", "r") as users:
            users = users.read()

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
            users = users.read()

        # Make a list of all usernames and passwords
        user_details = users.replace(",", "").replace("\n", " ").split(" ")

        # For loop to pick out all passwords from user_details
        for password in user_details:
            if user_details.index(password) % 2 != 0:
                passwords.append(password)

        return passwords

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

                print(f"\nWelcome back {username}\n")
                print(dashes)
                entry = True

    # Function to register a new user
    def reg_user():

        # Get list of all users
        usernames = get_usernames()

        while True:
            # Request new username
            new_username = input("Username: ")

            # Check if username already taken
            if new_username in usernames:
                print(f"{new_username} is already registered.\n")
            else:
                while True:
                    # Request password and password confirmation
                    new_password = input("Password: ")
                    new_password_confirm = input("Confirm password: ")

                    # Check if both password are the same
                    if new_password != new_password_confirm:
                        print("Password do not match.\n")
                    else:
                        break
                break

        # Append new user details to users.txt
        with open("users.txt", "a") as users:
            users.write(f"\n{new_username}, {new_password}")

        print(f"\n{new_username} has been registered.\n")
        print(dashes)

    # Function to add new task
    def add_task():

        # Get list of all usernames
        users = get_usernames()

        while True:
            # Request assigned user
            assigned_user = input("Assigned to: ")

            # Check if assigned user exists
            if assigned_user not in users:
                print(f"{assigned_user} has not been registered.\n")
            else:
                break

        # Request task details
        task = input("Task: ")
        date_assigned = input("Date assigned (d/m/y): ")
        due_date = input("Due date (d/m/y): ")
        description = input("Task description: ")

        # Append task details to tasks.txt
        with open("tasks.txt", "a") as tasks:
            tasks.write(f"\nAssigned to:       {assigned_user},Task:              {task},"
                        f"Date assigned:     {date_assigned},Due date:          {due_date},"
                        f"Task description:  {description},Task completed:    No")

        print("\nTask added")
        print(f"{dashes}\n")

    # Function to view all tasks
    def view_all():

        # Get a list of all tasks from tasks.txt
        with open("tasks.txt", "r") as tasks:
            tasks = tasks.read().strip()

        tasks_list = tasks.split("\n")

        # Use string handling to display all tasks in an easy-to-read format
        tasks_string = ""

        for task in tasks_list:
            task_details = task.split(",")
            for detail in task_details:
                tasks_string += detail + "\n"
            tasks_string += "\n\n" + "**************************************************" + "\n\n"

        print("**************************************************\n")
        print(tasks_string)

    # Function to view current users tasks
    def view_mine():

        with open("tasks.txt", "r") as tasks:
            tasks = tasks.read().strip()

        tasks_list = tasks.split("\n")

        # Create a list with all tasks assigned to current user
        my_tasks = []
        for task in tasks_list:
            task_details = task.split(",")
            if current_user[0] in task_details[0]:
                my_tasks.append(task)

        # Display tasks in an easy-to-read format
        my_tasks_string = ""
        print()
        for task in my_tasks:
            details = task.split(",")
            for detail in details:
                my_tasks_string += detail + "\n"
            my_tasks_string += "\n\n" + "**************************************************" + "\n\n"

        print(my_tasks_string)

    login()

    view_mine()


main_loop()
