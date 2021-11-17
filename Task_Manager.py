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

    reg_user()


main_loop()
