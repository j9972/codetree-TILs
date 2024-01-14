n,m = map(int,input().split())

lines , selected_lines = list(), list()

ans = m

for i in range(m):
    a,b = tuple(map(int,input().split()))
    lines.append((b, a-1)) # a가 1부터 시작하니까

lines.sort()

def possible():
    num1, num2 = [i for i in range(n)], [i for i in range(n)]
	
    for _, idx in lines:
        num1[idx], num1[idx + 1] = num1[idx + 1], num1[idx]
    for _, idx in selected_lines:
        num2[idx], num2[idx + 1] = num2[idx + 1], num2[idx]
    
    for i in range(n):
        if num1[i] != num2[i]:
            return False
    
    return True
        

def find_min_lines(cnt):
    global ans
    
    if cnt == m:
        if possible():
            ans = min(ans, len(selected_lines))
        return
    
    selected_lines.append(lines[cnt])
    find_min_lines(cnt + 1)
    selected_lines.pop()
	
    find_min_lines(cnt + 1) # 선택되지 않은 거에 대해서 재귀함수 호출


find_min_lines(0)
print(ans)