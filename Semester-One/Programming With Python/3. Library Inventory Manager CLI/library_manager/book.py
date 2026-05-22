# Task 1: Book Class Design

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}, Status: {self.status})"
    
    def to_dict(self):
        return {'title': self.title, 'author': self.author, 'isbn': self.isbn, 'status': self.status}
    
    def issue(self):
        if self.status == 'issued':
            return False
        self.status = 'issued'
        return True
    
    def return_book(self):
        if self.status == 'available':
            return False
        self.status = 'available'
        return True
    
    def is_available(self):
        return self.status == 'available'