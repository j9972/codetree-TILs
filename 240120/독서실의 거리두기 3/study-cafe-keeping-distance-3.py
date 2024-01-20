n = int(input())
arr = input()

max_dist = list()

for i in range(n):
    for j in range(i+1,n):
        if i == j:
            continue

        if arr[i] == '1' and arr[j] == '1':
            max_dist.append(j-i)
            break

max_dist.sort()

max_dist_data = max_dist.pop()

max_dist.append(max_dist_data // 2)

max_dist.sort()

print(max_dist[0])