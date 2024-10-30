from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,base,height):
        self.base = base 
        self.height = height
        
    @abstractmethod
    def area(self):
        pass

class triangle(shape):
    def area(self):
        tarea = 0.5 * self.base * self.height
       print("Triangle Area: tarea",tarea)
    



tr = triangle(10,20)
tr.area()