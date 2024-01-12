import heapq

for tc in range(int(input())):
    m = int(input())
    arr = list(map(int,input().split()))

    for idx in range(1,m+1):
        if idx % 2 == 1:
            #print("heap :",arr[:idx])
            #print(sum(heap), (idx + 1) // 2 - 1 , heap[0])
            print(arr[(idx + 1) // 2 - 1],end =" ")
    print()