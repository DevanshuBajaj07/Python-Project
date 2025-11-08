
```markdown
# Library Management System

A simple command-line Library Management System built using Python. This system allows users to add books, view all books, and manage a library's collection.

---

## Features
- **Add Books**: Add new books to the library with details like title, publisher, and year of publication.
- **View All Books**: Display a list of all books in the library, including their availability status.
- **Persistent Storage**: Book details are saved to a file (`books.txt`) for persistence across sessions.
- **Menu-Driven Interface**: Easy-to-use menu for navigating the system.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. **Run the Program**:
   Ensure you have Python installed, then run:
   ```bash
   python main.py
   ```

---

## How to Use

1. **Start the Program**:
   - Run the program to access the menu-driven system.

2. **Menu Options**:
   - **1. Add a Book**: Enter the book's title, publisher, and year of publication to add it to the library.
   - **2. View All Books**: Displays a list of all books in the library, including their availability status.
   - **3. Exit**: Exit the program.

3. **Persistent Storage**:
   - All books are saved in the `Library/books.txt` file. The program will read from this file when viewing books.

---

## File Structure

```
Library/
├── books.txt  # Stores the list of books (created automatically if it doesn't exist)
├── main.py    # Main Python script for the Library Management System
└── README.md  # Project documentation
```

---

## Example Usage

### Adding a Book
```plaintext
=== Library System ===
1. Add a book
2. View all books
3. Exit
Enter your choice (1/2/3): 1
Enter the book title: Python Programming
Enter the book publisher: O'Reilly Media
Enter the year published: 2020
Book "Python Programming" added successfully!
```

### Viewing All Books
```plaintext
=== Library System ===
1. Add a book
2. View all books
3. Exit
Enter your choice (1/2/3): 2
1. Python Programming — O'Reilly Media (2020) — Available
```

---

## Requirements

- Python 3.6 or higher

---

## Customization

- **Change the Storage File**:
  Modify the file path in the `add_book` and `view_books` methods to use a different file for storing book data:
  ```python
  with open("Library/books.txt", "a") as file:  # Change "Library/books.txt" to your desired file path
  ```

- **Add More Features**:
  - Implement a feature to delete books.
  - Add a search functionality to find books by title or publisher.
  - Track borrowed books and their return status.

---

## Credits

- **Developer**: [Your Name](https://github.com/DevanshuBajaj07)

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

---


Enjoy managing your library!
```
