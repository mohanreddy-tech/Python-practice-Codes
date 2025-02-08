
#list_name[stsart:end-1:steps

li1 = [10,302,45,67,56,45]
sub_list = li1[::]

print(sub_list)

sub_list2 = li1[1::]
print(sub_list2) 

sub_list3 = li1[::2]
print(sub_list3)


reverse_li1 = li1[::-1]

print(reverse_li1)

print(li1[-1::])

'''
1.what is list Slicing 
2.Is used to create sublist from main list.
Syntex list_namee [start:end-1:steps]

reverse list: [::-1]
last ele [-1::]
'''

