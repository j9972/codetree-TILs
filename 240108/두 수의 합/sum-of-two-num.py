from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 딕셔너리를 사용하여 각 요소의 출현 횟수 기록
num_count = defaultdict(int)
for num in arr:
    num_count[num] += 1

ans = 0
for num in arr:
    complement = k - num
    # 두 수의 합이 k가 되는 경우를 확인
    if complement in num_count:
        # 같은 요소끼리 조합하는 경우와 서로 다른 요소끼리 조합하는 경우 고려
        if complement != num:
            ans += num_count[complement]
        else:
            ans += num_count[complement] - 1

# 같은 요소끼리 조합된 경우의 수를 반으로 계산했으므로 2로 나눠줌
ans //= 2
print(ans)