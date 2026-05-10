"""
Login →
Main Menu →
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Transfer
    5. Mini Statement
    6. Change PIN
    7. Logout
"""
import os, json
FILE_NAME = 'users.json'
current_user = None

def load_user():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except:
        return []

def save_user(users):
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file, indent=4 )

def login():
    global current_user

    users = load_user()
    username = input("Enter username: ")
    pin = input("Enter PIN: ")

    for user in users:
        if user['username'] == username and user['pin'] == pin:
            current_user = user
            print(f"Welcome to our ATM Simulator System, {username}")
            return True
    print("Error: Invalid Credentials")
    return False

def register():
    users = load_user()

    username = input("Enter username : ")
    pin = input("Create 4-digits PIN: ")

    # Check duplicate of username
    for user in users:
        if user['username'] == username:
            print("Username already exists")
            return 
        
    # validate PIN
    if len(pin) != 4 or not pin.isdigit():
        print("Message: PIN must be exactly 4 digits")
        return
    new_user = {
        'username': username, 
        'pin': pin,
        'balance': 0.00,
        'transactions': []
    }

    users.append(new_user)
    save_user(users)

    print("Message: Account created successfully....")

def change_pin():
    users = load_user()

    old_pin = input("Enter your old pin: ")
    if current_user['pin'] != old_pin:
        print("Message: Incorrect old pin")
        return
    new_pin = input("Enter a new pin: ")

    # validate PIN
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("Message: PIN must be exactly 4 digits")
        return
    
    current_user['pin'] = new_pin
    for user in users:
        if user['username'] == current_user['username']:
            user.update(current_user)
    
    save_user(users)
    print("Message: Pin updated successfully....")
    
def logout():
    global current_user
    current_user = None
    print("Message: Logged out Successfully..")


def deposit():
    users = load_user()

    amount = float(input("Enter amont to deposit: "))
    current_user['balance'] += amount
    current_user['transactions'].append(f"Deposted +{amount}")

    for user in users:
        if user['username'] == current_user['username']:
            user.update(current_user)
    save_user(users)
    print(f"Message: Amount {amount} deposited Successfully..")

def check_balance():
    print(f"Your Balance: {current_user['balance']}")

def withdraw():
    users = load_user()

    amount = float(input("Enter your amount to withdraw: "))
    if amount > current_user['balance']:
        print("Message: Insufficient Balance")
        return
    current_user['balance'] -= amount
    current_user['transactions'].append(f"Withdraw -{amount}")

    for user in users:
        if user['username'] == current_user['username']:
            user.update(current_user)
    
    save_user(users)
    print(f"Amount {amount} withdraw successfully.....")

def transfer():
    users = load_user()
    transfer_to = input("Enter username to transfer: ")
    amount = float(input("Enter your amount to withdraw: "))

    if amount > current_user['balance']:
        print("Message: Insufficient Balance")
        return
    
    current_user['balance'] -= amount
    current_user['transactions'].append(f"Transfered -{amount} \n\tSender: {current_user['username']} \n\tReceiver: {transfer_to}")

    for user in users:
        if user['username'] == current_user['username']:
            user.update(current_user)
    
    save_user(users)
    print(f"Amount {amount} transferred successfully.....")

def view_statement():
    print("\n")
    print("\n===== MINI STATEMENT =====")
    print(f"User: {current_user['username']}")
    print(f"Balance: {current_user['balance']:.3f}\n")

    # transactions = current_user.get("transactions", [])
    transactions = current_user['transactions']

    for t in transactions[::-1]:
        print(t)

    print("==========================")

def main_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Mini Statement")
        print("6. Change PIN")
        print("7. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            view_statement()
        elif choice == "6":
            change_pin()
        elif choice == "7":
            logout()
            break
        else:
            print("Invalid choice")

def main():
    while True:
        print("\n")
        print("\n===== WELCOME =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                main_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()