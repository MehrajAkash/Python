
thislist = ["apple","banana",'cherry'] # thislist is a 'list'
print(thislist)
print(f"index 2 value: {thislist[2]}")
print(f"type of thislist: {type(thislist)}")
print(f"last index value: {thislist[-1]}")
print()

if 'banana' in thislist:
    print('Yes, "banana" is in the thislist \n')

list2 = ["hello","everyone",'Danish','German','Swedish'] # list2 is a 'list'
print(list2)
print(f"index 1 value: {list2[1]}")
print(f"type of list2: {type(list2)}")
print(f"index 1 to 3 value: {list2[1:4]}")
print(f"value before index 3 : {list2[:3]}")
print(f"value from index 3 to last: {list2[3:]}")
print(f'last index values: {list2[-1]}')
print(f"last 3 values: {list2[-3:]}")
print(f"2 values before last index: {list2[-3:-1]} \n")

list3 = [True,45,False,False,"mall",'alone']
print(list3)

list5 = list(('my','me')) # list5 is 'list'
print(type(list5))
print(f'index 0 value: {list5[0]} \n')

list4 = ('English','Spanish','Russian') # list4 is a 'tuple'
print(f'type of list4 variable: {type(list4)} \n') 