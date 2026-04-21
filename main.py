import mysql.connector

# Step 1: Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",           # your MySQL username
    password="c2c0909",    # the password you set during MySQL install
    database="banking_app"
)
cursor = conn.cursor()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def choice():
    while True:
        try: 
            chosen = int(input('Hello! Welcome to CASH CITY. \nEnter 1 to create an account. \nPress 2 to make a deposit into an account. \nPress 3 to withdraw money from an account. \nPress 4 to list all accounts. \nPress 5 to check an account balance. \nPress 6 to leave! '))
            if chosen == 1:
                create()
            elif chosen == 2:
                deposit()
            elif chosen == 3:
                withdraw()
            elif chosen == 4:
                list_account()
            elif chosen == 5:
                check_balance()
            elif chosen == 6: 
                break
            else:
                print('Please make sure you enter a number 1-6.')
                continue 
        except ValueError:
            print('Please enter an integer.')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create():
    print('You have chosen to create an account!')
    while True:
        try:
            account_name = input('Please enter the name of the account. ')
            initial_deposit = int(input('Now add an initial deposit. '))
            cursor.execute('INSERT INTO accounts (name, balance) VALUES (%s, %s)', (account_name, initial_deposit))
            conn.commit()
            print('Success!')
            break
        except ValueError: 
            print("Please make sure 'initial deposit' has entered correctly as a integer.")

def deposit():
    print('You have chosen to deposit money!')
    while True:
        try:
            account_chosen = input('Choose an account. ')
            amount = int(input('Please enter how much money you would like to deposit. '))
            
            if amount <= 0:
                print("Please make sure you deposit a number over 0.")
                continue

            cursor.execute('SELECT * FROM accounts WHERE name = %s', (account_chosen,))
            account_to_deposit = cursor.fetchone()

            if account_to_deposit is None:
                print('Make sure your account name is spelled correctly.') 
                continue

            balance = account_to_deposit[2]
            new_balance = amount + balance

            cursor.execute('UPDATE accounts SET balance = %s WHERE name = %s', (new_balance, account_chosen,))
            conn.commit()

            print(f'Success! The new balance of {account_chosen} is {new_balance}')
            break

        except ValueError: 
            print("Please make sure you deposit a number over 0 has entered correctly as a integer. Also make sure the account named is spelled correctly.")

def withdraw():
    print('You have chosen to withdraw money!')
    while True:
        try:
            account_chosen = input('Choose an account. ')
            amount = int(input('Please enter how much money you would like to withdraw from the account. '))
            
            if amount <= 0:
                print("Please make sure you deposit a number over 0.")
                continue

            cursor.execute('SELECT * FROM accounts WHERE name = %s', (account_chosen,))
            account_to_deposit = cursor.fetchone()

            if account_to_deposit is None:
                print('Make sure your account name is spelled correctly.') 
                continue

            balance = account_to_deposit[2]
            new_balance = balance - amount

            if balance < amount:
                print('Please make sure the amount you withdraw is less then the balance!')
                continue

            cursor.execute('UPDATE accounts SET balance = %s WHERE name = %s', (new_balance, account_chosen,))
            conn.commit()

            print(f'Success! The new balance of {account_chosen} is {new_balance}.')
            break

        except ValueError: 
            print("Please make sure you deposit a number over 0 has entered correctly as a integer. Also make sure the account named is spelled correctly.")

def list_account():
    print('You have chosen to see all accounts')
    cursor.execute('SELECT * FROM accounts')
    accounts = cursor.fetchall()
    for account in accounts:
     print(f"Name: {account[1]} | Balance: ${account[2]}")

def check_balance():
    print('You have chosen to check an accounts balance')
    while True:
        try:
            account_chosen = input('Choose an account. ')
            cursor.execute('SELECT * FROM accounts WHERE name = %s', (account_chosen,))
            account_to_deposit = cursor.fetchone()

            if account_to_deposit is None:
                print('Make sure your account name is spelled correctly.') 
                continue

            balance = account_to_deposit[2]
            print(f'Success! The new balance of {account_chosen} is {balance}')
            break

        except ValueError:
            print("Please make sure input is correct.")

choice()

# Always close when done
conn.close()