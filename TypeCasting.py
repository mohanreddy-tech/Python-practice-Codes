# if string is holding integer value then we can convert it to integer

a  = '30'
print(a,type(a))

b = int(a)
print(b, type(b))


#str to integer conversion in not allowed

x = 'Kod'
print(x, type(x))
# y = int(x)
# print(y, type(y))

#p = float(input ('Enter Float type data'))
#print(p, type(p))


#bool()

q = ''
print(q,type(q))
q = bool(q)
print(q, type(q))
print(q, type(q))

'''
1.while converting int to bool for all non zero values we will get True.
2.while converting int to bool for 0 and empty strings we will get False.
'''