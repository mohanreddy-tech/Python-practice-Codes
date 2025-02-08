
d1 = {'name:': 'Tom', 'age': 10,'phone': 1234567890,'age': 20}


print(d1,type(d1))


#in dict we cannot store duplicate keyys.


d1['name']= 'mohan'
print(d1)

#in dict we can store duplicates values.
marks = {'maths': 90, 'science': 90, 'maths': 90} #allowed
print(marks)


#dict is mutable

d1['name'] = 'mohan'

print(d1)


for i in d1.keys():
    print(i)


for i in d1.values():
    print(i)

for i in d1.items():
    print(i)

list(), tuple(), set(), dict()

int(), float(), str(), bool(), complex()


