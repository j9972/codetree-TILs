n = int(input())
arr = input()


cur_x ,cur_y= -1, -1

for i in range(n):
    dist = 0
    for j in range(i+1,n):
        if i == j:
            continue

        if arr[j] == '1' or j == n-1:
            if dist < j-i:
                dist = j - i
                cur_x ,cur_y = i,j
                break
        
print(cur_x ,cur_y)
#arr[cur_idx] = '1'

max_dist = list()

for i in range(n):
    for j in range(i+1,n):
        if i == j:
            continue

        if arr[i] == '1' and arr[j] == '1':
            max_dist.append(j-i)
            break

print(max_dist)
max_dist.sort()

max_dist_data = max_dist.pop()

max_dist.append(max_dist_data // 2)

max_dist.sort()

print(max_dist[0])