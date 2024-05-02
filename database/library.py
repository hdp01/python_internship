import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
)

cursor = cnx.cursor()

def view_books(cursor):
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    for book in books:
        print(book)

def search_book(cursor, title):
    query = "SELECT * FROM books WHERE title LIKE %s"
    title_param = (f"%{title}%",)
    cursor.execute(query, title_param)
    books = cursor.fetchall()
    for book in books:
        print(book)

def add_book(cursor, bookid, title, author, total_quantity):
    query = "INSERT INTO books (bookid, title, author, total_quantity) VALUES (%s, %s, %s, %s)"
    data = (bookid, title, author, total_quantity)
    cursor.execute(query, data)
    cnx.commit()

def delete_book(cursor, bookid):
    query = "DELETE FROM books WHERE bookid = %s"
    data = (bookid,)
    cursor.execute(query, data)
    cnx.commit()

def issue_book(cursor, bookid, quantity):
    query = "UPDATE books SET total_quantity = total_quantity - %s WHERE bookid = %s"
    data = (quantity, bookid)
    cursor.execute(query, data)
    cnx.commit()

while True:
    action = input("Enter action (view, search, add, delete, issue, exit): ")
    if action == "view":
        view_books(cursor)
    elif action == "search":
        title = input("Enter book title: ")
        search_book(cursor, title)
    elif action == "add":
        bookid = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        total_quantity = int(input("Enter total quantity: "))
        add_book(cursor, bookid, title, author, total_quantity)
    elif action == "delete":
        bookid = int(input("Enter book ID: "))
        delete_book(cursor, bookid)
    elif action == "issue":
        bookid = int(input("Enter book ID: "))
        quantity = int(input("Enter quantity: "))
        issue_book(cursor, bookid, quantity)
    elif action == "exit":
        break

cnx.close()