import sys
n = int(input())

s,e = None, None

num_list = []
num_dict = {}

for x in range(n):
    input_list = list(input())
    for y in range(n):
        val = input_list[y]

        if val == 'S':
            s = (x,y)
        elif val == 'E':
            e = (x,y)
        elif str.isdigit(val):
            num = int(val)
            num_list.append(num)
            num_dict[num] = (x,y)

num_list.sort()

length = len(num_list)
min_val = sys.maxsize

def dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            move= 0

            p1 = num_dict[num_list[i]]
            p2 = num_dict[num_list[j]]
            p3 = num_dict[num_list[k]]

            coords = [s, p1, p2, p3, e]

            for idx in range(4):
                move += dist(coords[idx], coords[idx+1])

            min_val = min(min_val, move)

if min_val == sys.maxsize:
    print(-1)
else:
    print(min_val)