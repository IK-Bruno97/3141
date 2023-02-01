#define a template for a consumers of base classes to inherit from. Child classed cant create instance of the base class, can only use the blueprint/idea to create implementations of the idea.

from abc import ABC, abstractmethod

#eg of an Interface
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass
  
  
  
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def CalcArea(self):
        pass
        
class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
        
    def CalcArea(self):
        return 3.14 * (self.radius ** 2)
        
    def toJSON(self):#interface 
        return f"{{\"Circle\":{str(self.CalcArea())}}}"
        
        
class Square(GraphicShape):
     def __init__(self, side):
         self.side = side
         
     def CalcArea(self):
       return self.side * 4
       
c = Circle(10)
print(c.CalcArea())
print(c.toJSON())