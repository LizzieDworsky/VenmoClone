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

def check_balances(user):
    print(f"Venmo: ${user['account_balance']}")
    for bank_tuples in user["connected_banks"]:
        print(f"{bank_tuples[0]}: ${bank_tuples[1]}")

def transfer_amount(user):
    while True:
        amount = int(input("How much would you like to transfer, numbers only: "))
        if amount <= user["account_balance"]:
            return amount
        else:
            print(f"Insufficient balance, you have {user['account_balance']}")

def transfer_money(transferor, transferee):
    while True:
        conf_trans = input(f"{transferor['full_name']} would you like to transfer money to {transferee['full_name']} y/n? ")
        if conf_trans == "n":
            return
        elif conf_trans == "y":
            amount = transfer_amount(transferor)
            return
        else:
            "Invalid entry, please retry"


# check_username_password(user_one)
# check_balances(user_one)
transfer_money(user_one, user_two)