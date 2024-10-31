# ********** Slicing String **************
b = "Hello, ,World"
print(b[1:6]) # ello,
print(b[:9])  # Hello, ,W
print(b[3:])   # lo, ,World
print(b[-3]) # r
print(b[-5:]) # World
print(b[-5:-1]) # Worl
print(b[:-5]) # 'Hello, ,'


# ********* Modifying String ************
b = "Hello, ,World"
print(b.upper()) # HELLO, ,WORLD
print(b.lower()) # hello, ,world

 # Removing white space from teh begining or the end
b = "      Hello, , ,World   "
print(b.strip())  # Hello, , ,World

a = "Hi i,j,, Mohammed,Hossain"
print(a.split(',')) # ['Hi i', 'j', '', ' Mohammed', 'Hossain']     split value","
a = 'Hi I am Bangladesh'
print(a.split(" ")) # ['Hi', 'I', 'am', 'Bangladesh']






