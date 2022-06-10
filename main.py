from library import *
import time
print("""
      **************************************
      *    Welcome to the Virtual Library  *
      **************************************
      *             Sections               *
      **************************************
      *                                    *
      *         1. Show All Books          *
      *         2. Search Book             *
      *         3. Add Book                *
      *         4. Delete Book             *
      *         5. Upgrade Edition         *
      *                                    *
      **************************************
      *   Press 'Q' to exit the program    *
      **************************************
      
      """)

library = Library()

while True:
    choice = input("\nYour choice: ")
    if(choice == "Q" or choice == "q"):
        print("\nThe program is terminated...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        break
    elif(choice == "1"):
        library.show_books()
        pass
    elif(choice == "2"):
        name = input("\nEnter book's name: ")
        library.search_book(name)
        pass
    elif(choice == "3"):
        name = input("\nEnter book's name: ")
        author = input("Enter author name: ")
        publisher = input("Enter publisher name: ")
        sort = input("Enter book's sort: ")
        edition = input("Enter book's edition: ")
        book = Book(name,author,publisher,sort,edition)
        print("\nThe book is adding to library...")
        time.sleep(2)
        library.add_book(book)
        print("The book was added to library successfully.")
        time.sleep(2)
        pass
    elif(choice == "4"):
        name = input("\nEnter the name of the book you want to delete: ")
        library.delete_book(name)
        pass
    elif(choice == "5"):
        name = input("\nEnter the name of the book you want to upgrade edition: ")
        library.upgrade_edition(name)
        print("The book's edition is upgrading...")
        time.sleep(2)
        print("The book's edition was upgraded successfully.")
        time.sleep(2)
        pass
    else:
        print("\nYou entered wrong choice.Please try again.")
        time.sleep(2)
        continue


