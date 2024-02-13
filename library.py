
class Library:
    def __init__(self , books) :
        self.books = books
        self.issue = {}
    def displayAvailableBooks(self) :
        for i in self.books :
            print(i)
    def borrowBook(self , name , bookname) :
        if bookname in self.books :
            self.books.remove(bookname)
            self.issue[bookname] = name
            print(f"{name} borrowed {bookname}")
        else :
            print("This book is not in Library")
        
    def returnBook(self , bookname) :
        if bookname in self.issue :
            self.books.append(bookname)
            print(f"{self.issue.pop(bookname)} returned {bookname}")
        else :
            print("This book is not issued")
    
    def donateBook(self,bookname) :
        self.books.append(bookname)
        print(f"{bookname} is donated")

class Student:
    def requestBook(self) :
        studentname = input("Enter your name : ")
        bookname = input("Enter the name of the book you want : ")
        return studentname , bookname 
    
    def returnBook(self) :
        studentname = input("Enter your name : ")
        bookname = input("Enter the book you want to return : ")
        return studentname , bookname 

    def donateBook(self) :
        bookname = input("Enter the name of the book you want to donate : ")
        return bookname 

def display_available_books():
    available_books = "\n".join(IIITlibrary.books)
    available_books_label.config(text=available_books)

def borrow_book():
    student_name, book_name = student.requestBook()
    IIITlibrary.borrowBook(student_name, book_name)
    display_available_books()

def return_book():
    student_name, book_name = student.returnBook()
    IIITlibrary.returnBook(book_name)
    display_available_books()

def donate_book():
    book_name = student.donateBook()
    IIITlibrary.donateBook(book_name)
    display_available_books()

def display_issued_books():
    issued_books = "\n".join([f"{owner} borrowed {book}" for book, owner in IIITlibrary.issue.items()])
    issued_books_label.config(text=issued_books)

IIITlibrary = Library(["Let us C", "Core C", "Core Java", "Learn Python the hard way", "Source Java"])
student = Student()