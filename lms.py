import sqlite3

# Connect to SQLite database (Create if not exist)
conn = sqlite3.connect('simple-python-library-management-system/lms.db')

# Create cursor object to execute SQLite queries
cursor = conn.cursor()

# Table creation if not exist

# Create Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY,
               first_name TEXT NOT NULL,
               last_name TEXT NOT NULL
    )
''')

# Create Book Types table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_types (
               id INTEGER PRIMARY KEY,
               type TEXT NOT NULL
    )
''')

# Create Books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               description TEXT NOT NULL,
               quantity INTEGER NOT NULL,
               book_type_id INTEGER NOT NULL
    )
''')

# Create Borrowing Cards table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrowing_cards (
               id INTEGER PRIMARY KEY,
               stude_id INTEGER NOT NULL,
               book_id INTEGER NOT NULL,
               borrow_date DATE NOT NULL,
               return_date DATE
    )
''')

# Close connection
conn.close()