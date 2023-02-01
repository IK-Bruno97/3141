class Pub: 
    def __init__(self, title, price):
        self.title = title
        self.price = price
        
class Period(Pub):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher
        
class Book(Pub):
    def __init__(self, title, author, pages, price):
        super.__init__(title, price)
        self.author = author
        self.pages = pages
        
        
class Magazine(Pub):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period