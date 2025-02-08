li = 1,34,56,32,56,78,56,21,79,53,21

li = list(map(int,input().split()))

even, odd = 0
for i in li:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers: ",even)
print("odd numbers: ",odd)    
