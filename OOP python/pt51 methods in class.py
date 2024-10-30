
class student:
    roll=""
    gpa = ""

    def setValue(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print('Roll: {0}   GPA: {1}' .format(self.roll, self.gpa))    


karim = student()
karim.setValue(103, 3.56)

Nasum = student()
Nasum.setValue(305, 4.89)

karim.display()
Nasum.display()