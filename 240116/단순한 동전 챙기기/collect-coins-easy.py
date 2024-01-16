import sys
n = int(input())

s,e = None, None

num_list = list()
num_dict = {}

for i in range(n):
    input_list = list(input())
    for j in range(n):
        val = input_list[j]

        if val == 'S':
            s = (i,j)
        elif val == 'E':
            e = (i,j)
        elif str.isdigit(val):
            num = int(val)
            num_list.append(num)
            num_dict[num] = (i,j)

def dist(a, b):
    (ax, ay), (bx, by) = a, b
    return abs(ax - bx) + abs(ay - by)

length = len(num_list)

min_val = sys.maxsize

for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            move = 0

            p1 = num_dict[num_list[i]]
            p2 = num_dict[num_list[j]]
            p3 = num_dict[num_list[k]]

            coords = [s,p1,p2,p3,e]

            for idx in range(4):
                move += dist(coords[idx], coords[idx+1])
            
            min_val = min(min_val, move)
if min_val == sys.maxsize:
    print(-1)
else:
    print(min_val)