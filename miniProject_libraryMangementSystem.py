class Library:
    def __init__(self):
        self.books=[]
        self.noOfBooks=0
    @property
    def printing_books(self):
        return f'The books in the library are : {self.books}'
    @printing_books.setter
    def adding_a_book(self,book):
        self.books.append(book)
        self.noOfBooks+=1
    @property
    def printing_noOfBooks(self):
        return f"The number of books are : {self.noOfBooks}"
x=Library()
x.adding_a_book='Think and grow rich'
x.adding_a_book='Atomic habits'
x.adding_a_book='Mahabharat'
x.adding_a_book='Bhagawat geeta'
print(x.printing_books)
print(x.printing_noOfBooks)