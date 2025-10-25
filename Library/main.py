# Define a class to represent a Book
class Book:
    def __init__(self, title, publisher, year, is_available=True):
        # Initialize book attributes
        self.title = title
        self.publisher = publisher
        self.year = year
        self.is_available = is_available

# Define a class to represent a Library
class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []
       
    def add_book(self, title, publisher, year):
        # Create a new Book object
        new_book = Book(title, publisher, year)
        # Add the new book to the library's list of books
        self.books.append(new_book)
        
        # Append the book details to a file for persistence
        with open("Library/books.txt", "a") as file:
            file.write(f"{title},{publisher},{year},Available\n")
        
        # Notify the user that the book was added successfully
        print(f'Book "{title}" added successfully!')
        
    def view_books(self):
        # Try to read the books from the file
        try:
            with open("Library/books.txt", "r") as file:
                # Read all lines from the file
                txt = file.readlines()
                
                # Check if the file is empty
                if not txt:
                    print("No Books Found. Try adding the books")
                else:
                    # Iterate through each line in the file
                    for index, line in enumerate(txt, start=1):
                        line = line.strip()  # Remove extra spaces or newline characters
                        title, publisher, year, status = line.split(",")  # Split the line by commas

                        # Display the book information in a clean format
                        print(f"{index}. {title} — {publisher} ({year}) — {status}")
        except FileNotFoundError:
            # Handle the case where the file does not exist
            print("The books file does not exist. Please add a book first.")    

# Create one Library object to use for the whole session
library = Library()

# Start an infinite loop for the menu-driven system
while True:
    # Display the menu options
    print("\n=== Library System ===")
    print("1. Add a book")
    print("2. View all books")
    print("3. Exit")
    
    # Get the user's choice
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        # Ask the user for book details
        title = input("Enter the book title: ").strip()
        publisher = input("Enter the book publisher: ").strip()
        year = input("Enter the year published: ").strip()
        
        # Add the book to the library
        library.add_book(title, publisher, year)
    
    elif choice == "2":
        # Show all books in the library
        library.view_books()
    
    elif choice == "3":
        # Exit the program
        print("Goodbye!")
        break  # Exit the loop and end the program
    
    else:
        # Handle invalid menu choices
        print("Invalid choice. Please try again.")
