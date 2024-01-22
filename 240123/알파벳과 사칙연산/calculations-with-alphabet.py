n = input()

oper , alpha = list(), list()

for i in n:
    if i.isalpha():
        alpha.append(i)
    else:
        oper.append(i)

dic = {}
for i in alpha:
    dic[i] = 0

ans = []
max_val = 0

def calc():
    global dic

    for i, k in enumerate(dic.keys()):
        dic[k] = ans[i]
    
    cnt = dic[alpha[0]]
    for i, op in enumerate(oper):
        next_val = dic[alpha[i+1]]
        if op == '+':
            cnt += next_val
        elif op == '-':
            cnt -= next_val
        else:
            cnt *= next_val
    
    return cnt


def choose(cnt):
    global max_val

    if cnt == len(dic):
        max_val = max(max_val, calc())
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cnt+1)
        ans.pop()

choose(0)
print(max_val)