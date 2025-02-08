'''
li  = input ('Enter space separated elements ')
print(li,type(li)) 

#split is used for the converted string to list 

li = li.split()
print(li)

li = list(map(int,li))
print(li)

tup = tuple(map(input('Enter space separated elements ').split()))

print(tup)
'''

li = [10,12,45,67,44]
li = list(map(int,input().split()))

print([ i for i in li if i%2 == 0])