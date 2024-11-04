
class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print('In shape class')

class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Triangle area: %d" %area)

class rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Rectangle area: ",float(area))


tr = triangle(10,20)
tr.area()
rt = rectangle(20,20)
rt.area()
