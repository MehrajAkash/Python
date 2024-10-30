
class triangle:
    base = ''
    height = ''
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def cal_area(self):
        area = 0.5 * self.base * self.height
        print('Triangle Area: ',area)

t1 = triangle(10,20)
t1.cal_area()

t2 = triangle(30,40)
t2.cal_area()