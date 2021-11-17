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

    login()


main_loop()
