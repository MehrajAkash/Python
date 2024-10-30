
class student:
    name = ''
    roll = ''
    gpa = ""

    def  __init__(self,name,roll,gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print("Name: {0}    Roll: {1}   GPA: {2}" .format(self.name, self.roll, self.gpa))  


rahim = student("Rahim",312, 4.83)
rahim.display()          