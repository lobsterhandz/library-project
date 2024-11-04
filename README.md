# Library Management System

## Overview
This is a command-line interface (CLI) based Library Management System that provides a range of functionalities for managing books, users, authors, and genres within a library. It is organized into different modules to promote maintainability and scalability. The system provides various menu actions like adding books, borrowing, returning, viewing items, and interacting with library users.

## Features
- **Book Operations**: Add new books, borrow books, return books, search for books, and display all available books.
- **User Operations**: Add users, view user details, and display all users.
- **Author Operations**: Add authors, view author details, and display all authors.
- **Genre Operations**: Add genres, view genre details, and display all genres.
- **Input Validation**: Input validation is performed to ensure data integrity and accuracy.
- **Error Handling**: Implements error handling for invalid inputs and edge cases like empty library data.

## Modules
The project is organized into the following Python modules to ensure code modularity and reusability:

1. **`main.py`**: The main entry point of the application. It initializes the library instance and starts the main menu.
2. **`menu.py`**: Handles user interactions through various menus for book, user, author, and genre operations.
3. **`book_utils.py`**: Contains classes like `Library`, `Book`, `Author`, and `Genre` that handle the core functionalities of the library management system.
4. **`user.py`**: Defines the `User` class to manage user interactions such as borrowing and returning books.
5. **`validation.py`**: Contains validation functions using regular expressions to validate inputs like ISBNs, user IDs, and names.

## Setup Instructions
1. Clone the repository from GitHub:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure you have Python installed (preferably version 3.7+).

3. Run the program using the following command:
   ```sh
   python main.py
   ```

## Usage
Upon running the program, you will be prompted with a main menu that includes different operations for books, users, authors, and genres. Each menu allows you to add, view, search, or display relevant data.

### Example Usage:
- **Add a Book**: Navigate to "Book Operations" and choose "Add a new book." Enter the required details like title, author, ISBN, publication date, and genre.
- **Borrow a Book**: Enter the ISBN and User ID to borrow a book. The system will mark the book as "Borrowed" if it is available.
- **View User Details**: Navigate to "User Operations" and provide the user ID to view the user's borrowing information.

## Input Validation
- ISBNs, user IDs, and names are validated using regular expressions to ensure they follow a specific format.
- Invalid inputs prompt an error message and request the user to try again.

## Edge Case Handling
- The system handles scenarios where there are no books, users, authors, or genres to display.
- Proper messages are displayed for empty lists, and operations such as borrowing or returning books that are unavailable are managed gracefully.

## Error Handling
- Error handling is implemented to catch and manage common issues.
  - **Invalid Input**: Users are informed if the input format is incorrect.
  - **Empty Records**: If there are no books, users, authors, or genres available, a proper message is displayed.

## Class Overview
- **`Library`**: Manages collections of books, users, authors, and genres.
- **`Book`**: Represents a book with attributes like title, author, ISBN, publication date, and availability status.
- **`User`**: Represents a library user, allows users to borrow and return books.
- **`Author`**: Stores information about authors, including their name and biography.
- **`Genre`**: Stores information about genres, including name, description, and category.

## Future Improvements
- **Database Integration**: Implement persistent data storage using SQLite or another relational database.
- **GUI**: Build a graphical user interface for better user experience.
- **Enhanced Features**: Add overdue penalties, reservation options, and book recommendations based on borrowing history.

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- The Python community and online tutorials for inspiration and guidance in building this library management system.
