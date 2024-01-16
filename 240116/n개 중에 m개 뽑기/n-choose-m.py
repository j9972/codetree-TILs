n,m = map(int,input().split())

ans = []

def Print():
    for e in ans:
        print(e, end=' ')
    print()

# def choose(cur):
#     if cur == m+1:
#         Print()
#         return
    
#     for i in range(1,n+1):
#         if len(ans) == 0 or ans[-1] < i:
#             ans.append(i)
#             choose(cur + 1)
#             ans.pop()
# choose(1)

def choose(cur,cnt):
    if cur == n+1:
        if cnt == m:
            Print()
        return
    
    # for i in range(1,n+1):
    #     if len(ans) == 0 or ans[-1] < i:
    #         ans.append(i)
    #         choose(cur + 1)
    #         ans.pop()

    ans.append(cur)
    choose(cur + 1, cnt + 1)
    ans.pop()
    choose(cur + 1, cnt)

choose(1,0)