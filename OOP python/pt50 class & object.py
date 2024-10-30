class student:
    roll = ""
    gpa = ""

    def display(self):
        print('In display function: ')
        print("Roll: {0}   Gpa: {1}" .format(self.roll, self.gpa))


rahim = student()
print(isinstance(rahim,student))  # isinstance(rahim,student)  returns true where rahim is a object of student() class

rahim.roll = 101
rahim.gpa = 3.75

print(f"Roll: {rahim.roll}   Gpa: {rahim.gpa}")

rahim.display()