# Library Inventory Manager

A simple command-line application to manage a campus library's book catalog. Built with Python using Object-Oriented Programming principles.

<img width="977" height="260" alt="image" src="https://github.com/user-attachments/assets/e426c025-e2d5-414b-87f7-f44c0b5ba3f1" />

---

## Features

- **Add Books** – Add new books to the library catalog
- **Issue Books** – Mark books as issued to students/staff
- **Return Books** – Mark issued books as available again
- **Search Books** – Find books by title or ISBN
- **View All Books** – Display the entire catalog
- **Persistent Storage** – Data saved automatically to CSV file

---

## Project Structure

```
library-inventory-manager-Prabhat/
│
├── cli/
│   └── main.py              # Command-line interface
├── library_manager/
│   ├── book.py              # Book class definition
│   └── inventory.py         # Inventory management logic
├── catalog.csv              # Book data storage (auto-generated)
└── README.md                # This file
```

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/prabhatb-alt/library-inventory-manager-prabhatbhatia.git
   cd library-inventory-manager-prabhatbhatiaa
   ```

2. **Run the application**
   ```bash
   python -m cli.main
   ```

---

## Usage

When you run the program, you'll see this menu:

```
--- Library Inventory Manager ---
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit
```

### Example Workflow

**Adding a book:**
```
Choose option: 1
Title: Python Programming
Author: John Doe
ISBN: 978-0-123456-78-9
✓ Book added successfully
```

**Issuing a book:**
```
Choose option: 2
Enter ISBN: 978-0-123456-78-9
✓ Issued: Python Programming
```

**Searching books:**
```
Choose option: 5
1. Search by Title
2. Search by ISBN
Enter choice: 1
Enter title: Python
'Python Programming' by John Doe (ISBN: 978-0-123456-78-9, Status: issued)
```

---

## Data Storage

- Books are saved in `catalog.csv` with columns: `title`, `author`, `isbn`, `status`
- The file is created automatically on first run
- All changes are saved immediately

---

## Technical Details

**Built with:**
- Python 3.10+
- CSV for data storage
- Object-Oriented Programming (OOP)

**Key Classes:**
- `Book` – Represents a single book with title, author, ISBN, and status
- `LibraryInventory` – Manages the collection of books and file operations

---

## Requirements

- Python 3.7 or higher
- No external libraries required (uses standard library only)

---

## Assignment Tasks Completed

- ✅ Task 1: Book Class Design
- ✅ Task 2: Inventory Manager
- ✅ Task 3: File Persistence (CSV)
- ✅ Task 4: Menu-Driven CLI
- ✅ Task 5: Exception Handling & Logging
- ✅ Task 6: Project Packaging

---

## Author

- Prabhat Bhatia
- B.Tech CSE Cyber Security(First Semester)
- 21st November 2025
- Programming With Python - Lab Assignment 3