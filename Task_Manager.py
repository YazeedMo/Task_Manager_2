# Function "main_loop" - loops over the whole programme
def main_loop():

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


main_loop()
