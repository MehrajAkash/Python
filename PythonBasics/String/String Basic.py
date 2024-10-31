# multiline string
a = """Bangladesh India, Nepal
Bhutan, Srilanka
Maldives"""
print(a) 

a = 'Hello Bangladesh'
print(a[2])
print( f"{a[4]}"  + "\n")

for x in 'banana':
    print(x)

a = 'Hello Bangladesh'
print(len(a),"\n")

a = 'Hello Bangladesh'
print('Hello' in a) # True
print(' ' in a) # True

txt = 'I like Sweden'
if 'like ' in txt:  # any character can be exist, even empty space also
    print("Yes, 'like' is present.")

if 'fin' not in txt:
    print('No, "finland" is not Present')    


    