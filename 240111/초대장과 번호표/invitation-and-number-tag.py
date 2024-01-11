from collections import deque

n,g = map(int,input().split())

group = [set() for _ in range(g)]
ppl = [[] for _ in range(n)]
invited = [False] * n

q = deque()
ans = 0

for i in range(g):
    nums = list(map(int,input().split()))[1:]

    for num in nums:
        num -= 1
        group[i].add(num)
        ppl[num].append(i)

q.append(0)
invited[0] = True

while q:
    x = q.popleft()
    ans += 1

    for g_num in ppl[x]:
        group[g_num].remove(x)

        if len(group[g_num]) == 1:
            p_num = list(group[g_num])[0]
            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)
print(ans)