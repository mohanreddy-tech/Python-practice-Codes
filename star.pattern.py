rows = 4
col = 5
for i in range(rows):
    for j in range(col):
        if i==0 or i==3 or j==0 or j==4:
            print("*",end="")
        else:
            print(end=" ")
    print()