'''
1.In list we can store homogenous and hetrogenous data.
2.in list we can store duplicate values.
3.list order of data collection of data: order of insertion will remain
as it is in the output.
4.list mutable: once declare the list we can modify it.
'''
li1 = [10,20,44.45,True,'Kodnest',20]
print(li1, type(li1))

# append() : will add element at the end of the list or only one element at a time.
li1.append(300)
print(li1)

#insert (index , element):Adds an ele . specified index
li1.insert(1,15)
print(li1) 

#remove the elements(ele): removes the first occurances of the specified ele.
li1.remove(20)
print(li1)



#in and not in operator:

print(2000 in li1) #False
print('Kodnest' in li1) #True

#pop(): without argument will delete  and return last ele. from list
removed_ele = li1.pop()
print(removed_ele)  #300
print(li1) #[10, 15, 44.45, true, 'Kodnest', 20]

#pop(index): will delete and return the element at the specified index.

removed_ele=li1.pop(4)
print(removed_ele) #Kodnest
print(li1) #[10, 15, 44.45, true, 20]


#del keyword:
#li1.pop(1)
del li1[1]
print(li1) #[10, 44.45, true, 20]

del li1
print(li1) #NameError: name 'li1' is not defined















