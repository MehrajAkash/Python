
fruits = ('applee', "bananaa", "cherryy")
(gre,yel,red) = fruits
print(gre,yel,red)

# ******** Using Asterisk ********
fruits = ('mango','strawberry','apple','cherry','banana')
(g,y,*r) = fruits
print(g)
print(y)
print(r) # ['apple', 'cherry', 'banana']

print()
fruits = ('mango','strawberry','apple','cherry','banana')
(g,*y,r) = fruits
print(g)
print(y) # ['strawberry', 'apple', 'cherry']
print(r)


