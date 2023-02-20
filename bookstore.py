import sqlite3
#importing sqlite3

db = sqlite3.connect('bookstore_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
db.commit()# creates a table if it does not exists and adds the column

books = [(3001, 'A Tale of Two Cities',' Charles Dickens', 30),
(3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
(3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
(3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]
cursor.executemany(''' INSERT INTO bookstore(id, Title, Author, Qty) VALUES(?,?,?,?)''',
books) # Updates the records
db.commit()

#========================================functions=============================================
def enter_book():
    """
    Adds a new record to the bookstore table with the values given by the user
    """
    id = int(input("Enter the id: "))
    title = input("Enter the title : ")
    author = input("Enter the author: ")
    qty = int(input("Enter the quantity: "))
    cursor.execute(''' INSERT INTO bookstore(id, Title, Author, Qty) VALUES(?,?,?,?)''',
    (id,title,author,qty))
    db.commit()
    print("Book has been successfully added to the inventory")

def update_book():
    """
    Updates a record in the bookstore table with the qty for a corresponding id provided by the user
    """
    id = int(input("Enter the id of the book that you would like to update: "))
    qty = int(input("Enter the quantity you would like to update for the corresponding id: "))
    cursor.execute('''UPDATE bookstore SET Qty = ? WHERE id = ? ''', (qty, id))
    print(f"Quantity for the book with ID:{id} has been updated to {qty}")

def delete_book():
    """
    Deletes a record in the bookstore table using the id provided by the user
    """
    id = int(input("Enter the id of the book that you would like to Delete: "))
    cursor.execute('''DELETE FROM bookstore WHERE id = ? ''', (id,))
    print(f"The book is deleted")

def search_book():
    """
    Searches and prints a record in the bookstore table using the id provided by the user
    """
    id = int(input("Enter the id of the book that you would like to Search: "))
    cursor.execute('''SELECT * FROM bookstore  WHERE id = ?''', (id,))
    book = cursor.fetchone()
    print(book)

#========================================Menu=============================================

cursor.execute('''SELECT * FROM bookstore ''')
book = cursor.fetchall()
for row in book:
    print(row)# Prints the table in the form of list for the user to view


while True:
    """ 
    Program uses a series of if, elif and else statements inside a while loop.
    Performs an action chosen by the user from the menu by calling the appropriate functions.
    try except block is used for error handling
    """
    try:
        user_choice = int(input('''\nPlease select one of the following options:
                    1 - Enter Book
                    2 - Update Book
                    3 - Delete Book
                    4 - Search Book
                    0 - exit\n: '''))
    
        if user_choice ==1:
            enter_book()

        elif user_choice ==2:
            update_book()

        elif user_choice ==3:
            delete_book()

        elif user_choice ==4:
            search_book()

        elif user_choice ==0:
            break

        else:
            print("Invalid Input")

    except  ValueError:
        print("Enter an Integer")

    