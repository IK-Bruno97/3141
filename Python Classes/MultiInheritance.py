#This kind of inheritance is mainly useful in the idea of an 'interface' (promise). See Abstract continuation for an eg of 'Interface'

class A:
    def __init__(self, foo, name):
        super().__init__()
        self.foo = foo
        self.name = name
         
class B:
    def __init__(self, bar, name):
        super().__init__()
        self.bar = bar
        self.name = name
          
          
class C(A, B):
    def __init__(self):
        super().__init__()
        
    def showprops(self):
        print(self.foo)
        print(self.bar)

print(C.showprops())           
print(C.__mro__) #to see resolution order which self.name is printed from which base
        