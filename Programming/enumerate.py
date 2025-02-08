
li = [10,20,30]

for idx, ele in enumerate(li):
    print(f"Index of {ele} is: {idx}")


#wap to print all elements even index elements:
for idx, ele in enumerate(li):
    if idx % 2 == 0:
        print(f"Element at even index {idx} is: {ele}")