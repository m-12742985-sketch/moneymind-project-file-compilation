import sqlite3 #Connect to SQLite data base
connection = sqlite3.connect("moneymind.db")
cursor = connection.cursor() #Giving instructions to the database

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    monthly_allowance REAL NOT NULL
)
""")
# Create an integer ID that uniquely identifies each student
#Username is text, cannot be empty, and two students cannot have the same username.

#--------------
#Database for transactions
#-------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    source TEXT NOT NULL,
    date TEXT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
)
""")

#--------------
#Transactions
#-------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    source TEXT NOT NULL,
    date TEXT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
)
""")

#--------------
#Goals
#-------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS goals (
    goal_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    target_amount REAL NOT NULL,
    saved_amount REAL NOT NULL DEFAULT 0,
    deadline TEXT,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
)
""")

#--------------
#products
#-------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL,
    description TEXT
)
""")

#-----------------
#Buying products
#-----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    purchase_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_price REAL NOT NULL,
    date TEXT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
)
""")

connection.commit()
connection.close()

print("MoneyMind database created successfully!")