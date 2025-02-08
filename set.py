'''
1.in set we can Homogeneous as well as heterogeneous data.
2. set is mutable.
3.set is an unordered collection of data.
4.set does not support indexing of data.
5.set does not support slicing of data.
6.in set we cannot stroe duplicates.
'''

s1 = {10,True,'mohan',10,34,56,67}

print(s1),type(s1)  # {True, 10, 34, 67, 'mohan', 56} <class 'set'>
#print(s1[0])  # TypeError: 'set' object is not subscriptable

#add(): used to add element in the set

s1.add(100)
print(s1) # {True, 34, 100, 67, 10, 'mohan', 56}

s1.remove(55.76)
print(s1) # {True, 34, 100, 67, 10, 'mohan', 56}


#pop(): without index will delete and return one element from the set.
poped_ele = s1.pop()
s1.pop(poped_ele)
print(s1) # {34, 100, 67, 10, 'mohan', 56}

del s1[2] #error

del s1








