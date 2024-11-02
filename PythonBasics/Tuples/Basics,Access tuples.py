# tuple allows duplicate value
thistuple = ('apple','banana','cherry','banana') 
print(thistuple)
print(f"tuple length: {len(thistuple)}") # 4

# One item tuple, remember the comma
thistuple = ('apple',)
print(type(thistuple)) # <class 'tuple'>

tuple1 = ('abc',34,True,"male")
print(tuple1)

thistuple = tuple(("apple","banana","cherry"))
print(thistuple)

# *********** Access Tuple ****************
thistuple = ("apple","banana","cherry")
print(thistuple[1])

thistuple = ("apple","bcd",'efg','ijk','lmn')
print(thistuple[1:4]) #  ('bcd', 'efg', 'ijk')    
print(thistuple[-5:-1])  # ('apple', 'bcd', 'efg', 'ijk')

if "bcd" in thistuple:
    print("Yes, 'bcd' is in the thistuple")
