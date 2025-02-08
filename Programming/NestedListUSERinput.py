#li = []
#sub_list_count = int(input())
#for i in range(sub_list_count):
 #   li.append([input(), float(input())])


li = list(map(int,input().split()))
d = {10:2, 20:3, 30:4}

for num, count in d.items():
    print(num, count) c