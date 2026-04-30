This is a simple banking app utilizing Python and SQL. All information is stored in a database. To get started, enter your MySQL login credentials and connect your MySQL server to Python. After that, you're ready to go. 
The core functions of this app are as follows: 
Create an account 
Withdraw money from an account 
Deposit into an account 
List an account 
Check the balance of a specific account.

Run this first: pip install mysql-connector-python

Then: CREATE DATABASE banking_app;
USE banking_app;
CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    balance INT NOT NULL);
