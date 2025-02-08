#reverse() will reverse the original number
li = [10,5,20,7]
print('Before Reverse:', li)
li.reverse()
print('After Reverse:' , li) 

#reversed(iterable_object):

li2 = [11,23,45,66,54]
                 
                 #list is must be convert into tuple are list inside iterable object
reverse_li2=list(reversed(li2))
print(reverse_li2)

li3 = [1,5,6,7,8,5]

new_reverse_li3 = list(reversed(li3))#creating new reverse list
li3.reverse() #---> reverse original list


