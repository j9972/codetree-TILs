n = int(input())
n_list = list(map(int,input().split()))
n_set = set(n_list)

m = int(input())
m_list = list(map(int,input().split()))

for e in m_list:
    if e in n_set:
        print(1, end=' ')
    else:
        print(0, end=' ')