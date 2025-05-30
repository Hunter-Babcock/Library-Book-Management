#Hunter Babcock
#CMPS 372 Intro to Python
#Final Assignment
import time

# Base User class
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_name, library):
        if book_name in library.inventory:
            self.borrowed_books.append(book_name)
            library.inventory.remove(book_name)
            library.borrow_log.append(book_name)
            print(f"{self.name} borrowed '{book_name}'.")
        else:
            print(f"Sorry, '{book_name}' is not available.")

    def return_book(self, book_name, library):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            library.inventory.append(book_name)
            print(f"{self.name} returned '{book_name}'.")
        else:
            print(f"{self.name} did not borrow '{book_name}'.")

# Student and Teacher classes
class Student(User):
    def borrow_book(self, book_name, library):
        if len(self.borrowed_books) >= 3:
            print("Students can borrow up to 3 books only.")
        else:
            super().borrow_book(book_name, library)

class Teacher(User):
    def borrow_book(self, book_name, library):
        if len(self.borrowed_books) >= 5:
            print("Teachers can borrow up to 5 books only.")
        else:
            super().borrow_book(book_name, library)

# Library class
class Library:
    def __init__(self):
        self.inventory = ["1984", "To Kill a Mockingbird", "Moby Dick"]
        self.borrow_log = []

    def add_book(self, book_name):
        self.inventory.append(book_name)
        print(f"Book '{book_name}' added to the inventory.")

    def remove_book(self, book_name):
        if book_name in self.inventory:
            self.inventory.remove(book_name)
            print(f"Book '{book_name}' removed from inventory.")
        else:
            print(f"Book '{book_name}' not found.")

    def view_inventory(self):
        if self.inventory:
            print("\nAvailable books:")
            for book in self.inventory:
                print(f"- {book}")
        else:
            print("No books available.")

    def view_report(self):
        print("\n--- Library Report ---")
        print(f"Total books borrowed: {len(self.borrow_log)}")
        print(f"Books currently in inventory: {len(self.inventory)}")
        print("------------------------")

# Main menu

def main():
    library = Library()
    user = None

    while True:
        print("\nWelcome to the Library Management System")
        print("1) Log in as Student")
        print("2) Log in as Teacher")
        print("3) Borrow a Book")
        print("4) Return a Book")
        print("5) Manage Inventory")
        print("6) View Report")
        print("7) Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            user = Student(name)
            print(f"Logged in as Student: {name}")

        elif choice == "2":
            name = input("Enter your name: ")
            user = Teacher(name)
            print(f"Logged in as Teacher: {name}")

        elif choice == "3":
            if user:
                library.view_inventory()
                book = input("Enter the name of the book to borrow: ")
                user.borrow_book(book, library)
            else:
                print("Please log in first.")

        elif choice == "4":
            if user:
                book = input("Enter the name of the book to return: ")
                user.return_book(book, library)
            else:
                print("Please log in first.")

        elif choice == "5":
            print("\n1) Add a Book")
            print("2) Remove a Book")
            sub_choice = input("Choose an option: ")
            if sub_choice == "1":
                book = input("Enter book name to add: ")
                library.add_book(book)
            elif sub_choice == "2":
                book = input("Enter book name to remove: ")
                library.remove_book(book)
            else:
                print("Invalid input.")

        elif choice == "6":
            library.view_report()

        elif choice == "7":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid selection. Please try again.")
        time.sleep(1)

if __name__ == "__main__":
    main()

