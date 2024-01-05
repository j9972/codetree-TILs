n,m = map(int,input().split())
n_arr = list(map(int,input().split()))
m_arr = list(map(int,input().split()))

dic = dict()
for i in n_arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for mm in m_arr:
    if mm in dic:
        print(dic[mm],end= ' ')
    else:
        print(0,end= ' ')