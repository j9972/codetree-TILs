from itertools import combinations

def three_sum_count(arr, k):
    ans = 0
    for comb in combinations(arr, 3):
        if sum(comb) == k:
            ans += 1
    return ans

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = three_sum_count(arr, k)
print(result)