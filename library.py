import sqlite3
import time

class Book():
    def __init__(self,name,author,publisher,sort,edition):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.sort = sort
        self.edition = edition

    def __str__(self):
        return "Book's name: {}\nAuthor: {}\nPublisher: {}\nSort of Book: {}\nEdition: {}".format(self.name,self.author,self.publisher,self.sort,self.edition)

class Library():
    def __init__(self):
        self.create_connect()

    def create_connect(self):
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS books (name TEXT,author TEXT,publisher TEXT,sort TEXT,edition INT)"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connect(self):
        self.conn.close()

    def show_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        if(len(books) == 0):
            print("There is no book in library.")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def search_book(self,name):
        query = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()
        if(len(books) == 0):
            print("\nNo books were found for your search.")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(book)

    def add_book(self,book):
        query = "INSERT INTO books Values(?,?,?,?,?)"
        self.cursor.execute(query,(book.name,book.author,book.publisher,book.sort,book.edition))
        self.conn.commit()

    def delete_book(self,name):
        query = "DELETE FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        book = self.cursor.fetchall()
        if(len(book)==0):
            print("No such book can be found.")
        else:
            print("The book is deleting...")
            time.sleep(2)
            print("The book was deleted from library successfully.")
            time.sleep(2)
        self.conn.commit()

    def upgrade_edition(self,name):
        query = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        books = self.cursor.fetchall()
        if(len(books) == 0):
            print("No such book can be found.")
        else:
            edition = books[0][4]
            edition += 1
            query2 = "UPDATE books SET edition = ? WHERE name = ?"
            self.cursor.execute(query2,(edition,name))
            self.conn.commit()