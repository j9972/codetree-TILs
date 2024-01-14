string = input()

oper , alpha = list(), list()

for i in string:
    if i.isalpha():
        alpha.append(i)
    else:
        oper.append(i)

unique_alpha = {
    a:0
    for a in set(alpha)
}
ans = []
max_val = -1

def println():
    global max_val, unique_alpha

    for i, k in enumerate(unique_alpha.keys()):
        unique_alpha[k] = ans[i]
    
    cnt = unique_alpha[alpha[0]]
    for i, op in enumerate(oper):
        next_val = unique_alpha[alpha[i+1]]
        if op == '+':
            cnt += next_val
        elif op == '-':
            cnt -= next_val
        else:
            cnt *= next_val
    
    max_val = max(max_val, cnt)

def choose(cnt):
    if cnt == len(unique_alpha):
        println()
        return


    for i in range(1,5):
        ans.append(i)
        choose(cnt+1)
        ans.pop()
choose(0)
print(max_val)