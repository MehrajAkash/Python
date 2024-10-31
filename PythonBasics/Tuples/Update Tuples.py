
x = ('apple','banana','cherry')
y = list(x)
print(type(y))  # ['apple', 'banana', 'cherry'] -> list

y[0] = "kiwi"
x = tuple(y)
print(x) # ('kiwi', 'banana', 'cherry')  -> tuple

# ********* Add items *************
thistuple = ("Mango","Stravery")
y = list(thistuple)
y.append("Orange")
y.append("Palm")
thistuple = tuple(y)
print(thistuple) # ('Mango', 'Stravery', 'Orange', 'Palm')

# ********* Add another tuple**************
thistuple = ('Orange', 'Palm')
y = ('coconut','kiwi')
thistuple = thistuple + y
print(thistuple)
