'''#Strings immutable:
# 1,once we declare the strings we cannot modifty it, if we try t omoduity thw string it will create new string object
# 2, Strings it will create new String

#if we string does not have any reference variables then will be removed.
3.Python internally uses String intering.

4.String interning is the process of checkung string intern pool before creating
any new object

whenever we want t ocreate new object ,python first will check string
intern pool, wheather that object already exist or not

when object already exist in the string intern records then address 
of existing object will be reused.

'''
#s1 = 'kodnest'
#s1=s1.upper()
#print(s1)


#s1 = 'K'
#print(s1, id(s1))

s1 = 'Hello'
s2 = 'world'
print(s1, id(s1))
print(s2, id(s2))

print('s1 of H:',id(s1[0]))
print('s2 ID of w:',id(s2[0]))

print('s1 of o:',id(s1[-1]))
print('s2 ID of o:',id(s2[1]))

print('s1 ID of l:',id(s1[2]))
print('s1 ID of l:',id(s1[3]))
print('s2 ID of l:',id(s1[3]))