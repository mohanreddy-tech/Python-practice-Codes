li1 = [1,2,3,4,5]
print(li1)
sq_li = []
for i in li1:
    sq_li.append(i**2)
    print(sq_li)


li1 = [1,2,3,4,8,10,34]
#list comprehension of syntex of the list
even = [i for i in li1 if i%2==0]

print(even)

li2 = [4,5,67,87,56,88]
duplicate_li1 = [i for i  in li2]

even = [i for i in li2 if 1 %2 ==0]
sq_list = [i**2 for i in li2]
new_li1 = [ele+2 for ele in li2]

print(even)
print(sq_list)
print(new_li1)

li3 = [4,5,67,89]

#when we have only if part then write it after for loop
#correct sytnex for the if and else condition 
number = ['even' if i%2==0 else 'odd' for i in li3]
new_li3 = [ele+2 for ele in li1]

print(new_li3)

print(number)

#when we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'odd' for  i in li3]

print(number)

#nested for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]

#multiple for loops inside list comprehension

li = [10,20] , [20,40],  [50,60]


new_li = [ele for i in li for ele in i]
print(li)

#hacker rank question of the list comprehension question

'''
1. r1 = upper limit 1 (0,1)
2. r2 = upper limit 2  (0,1 ,2)
3 . r3 = upper limit  (0,1)
sum = 2

(0,0,1),(0,0,0),(0,1,0),(1,1,1)
'''

[(i,j,k) for i in range(r1+1) for j in range(r2+1) for k in range(r3+1) if i+j+k !=2]








