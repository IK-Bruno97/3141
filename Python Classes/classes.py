class Book:
    
    BOOK_TYPES = ("Hardcover", "eBook")

    __booklist = None
    
    def __init__(self, title, price, author, booktype):
        self.title = title
        self.price = price
        self.author = author
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError("Not a valid book type")
        else:
            self.booktype = booktype
        self.__secret = "Secret of this class"
   

   #an instance function     
    def settitle(self, newtitle):
        self.title = newtitle
        

    @classmethod #works on the entire class across all instances of the class.
    def getbooktypes(cls):
        return cls.BOOK_TYPES
        
        
    @staticmethod #put a global function in the class namespace
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    


    def __str__(self):
        return f"{self.booktype}. {self.title}, by {self.author}"
    
    def __repr__(self):
         return f"Title={self.title}"
        
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book with non-book")
        return (self.title == value.title and self.author==value.author and self.price==value.price)

    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book object with non-book")
        return self.price >= value.price

    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book object with non-book")
        return self.price < value.price

    def __getattribute__(self, name):
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p * d)
        return super().__getattribute__(name)

    def __getattr__(self, name):
       return name + ' is not a prop of Book'

    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError('Price must be float')
        return super().__setattr__(name, value)

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price



    def price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
        
    def discount(self, amount):
      #the underscore (_) lets others to know this method is intended to be internal to the class
        self._discount = amount
        
        
        
b1 = Book("Peace and War", 21.0, "John", "eBook")
b3 = Book("Peace and War", 21.0, "John", "eBook")
b2 = Book("Pride and Prejudice", 15.0, "J. Austen", "Hardcover")
#print(b1.price)
print(b2.getbooktypes())
#b1.discount(2.4)
#print(b1.price)
#print(b1.__secret)error
#print(b1._Book__secret)
#print(type(b1))
#print(type(b1)==type(b2))
#print(b1==b2)
#print(isinstance(b1, Book))
#print(isinstance(b1, object))
#thebook = Book.getbooklist()
#print(thebook)
#thebook.append(b2)
#thebook.append(b1)
#print(thebook)
#print(repr(b1))
#print(str(b1))
#print(b1==b3)
#print(b1==b2)
#print(b1 >= b2)
#books = [b1, b2, b3]
#books.sort()
#print([book.title for book in books])

#b1('Ann', "John", 10.5)
print(b1)