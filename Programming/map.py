#map(function , iterable object) ----> Iterator object 

def double(x):
    return x*2

li = [1,2,3,4]

double_li = list(map(double, li))
print(double_li)

tup = ('10','20','30','40')

print(tup)

tup = tuple(map(int,tup))
print(tup)

li2 = [1,5,4,7]
print(li2)
li2 = list(map(float,li2))
print(li2) # [1.0,5.0,4.0,7.0]



