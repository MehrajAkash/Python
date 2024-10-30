import cmath
# find the area of a triangle
a = 5
b = 6
c = 7
#calculate the semi-perimeter
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.3f' %area)

# Quadratic equation ax**2+bx+c = 0
a = 1
b = 5
c = 6
#calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

print('The solutions are {0} and {1}' .format(sol1, sol2))

print('value of a is {0:.3f}' .format(a))