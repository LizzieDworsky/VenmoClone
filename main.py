user_one = {"full_name": "Amy", "username": "Lizzie", "password": "password", "account_balance": 50, "connected_banks": [("Chase", 200), ("Citi", 50)]}
user_two = {"full_name": "Josh", "username": "Joshua", "password": "password", "account_balance": 25, "connected_banks": [("Chase", 150), ("Capital One", 200)]}


def check_username_password(user):
    conf_bool = True
    while conf_bool:
        temp_username = input("Please enter your username: ")
        if temp_username == user["username"]:
            while conf_bool:
                temp_password = input("Please enter your password: ")
                if temp_password == user["password"]:
                    print("You have been logged in")
                    conf_bool = False


check_username_password(user_one)