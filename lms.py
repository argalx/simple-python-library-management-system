import sqlite3
from os import system
from time import sleep

# Clear interpreter variable
clear = lambda: system('cls')

# Sleep seconds
sleepSeconds = 3

# Database connection variable
conn = sqlite3.connect('simple-python-library-management-system/lms.db')

# Cursor variable
cursor = conn.cursor()

# LMS Functions
# Invalid Int Message Function
def invalidInt():
    print('Invalid input! The key selection is not part of the specified option.')

# Invalid Not Int Message Function
def invalidNotInt():
    print('The key selection is not a number and is invalid.')

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

# LMS Objects
# Student Object
class Student:
    def __init__(self, id='', firstName='', lastName=''):
        self._id = id
        self._firstName = firstName
        self._lastName = lastName

    # Add Student Method
    def addNewStudent(self):
        # Insert data to students table
        cursor.execute('INSERT INTO students (first_name, last_name) VALUES (?, ?)', (self._firstName, self._lastName))

        # Commit changes
        conn.commit()

        return 'Student Added.'
    
    # List All Student Method
    def listAllStudent(self):
        # Select all data in students table
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        
        if not students:
            return 'Student Record is Empty'
        
        else:
            # Display retrieved students data
            for student in students:
                print(student)

    # Select Student Method
    def selectStudent(self):
        # Select student based on ID filter
        cursor.execute('SELECT * FROM students WHERE id=?',(self._id,))
        student = cursor.fetchall()

        return student

    # Update Student Method
    def updateStudent(self, recordToUpdate):
        # Record to Update Condition
        if recordToUpdate == 'firstName':
            # Update First Name
            cursor.execute('UPDATE students SET first_name=? WHERE id=?',(self._firstName, self._id))

            # Commit changes
            conn.commit()

            return 'First Name Updated.'

        elif recordToUpdate == 'lastName':
            # Update Last Name
            cursor.execute('UPDATE students SET last_name=? WHERE id=?',(self._lastName, self._id))

            # Commit changes
            conn.commit()

            return 'Last Name Updated.'
        
    # Delete Student Method
    def deleteStudent(self):
        # Delete Student Record
        cursor.execute('DELETE FROM students WHERE id=?',(self._id,))

        # Commit changes
        conn.commit()

        return 'Student Record Deleted.'

class BookType:
    def __init__(self):
        pass

class Book:
    def __init__(self):
        pass

class BorrowCard:
    def __init__(self):
        pass

# Welcome message
print('Welcome to ArgalX Library Management System')

# LMS Logic
while True:
    # Try catch Main Menu errors
    try:
        # Main Menu
        userInput = int(input('Main Menu: Press 1 - (Student Management) | Press 2 - (Book Management) | Press 3 - (Book Borrowing) | Press 4 - (Exit Application): '))

        # Main Menu Controls
        # Student Management
        if userInput == 1:
            # Student Management Main Loop Control
            studentManagement = True

            while studentManagement == True:
                try:
                    # Pause for n seconds after printing output
                    sleep(sleepSeconds)

                    # Clear screen for windows only
                    clear()

                    # Student Management Menu
                    userInput = int(input('Student Management: Press 1 - (Add Student) | Press 2 - (List All Student) | Press 3 - (Update Student Record) | Press 4 - (Delete Student Record) | Press 5 - (Back to Main Menu): '))

                    # Student Management Menu Controls
                    # Add Student
                    if userInput == 1:
                        # Add Student Loop Control
                        addStudent = True

                        firstName = input('Enter Student First Name: ')
                        lastName = input('Enter Student Last Name: ')

                        # Add Student Loop
                        while addStudent == True:
                            try:
                                userInput = int(input('Would you like to add this student? Press 1 - (Confirm) | Press 2 - (Cancel): '))

                                if userInput == 1:
                                    addStudent = False
                                    
                                    # Initialize Student Instance
                                    student = Student(firstName=firstName, lastName=lastName)

                                    # Call addNewStudent Method
                                    print(student.addNewStudent())

                                elif userInput == 2:
                                    addStudent = False
                                    print('Canceled...')

                                else:
                                    # Invalid Int Selection
                                    invalidInt()

                            # Catch ValueError type (Add Student)
                            except ValueError:
                                invalidNotInt()

                            # Catch any errors        
                            except Exception as e:
                                print(f'Error: {type(e).__name__}, Message: {e.args}')

                    # List All Student
                    elif userInput == 2:
                        # Initialize Student Object
                        student = Student()

                        # Call listAllStudent Method
                        if student.listAllStudent() == 'Student Record is Empty':
                            print(student.listAllStudent())
                            print('Back to Student Management Menu...')

                    # Update Student Record
                    elif userInput == 3:
                        # Update Student Loop Control
                        updateStudent = True
                        
                        # Update Student Loop
                        while updateStudent == True:
                            try:
                                # Pause for n seconds after printing output
                                sleep(sleepSeconds)

                                # Clear screen for windows only
                                clear()

                                userInput = int(input('Would you like to update a student record? Press 1 - (Confirm) | Press 2 - (Back to Student Management Menu): '))

                                if userInput == 1:
                                    # Initialize Student Object
                                    student = Student()

                                    # Call listAllStudent Method
                                    if student.listAllStudent() == 'Student Record is Empty':
                                        print(student.listAllStudent())
                                        
                                        # End Loops
                                        updateStudent = False
                                        studentUpdate = False

                                        print('Back to Student Management Menu...')

                                    else:
                                        # Student Update Loop Control
                                        studentUpdate = True

                                    while studentUpdate == True:
                                        try:
                                            studentId = int(input('Select Student ID: '))

                                            # Initialize Student Object
                                            student = Student(id=str(studentId))

                                            # Check if Student Record Exist
                                            if not student.selectStudent():
                                                print('No Record Found.')

                                            else:
                                                print(student.selectStudent())
                                                # Updating Student Record
                                                # Update Student Record Loop Control
                                                updateRecord = True
                                                
                                                # Update Student Record Loop
                                                while updateRecord == True:
                                                    try:
                                                        userInput = int(input('Select Record to Update: Press 1 - (First Name) | Press 2 - (Last Name) | Press 3 - (Cancel): '))
                                                        
                                                        # Update First Name
                                                        if userInput == 1:
                                                            # First Name
                                                            studentFirstName = input('Student First Name Update: ')

                                                            # Initialize Student Instance
                                                            student = Student(id=studentId, firstName=studentFirstName)

                                                            # Call updateStudent Method
                                                            print(student.updateStudent('firstName'))
                                                            
                                                            # End Loops
                                                            updateRecord = False
                                                            studentUpdate = False
                                                            updateStudent = False

                                                        elif userInput == 2:
                                                            # First Name
                                                            studentFirstName = input('Student First Name Update: ')

                                                            # Initialize Student Instance
                                                            student = Student(id=studentId, firstName=studentFirstName)

                                                            # Call updateStudent Method
                                                            print(student.updateStudent('firstName'))

                                                            # End Loops
                                                            updateRecord = False
                                                            studentUpdate = False
                                                            updateStudent = False

                                                        elif userInput == 3:
                                                            # End Loops
                                                            updateRecord = False
                                                            studentUpdate = False
                                                            updateStudent = False
                                                            print('Canceled. Going back to Student Management Menu...')

                                                        else:
                                                            # Call invalidInt Function
                                                            invalidInt()

                                                    # Catch ValueError type (Select Record to Update)
                                                    except ValueError:
                                                        invalidNotInt()

                                                    # Catch any errors        
                                                    except Exception as e:
                                                        print(f'Error: {type(e).__name__}, Message: {e.args}')

                                        # Catch ValueError type (Student ID)
                                        except ValueError:
                                            invalidNotInt()

                                        # Catch any errors        
                                        except Exception as e:
                                            print(f'Error: {type(e).__name__}, Message: {e.args}')

                                elif userInput == 2:
                                    updateStudent = False
                                    print('Back to Student Management Menu...')

                                else:
                                    # Invalid Int Selection
                                    invalidInt()

                            # Catch ValueError type (Update Student)
                            except ValueError:
                                invalidNotInt()

                            # Catch any errors        
                            except Exception as e:
                                print(f'Error: {type(e).__name__}, Message: {e.args}')

                    # Delete Student Record
                    elif userInput == 4:
                        # Delete Student Loop Control
                        deleteStudent = True

                        # Delete Student Loop
                        while deleteStudent == True:
                            try:
                                # Pause for n seconds after printing output
                                sleep(sleepSeconds)

                                # Clear screen for windows only
                                clear()

                                userInput = int(input('Would you like to delete a student record? Press 1 - (Confirm) | Press 2 - (Back to Student Management Menu): '))

                                if userInput == 1:
                                    # Initialize Student Object
                                    student = Student()
                                    
                                    # Call listAllStudent Method
                                    if student.listAllStudent() == 'Student Record is Empty':
                                        print(student.listAllStudent())

                                        # End Loops
                                        deleteStudent = False
                                        studentDelete = False

                                        print('Back to Student Management Menu...')

                                    else:
                                        # Student Delete Loop Control
                                        studentDelete = True

                                    # Student Delete Loop
                                    while studentDelete == True:
                                        try:
                                            studentId = int(input('Select Student ID: '))

                                            # Initialize Student Object
                                            student = Student(id=str(studentId))

                                            # Check if Student Record Exist
                                            if not student.selectStudent():
                                                print('No Record Found.')

                                            else:
                                                print(student.selectStudent())
                                                # Deleting Student Record
                                                # Delete Student Record Loop Control
                                                deleteRecord = True

                                                # Delete Student Record Loop
                                                while deleteRecord == True:
                                                    try:
                                                        userInput = int(input('Do you want to delete this record permanently?: Press 1 - (Confirm) | Press 2 - (Cancel): '))

                                                        if userInput == 1:
                                                            # Call deleteStudent Method
                                                            print(student.deleteStudent())

                                                            # End Loops
                                                            deleteRecord = False
                                                            studentDelete = False
                                                            deleteStudent = False

                                                        elif userInput == 2:
                                                            # End Loops
                                                            deleteRecord = False
                                                            studentDelete = False
                                                            deleteStudent = False
                                                            print('Canceled. Going back to Student Management Menu...')

                                                        else:
                                                            # Invalid Int Selection
                                                            invalidInt

                                                    # Catch ValueError type (Student ID)
                                                    except ValueError:
                                                        invalidNotInt()

                                                    # Catch any errors        
                                                    except Exception as e:
                                                        print(f'Error: {type(e).__name__}, Message: {e.args}')
                                        
                                        # Catch ValueError type (Student ID)
                                        except ValueError:
                                            invalidNotInt()

                                        # Catch any errors        
                                        except Exception as e:
                                            print(f'Error: {type(e).__name__}, Message: {e.args}')

                                elif userInput == 2:
                                    deleteStudent = False
                                    print('Back to Student Management Menu...')

                                else:
                                    # Invalid Int Selection
                                    invalidInt()

                            # Catch ValueError type (Update Student)
                            except ValueError:
                                invalidNotInt()

                            # Catch any errors        
                            except Exception as e:
                                print(f'Error: {type(e).__name__}, Message: {e.args}')

                    # Back to Main Menu
                    elif userInput == 5:
                        studentManagement = False
                        print('Back to Main Menu...')

                    else:
                        # Invalid Int Selection
                        invalidInt()

                # Catch ValueError type (Student Management Menu)
                except ValueError:
                    invalidNotInt()

                # Catch any errors (Student Management Menu Controls)    
                except Exception as e:
                    print(f'Error: {type(e).__name__}, Message: {e.args}')

        # Book Management
        elif userInput == 2:
            pass
            
        # Book Borrowing
        elif userInput == 3:
            pass

        # Exit Application
        elif userInput == 4:
            print('Exit program...')
            break

        else:
            # Invalid Int Selection
            invalidInt()

    # Catch ValueError type (Main Menu)
    except ValueError:
        invalidNotInt()

    # Catch any errors        
    except Exception as e:
        print(f'Error: {type(e).__name__}, Message: {e.args}')

    # Pause for n seconds after printing output
    sleep(sleepSeconds)

    # Clear screen for windows only
    clear()

# Close connection
conn.close()