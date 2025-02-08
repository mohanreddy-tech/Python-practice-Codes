'''
In tuples we can store homogeneous as well as heterogeneous data.
in tuples are ordered collections of data.
Tuples are ordered collections of data.
Tuples are immutable. once we declare the tiples we cannot modifty it.

'''
tup1= (22.55, 23,'Kodnest',True,10)
print(tup1)

#tup1.remove(23)
#tup1.append(400)
#tup1.pop().
#tup1.pop()
#del tup1[]

#delete the complete tup1 object
#del tup1 
print(tup1[2]) #error


del tup1 
#print(tup1)

t1 = (1,2,3,4,5)
t2 = (4 ,5,6,7,8)
t3 = t1+t2
print(t3)

# create a singleton tuple:
tup = (50,)
print(tup,type(tup))


new_tup = {50,56,78,56}

#ele1 = new_tup[0]
#ele2 = new_tup[1]

#unpacking of tuple elements #group of elements
ele1,ele2,ele3,ele4 = new_tup
print('Value of ele1:',ele1)

