''' 28.10.20-
author-manas verma
mini project(my library)

Statement:-
The task is to create an “Online Library Management System”.
For this, you have to create a library class which includes the following methods:

Displaybook() : To display the available books
Lendbook(): To lend a book to a user
Addbook(): To add a book in the library
Returnbook(): To return the book in the library.
As you have created a library class, now you will create an object and pass the following
parameters in the constructor.

HarryLibrary=Library(listofbooks, library_name)

After that, create a main function and run an infinite while loop which asks the users
for their input that whether they want to display, lend, add or return a book.

Optional:-
Maintain a dictionary for the users who own a book. Dictionary should take book name as a
key and name of the person as a value. Whenever you lend a book to a user, you should maintain
a dictionary.'''


class Library():
    def __init__(self, list_of_books, Library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No reader have lend this book
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = reader
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)


def main():
    # By deafault variables
    list_books = ['Cookbook', 'Sherlock Holmes', 'Chacha_chaudhary', 'Rich Dad and Poor Dad']
    Library_name = 'manas'
    secret_key = 1357

    manas = Library(list_books, Library_name)

    print(
        f"Welecome To {manas.library_name} library\n\nq for exit \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and Delete Book using 'del' \n ")

    Exit = False
    while (Exit is not True):
        _input = input("option:")
        print("\n")

        if _input == "q":
            Exit = True

        elif _input == "d":
            manas.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")
            print("\n Book Lend \n")
            manas.lend_book(_input3, _input2)

        elif _input == "a":
            _input2 = input("Book name:")
            manas.add_book(_input2)

        elif _input == "del":
            _input_secret = int(input("Write the secret key to delete:"))
            if (_input_secret == secret_key):
                _input2 = input("Book Which you want to delete:")
                manas.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            manas.return_book(_input3, _input2)


if __name__ == "__main__":
    main()
























