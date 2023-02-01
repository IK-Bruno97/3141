#Here we build objects out of other objects.

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []
         
    def __str__(self):
        return "{} by {}".format(self.title, self.author)
        
    def addchapters(self, chapter):
        self.chapters.append(chapter)
           
    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
           result += ch.pagecount
        return result
           
           
class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
           
    def __str__(self):
        return f"{self.fname} {self.lname}"
           

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount
           
           
auth = Author("Chinue", "Achebe")
b1 = Book("Arrow of God", 39.4, auth) 
b1.addchapters(Chapter("Chapter 1", 122))         
b1.addchapters(Chapter("Chapter 2", 130))
print(b1)
print(b1.author)
print(b1.title)
print(b1.getbookpagecount())