class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

    
class Bookstore:
    books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title}: added to the inventory.")

    def remove_book(self, title):
        for book in self.books:
            self.books.remove(book)
            print("Book have been removed")

        else:
            print("book not found in the inventory")

    def search_by_author(self, author):
        
        for book in self.books:
            if book.author.lower() == author.lower():
                print(f"Name: {book.title}")
                break
                
            else:
                print("Book not found")

    def search_by_title(self, title):
     
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Name: {book.title}")
                break
        
            else:
                print("Book not found")

    def display_book(self):
        for book in self.books:
            print(book.title)

class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.books_collection = []

    def buy_book(self, bookstore, title):

        for book in bookstore.books:
            if book.title.lower() == title.lower():
                if book.quantity > 0:
                    self.books_collection.append(book)
                    book.quantity -= 1
                    bookstore.books.remove(book)
                    print(f"Book have been purchased successfully.")
                break
        else:
            print("Book not found in the inventory.")

    def display_books_collection(self):
        print(f"Books Collection of {self.name}:")
        for book in self.books_collection:
            print(book.title)
    
def main():
    
    bookstore = Bookstore()
    b1 = Book("the chemist", "Meyer", "Thriller", 12, 10)
    b2 = Book("twenty dollar horse", "gerald", "drama", 32, 14)
    b3 = Book("the cent son", "jannie", "drama", 52, 15)

    bookstore.add_book(b1)
    bookstore.add_book(b2)
    bookstore.add_book(b3)

    while(True):
        print("input a choice from the following choices")
        print("For adding the book press: 1")
        print("For removing the book press: 2")
        print("Search book by title press: 3")
        print("Search book by author name press: 4")
        print("Display the book in the inventory press: 5")
        print("buy a book form store press: 6")
        print("Quit the program press: 7")

        choice = input("Type your choice: ")
        
        if choice == "1":
            a = input("Add the title of the Book: ")
            b = input("Add the author name of the Book: ")
            c = input("Add the genre of the Book: ")
            d = int(input("Add the price of the Book: "))
            e = int(input("Add the qunatity of the Book: "))

            book3 = Book(a, b, c, d, e)

            bookstore.add_book(book3)

        elif choice == "2":
            removing_book = input("Enter the title of the book: ")
            bookstore.remove_book(removing_book)

        elif choice == "3":
            search_title = input("Enter the title for search the book")

            bookstore.search_by_title(search_title)

        elif choice == "4":
            search_author = input("Enter the author name for search the book")

            bookstore.search_by_author(search_author)


        elif choice == "5":
            if bookstore.books:
                bookstore.display_book()
            else:
                print("no book found in the inventory")

        elif choice == "6":
            if bookstore.books:
                user_name = input("Enter your name: ")
                user_age = int(input("Enter your age: "))
                user_address = input("Enter your address: ")

                user = User(user_name, user_age, user_address)

                book_to_buy = input("Enter the title of the book you want to buy: ")
                user.buy_book(bookstore, book_to_buy)


        elif choice == "7":
            print("quiting a program")
            break

        else:     
            print("invalid choice")

main()
