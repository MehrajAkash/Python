
thislist = ["orange",'apple','mango','banana']
thislist.sort()
print(thislist)

thislist = [80,-20,5,-3,8]
thislist.sort()
print('Ascending sort: ', thislist)

# for descending sort: list.sort(reverse = True)

thislist = ['apple','orange','mango','kiwi','banana']
# thislist.sort(reverse=False)  ['apple', 'banana', 'kiwi', 'mango', 'orange']
thislist.sort(reverse=True)
print(thislist)  # ['orange', 'mango', 'kiwi', 'banana', 'apple']

thislist = [80,-20,5,-3,8]
thislist.sort(reverse=True)
print('Descending sort: ', thislist)

# sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n-50)

thislist = [40,50,58,92,20]
thislist.sort(key = myfunc)  # [50, 58, 40, 20, 92]
print(thislist)




# perform a case-insensitive sort of the list: 
thislist = ['banana',"Orange",'Kiwi','cherry'] 

"""
**** a way to sort case-sensitive list  but here letter case is changed******
newlist = []
for x in thislist:
    newlist.append(x.lower())
print('using for loop: ',newlist)    #  ['banana', 'orange', 'kiwi', 'cherry']
newlist.sort()     # ['banana', 'cherry', 'Kiwi', 'Orange']

**** another way to sort case-sensitive list  but here letter case is changed********
thislist = [x.lower() for x in thislist]
print(thislist)  # ['banana', 'orange', 'kiwi', 'cherry']
thislist.sort()  # ['banana', 'cherry', 'Kiwi', 'Orange']
"""
thislist.sort(key = str.lower)  # ['banana', 'cherry', 'Kiwi', 'Orange']
print(thislist)  

thislist = ['banana',"Orange",'Kiwi','cherry'] 
thislist.sort(key = str.lower, reverse= True)  # ['Orange', 'Kiwi', 'cherry', 'banana']
print('Reversed list: ',thislist)