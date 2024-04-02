n = int(input())
clients = list(map(int,input().split()))
leader_can_cnt, teammate_can_cnt = map(int,input().split())

tot = 0
for i in clients:
    tot += 1
    i -= leader_can_cnt

    if i > 0:
        if i <= teammate_can_cnt:
            tot += 1
        else:
            tot += i // teammate_can_cnt

            if i % teammate_can_cnt != 0:
                tot += 1
print(tot)